# Workstream: International markets & local pricing

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).
>
> **18 Oct 2026, after 18:10 BST — George answered this branch's six decisions in the workstream chat** (recorded in [QUESTIONS.md](QUESTIONS.md)): tiers and USD/EUR lists APPROVED; US duties NOT SURE; use CROOKS Shipping (Easyship + Parcel2Go) for real costs; Channel Islands free Tracked 48 from £30 YES; CROOKS IS VAT-registered; print-on-demand tees are printed in-house.

**Branch:** cowork/international-markets-pricing  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 18:50 BST  
**Priority:** P2  
**Overall status:** IMPLEMENTING — PAUSED: loading the USD prices needs George's typed "go"

## Objective

Make international customers see deliberate local prices and clean shipping in a currency they recognise, from the first page to checkout, without giving away margin.

## Current state

Live now (each read back; see [CHANGES.md](CHANGES.md)):

1. **Markets restructured** so a fixed-price catalog can't be undercut by an overlapping market: "all world" is rest of world only; new single-country **United States** market (base USD); the old "United States and Canada" market is now **Canada**. No customer price moved: the £60 sweats are still $82 / €72.95 / C$116 / A$118 / ¥12,900 / £60 in Guernsey.
2. **Channel Islands Tracked 48 free from £30** (£3.99 below £30). Tracked 24 £7 unchanged.
3. **US catalog + USD price list exist as DRAFT with 0 fixed prices.** No effect until activated.

Paused: writing the approved USD prices into that price list was refused by this session's permission check as a production price change. George picks one:

- type **go** in the workstream chat: I load 44 products + 8 sock packs, activate the catalog and test; or
- import [artifacts/catalog-prices-USD.csv](artifacts/catalog-prices-USD.csv) in Markets → Catalogs → Import, then set the 8 sock packs by hand (list in NEXT.md; socks have no SKUs so the CSV can't price packs separately).

Until the country selector is on (theme workstream), US visitors still browse in £ and meet $ only at checkout. Fixed prices fix the number; the selector fixes where it shows.

## Completed

- **Analysed:** sales, sessions and checkout funnel by country (12 months = store lifetime, 90 days). FINDINGS F1.
- **Audited:** every Market (F2), shipping zones and rates (F6), HS codes, origin and weights (F5, refreshed for 45 active products).
- **Tested:** storefront from a US IP (F4).
- **Researched:** Shopify conversion fee, rounding, catalogs, duty collection; US tariffs on China-origin goods (Oct 2026); EU €3 duty; Royal Mail US duty-prepaid service.
- **Built:** tiers, USD/EUR ladders, shipping matrix, change list, ROI. [artifacts/PROPOSAL.md](artifacts/PROPOSAL.md), [artifacts/price-matrix.md](artifacts/price-matrix.md).
- **Costed:** real carrier rates from CROOKS's Parcel2Go account (F8). Easyship needs a login I can't enter, so it isn't included.
- **Checked:** VAT effect on the approved lists (F9); Channel Islands carrier routing (F10).
- **Implemented:** IMP-1 to IMP-4 (CHANGES.md). Post-change Markets table in F11.
- **Prepared:** catalog import files for USD and EUR (artifacts/).

## Blockers

### Blocker 1 — USD price load needs George's "go"

**Blocking:** US fixed prices going live  
**Needs:** George types "go" in this workstream's chat, or imports the CSV himself  
**Severity:** P2  
**Workaround:** none; nothing customer-facing is broken while it waits (US stays on automatic $82 etc.).

### Blocker 2 — Eurozone catalog: how to treat non-euro EU (Q12)

The EU market's base currency is GBP and a EUR price list needs a EUR market. Recommended: split off a "Eurozone" market so PL, DK, SE, CZ, HU, RO stay on automatic conversion as approved.

### Blocker 3 — Country selector (theme workstream)

Without it, local prices only appear at checkout.

### Blocker 4 — US duties (Q3b)

George is not sure. Royal Mail to the US via Parcel2Go is duty-prepaid by the sender, so if US orders go that way CROOKS is paying ~£23 duty on an $85 hoodie today.

### Blocker 5 — Weights and HS codes (product-data workstream)

31 of 45 active products weigh 0; 37 have no HS code. Weight-based shipping and duty collection both need them.

### Blocker 6 — Channel Islands routed to Parcelforce (Q14)

Free CI shipping only pays while CI parcels go Royal Mail Tracked 48.

### Blocker 7 — Tee blank origin (Q15)

## Next actions

See [NEXT.md](NEXT.md).

## Expected impact

**Commercial:** Medium (US/EU checkout completion; stops £1–£11 shipping losses per overseas parcel; closes a possible ~£23-per-hoodie US duty leak)  
**SEO:** Low  
**GEO:** Low–Medium (shopping surfaces get market-correct prices once local prices show on the storefront)  
**Confidence:** Medium — the funnel signal is clear but samples are small; no improvement will be claimed without the 30/60-day re-pull.
