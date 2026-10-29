# 04 — Merchant Center results (account 5860086407)

This is the results file the brief asked for at `cowork-results/04-merchant-center.md`. That folder isn't reachable from this session, so the file lives here. `cowork/programme-records` can merge it from this branch.

Session: Merchant Center only. Nothing changed in Shopify. Nothing saved in Merchant Center without George's yes.

## Status by task

| Task | State | Detail |
|---|---|---|
| A. Export and summarise | Done | [baseline-2026-10-16.md](baseline-2026-10-16.md); the 11-findings comparison is in [findings-map-03.md](findings-map-03.md). |
| B. Invalid-GTIN attribute rules | Can't be done as written; not needed now | No Attribute rules on Shopify's Merchant API sources, and no GTIN issue live. See FINDINGS 2. |
| C. Shipping check | Done | £3 and free from £30 match. Handling is 0 days; free tiers say 2–4 days; cut-off is 12:00 AM. See FINDINGS 3. |
| D. Tee handling time and shipping_label | Approved; waiting on George's yes in chat | 2–3 days (owner decision #1). The file `gmc-supplemental-tee-handling-GB.tsv` is ready, for 90 GB tee variants. |
| E. Re-check and opt-in call | Done, 29 Oct | **Stay opted in.** The UK is clean. See the section below. |
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

## Task E — 29 Oct 2026 opt-in call

**Call: stay opted in. No action needed. Opting in is the default; the opt-out deadline is 1 Nov.**

George's rule (Q4): stay in if the 29 Oct export is clean in the UK, otherwise opt out by 1 Nov.

| | 16 Oct | 18 Oct 20:24 (store locked) | 29 Oct |
|---|---|---|---|
| Total offers | 18.6K | 17.5K | 17.5K |
| Approved | 17.7K | — | 12.3K |
| Limited | 739 | — | 700 |
| Not approved | 77 | 17.4K not showing | 4.4K |
| GB offers with a product link | 244 / 244 | 0 / 306 | **306 / 306** |
| UK disapprovals | Cream Cap (1 variant) | everything | **1 variant: MotionTec Socks White/Red 12pc, "Mismatched product price"** |

The UK evidence ([check-2026-10-29.md](check-2026-10-29.md)):
- All 306 GB offers have a link, "unisex" / "adult", colour and description.
- No GB offer has "Missing product page", "Invalid checkout URL" or "Generic landing page".
- The only UK issue is one sock pack's price.
- The password lock is gone: Shopify is sending links again.
- The business-name issue has cleared. "No Google Ads account linked" is the only account issue left, and it's expected.

Where the 4.4K "not approved" sit, all outside the UK:
- In each of the 56 international feed labels, 76 variants (the sets, the Pink and Black hoodies, the socks, the shorts, the Puffa and the crewneck) are sent with **no link**. Total: 4,256 offers.
- That's the international Markets setup, not the UK feed. It's for `cowork/international-markets-pricing` to look at.

Open items that don't change the call:
- The 10 `CROOKSRELEASESEPT` duplicates are still live. Archiving them waits on George's yes typed in this chat.
- Tee handling time is still 0 days. The supplemental source waits on the same yes.
- **UK shipping in the feed changed.** Tracked 48 now goes out at £0.00 on every order, and Tracked 24 is £4.99, free from £50. The shipping policy page still says "standard £3, free over £30; Tracked 24 £4.99, free over £80". If the free shipping is a deliberate offer, update the policy page to match; if not, the Shopify shipping rates need putting back. That's Shopify's side, not Merchant Center's.
- Auto-add on 2 Nov will add "30 more products from crooksldn.com". They can't be inspected beforehand (FINDINGS 7). Accepted under George's rule; check what arrived on 3 Nov.

## Opt-in reading as of 18 Oct (superseded by the 29 Oct call above)

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

| Time | Change | Before | After | George's yes |
|---|---|---|---|---|
| 18 Oct 20:12 BST | Business name | CROOKSLDN (rejected; seller shown as crooksldn.com) | Crooks LDN | Q2, ANSWERS.md; "answered" in chat 20:08 |

The archive of the 10 duplicates and the tee supplemental are approved, but this session's permission check refused them. They're waiting on George's yes typed in this chat. See CHANGES.md.

## Next check

Tue 3 Nov 2026: list what auto-add brought in on 2 Nov, check for duplicates of Shopify items, and confirm UK disapprovals are still at or near zero.
