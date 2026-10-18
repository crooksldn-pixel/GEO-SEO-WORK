"""Summarise a Merchant Center "All products" export and a "Needs attention" issues export.

Usage:
  python3 gmc_summary.py products_<date>.tsv [product_issues_<date>.csv]

The products export comes from Products > All products > download (a zip holding one TSV).
The issues export comes from Products > Needs attention > All products that need attention > download.
Prints markdown. Used for the 16/18 Oct baseline and for the 29 Oct re-check (task E).
"""
import csv, collections, re, sys

csv.field_size_limit(10**9)
SHIP = 'shipping(country:free shipping threshold:max handling time:max transit time:min handling time:min transit time:price:service)'


def ean_ok(code):
    """GS1 check digit for 8/12/13/14-digit codes."""
    if not re.fullmatch(r'\d{8}|\d{12,14}', code):
        return False
    d = [int(c) for c in code]
    body, check = d[:-1], d[-1]
    total = sum(v * (3 if i % 2 == 0 else 1) for i, v in enumerate(reversed(body)))
    return (10 - total % 10) % 10 == check


def products(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    labels = collections.Counter(r['feed label'] for r in rows)
    print(f'## Products export: {path}\n')
    print(f'- Rows (offers): {len(rows)}')
    print(f'- Feed labels: {len(labels)}')
    odd = {k: v for k, v in labels.items() if v != max(labels.values())}
    print(f'- Labels with an unusual row count: {odd}')
    g = [r for r in rows if re.fullmatch(r'\d+', r['gtin'])]
    print(f'- Offers sending a numeric gtin: {len(g)} '
          f'({len(set(r["merchant item id"] for r in g))} variants; '
          f'lengths {dict(collections.Counter(len(r["gtin"]) for r in g))}; '
          f'checksum-valid {sum(ean_ok(r["gtin"]) for r in g)})')
    for code in sorted(set(r['gtin'] for r in g)):
        owners = sorted(set(r['title'].split(' — ')[0] + ' ' + r['size'] for r in g if r['gtin'] == code))
        print(f'  - {code} (checksum {"ok" if ean_ok(code) else "FAIL"}): {", ".join(owners)}')
    gb = [r for r in rows if r['feed label'] == 'GB']
    print(f'\n### GB feed label: {len(gb)} offers\n')
    print('| Product | Offers | In stock | GPC | Colour | is_bundle | GTIN sent | Extra images | Weight values |')
    print('|---|---|---|---|---|---|---|---|---|')
    grp = collections.OrderedDict()
    for r in gb:
        grp.setdefault(r['item group id'], []).append(r)
    for rs in grp.values():
        t = re.sub(r' \| CROOKSLDN.*$', '', rs[0]['title'])
        t = re.sub(r'\s+(XS|S|M|L|XL)$', '', t).replace('|', '\\|')
        gpc = ', '.join(sorted(set(x['google product category'] for x in rs))) or '—'
        col = ', '.join(sorted(set(x['color'] for x in rs if x['color']))) or '—'
        print(f"| {t} | {len(rs)} | {sum(x['availability']=='in stock' for x in rs)} | {gpc} | {col} | "
              f"{'yes' if all(x['is bundle']=='yes' for x in rs) else '—'} | "
              f"{sum(1 for x in rs if x['gtin'])} | {sum(1 for x in rs if x['additional image link'])} | "
              f"{', '.join(sorted(set(x['shipping weight'] for x in rs)))} |")
    print('\nGB item-level shipping values:')
    for k, v in collections.Counter(r[SHIP] for r in gb).items():
        print(f'- {v} offers: `{k}`')
    other = [r for r in rows if r['feed label'] not in ('GB',) and not r['id'].startswith('shopify_')]
    if other:
        print(f'\nOffers not from Shopify: {len(other)}')
        for r in other:
            print(f"- {r['id']} | {r['feed label']} | {r['title']} | {r['price']} | brand={r['brand'] or '—'}")


def issues(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8')))
    print(f'\n## Issues export: {path}\n')
    print(f'- Rows (issue × destination × country): {len(rows)}')
    print(f'- Item status: {dict(collections.Counter(r["Item status"] for r in rows))}\n')
    print('| Issue | Severity | Offers | Variants | Feed labels | Countries | Products |')
    print('|---|---|---|---|---|---|---|')
    for t in sorted(set(r['Issue title'] for r in rows)):
        rs = [r for r in rows if r['Issue title'] == t]
        prods = collections.Counter(re.split(r' \| | — ', r['Title'])[0] for r in rs)
        print(f"| {t} | {', '.join(sorted(set(r['Issue severity'] for r in rs)))} | "
              f"{len(set((r['Item ID'], r['Feed label']) for r in rs))} | {len(set(r['Item ID'] for r in rs))} | "
              f"{', '.join(f'{k} ({v})' for k, v in collections.Counter(r['Feed label'] for r in rs).most_common(4))} | "
              f"{', '.join(sorted(set(r['Country'] for r in rs)))[:120]} | {len(prods)} |")


if __name__ == '__main__':
    products(sys.argv[1])
    if len(sys.argv) > 2:
        issues(sys.argv[2])
