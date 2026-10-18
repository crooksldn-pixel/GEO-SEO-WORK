# 04 — Merchant Center results (account 5860086407)

This is the results file the brief asked for at `cowork-results/04-merchant-center.md`. That folder isn't reachable from this session, so the file lives here. `cowork/programme-records` can merge it from this branch.

Session: Merchant Center only. Nothing changed in Shopify. Nothing saved in Merchant Center without George's yes.

## Status by task

| Task | State | Detail |
|---|---|---|
| A. Export and summarise | Done; one part open | Products 16 Oct and issues 18 Oct: [baseline-2026-10-16.md](baseline-2026-10-16.md). The comparison against the 11 findings in `03-merchant-feed.md` is open, because that file isn't available here. |
| B. Invalid-GTIN attribute rules | Can't be done as written; not needed now | No Attribute rules on Shopify's Merchant API sources, and no GTIN issue live. See FINDINGS 2. |
| C. Shipping check | Done | £3 and free from £30 match. Handling is 0 days; free tiers say 2–4 days; cut-off is 12:00 AM. See FINDINGS 3. |
| D. Tee handling time and shipping_label | Waiting on George | Needs the print-on-demand time. The route is still to be confirmed (NEXT 2). |
| E. Re-check and opt-in call | Scheduled | 29 Oct 09:00 GMT reminder in the Cowork chat. |
| F. Titles and is_bundle | Proposals below | is_bundle is already "yes" on all 4 sets. |

## Account snapshot

| | 16 Oct (Overview) | 18 Oct (Products) |
|---|---|---|
| Total offers | 18.6K | 18,554 |
| Approved | 17.7K | — |
| Limited | 739 | — |
| Not approved | 77 | 76 (the Cream Cap × 76 feed labels) |

Issues on 18 Oct, by type:

| Issue | Offers | Cause |
|---|---|---|
| Missing Korean business registration number | 254 | South Korea is a Shopify Markets market |
| Missing shipping info in some countries | 254 | Liechtenstein on the CHF source (244), plus the 10 hand-added duplicates |
| Missing product image | 76 | Cream Cap, every label |
| Mismatched currency in shipping information | 10 | Hand-added `CROOKSRELEASESEPT` duplicates |
| Unsupported currency | 10 | The same 10, in South Korea |

Account issues: "Invalid business name" (CROOKSLDN, shown as crooksldn.com), and "No Google Ads account linked", which is expected.

## Opt-in reading as of 18 Oct (provisional; decided 29 Oct)

- **Core feed:** all 25 Shopify products are approved for the UK, apart from the Cream Cap, which product-data item A is pulling. On feed cleanliness alone, that points to **stay opted in**.
- **Against:** the auto-add adds products that aren't in any data source. Pulling the cap from the Google channel makes it a candidate again (FINDINGS 7), and the 30 products Google found can't be inspected before they're added.
- **The 29 Oct call** will rest on three things:
  - whether the cap and the duplicates are gone
  - whether product-data's gender, age group and colour writes have processed without new disapprovals
  - whether "Found by Google" still shows 30 products

## Proposals waiting for George's yes

Nothing below has been done.

### P1 — Delete the 10 hand-added `CROOKSRELEASESEPT` products

- **Where:** Products > All products, filtered to the "Merchant Center · CROOKSRELEASESEPT" source. Select the 10 products, then delete. The source itself and the 76 Shopify sources stay untouched.
- **Before:** 10 extra offers, IDs `G-65230983` to `G-65230992`. Titles are all caps, with no brand, colour, category or size. They're eligible in the UK next to the Shopify listings for the same URLs, and disapproved in 33 other countries.
- **After:** only Shopify's complete listings remain. The currency issues go to 0, and missing-shipping drops by 10.
- **Risk:** if George added them on purpose, for example to target countries Shopify doesn't, that coverage is lost. Shopify already sends all 10 products to 76 feed labels.
- **Question for George:** are these a September leftover, and may this session delete them?

### P2 — Business name

- **Where:** Settings > Business info > Business name.
- **Before:** "CROOKSLDN", which Google rejects, so it shows the seller as "crooksldn.com".
- **After:** "Crooks LDN", one of George's confirmed alternates.
- **Question for George:** "Crooks LDN", or keep "CROOKSLDN" and accept the domain as the seller name?

### D — Tee handling time (needs George's number first)

- **Before:** every tee offer sends handling 0–0 days, and the site says "ships today".
- **After (once confirmed):** tee offers carry `min_handling_time` and `max_handling_time` equal to the real production + dispatch time, plus `shipping_label` = `print-on-demand`.
- **Route:** a supplemental source on the Shopify API sources, if Merchant Center allows it (to be checked). Otherwise this has to be fixed on the Shopify side.
- **Question for George:** how many working days from order to dispatch for a tee?

## F — Title proposals (for `cowork/product-data` to apply as Shopify SEO titles)

The Google channel sends the Shopify SEO title as the feed title. Most titles are already in mixed case, with the product name followed by "| CROOKSLDN", so they're left alone. Only these need changing:

| Product | Feed title now | Proposed |
|---|---|---|
| Charcoal Cellblock Crewneck | CHARCOAL CELLBLOCK CREWNECK | Charcoal Cellblock Crewneck — 450gsm Fleece \| CROOKSLDN |
| Double-Agent Puffa | Double-Agent Puffa \| Heat-Reactive Puffer Jacket | Double-Agent Puffa — Heat-Reactive Puffer Jacket \| CROOKSLDN |
| Major League Crooks Cap (Cream) | MAJOR LEAGUE CROOKS CAP (CREAM) | Major League Crooks Cap — Cream \| CROOKSLDN (only once it's relisted with a photo) |
| 3 tees | "…Cotton…" | Already covered by product-data C2–C4 |

The crewneck title follows the existing "Charcoal Cellblock Shorts — 450gsm Fleece" title, and 450gsm is a confirmed fact for crewnecks. is_bundle needs no change.

## Changes made

None.

| Time | Change | Before | After | George's yes |
|---|---|---|---|---|
| — | — | — | — | — |

## Next check

Thu 29 Oct 2026 (task E). The opt-out deadline is Sun 1 Nov, and auto-add starts Mon 2 Nov.
