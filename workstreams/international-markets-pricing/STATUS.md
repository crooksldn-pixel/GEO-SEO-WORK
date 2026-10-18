# Workstream: International markets & local pricing

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).

**Branch:** cowork/international-markets-pricing  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 18:10 BST  
**Priority:** P2  
**Overall status:** PROPOSAL READY — WAITING ON GEORGE

## Objective

Make international customers see deliberate local prices and clean shipping in a currency they recognise, from the first page to checkout, without giving away margin. Nothing in Shopify changes until George approves the architecture.

## Current state

Audit and proposal done. Nothing has been changed in Shopify.

The headline problem isn't the rounding. The storefront has no country/currency selector and the Grow plan has no automatic market detection, so every international visitor browses in £ and only meets their own currency at checkout — where shipping (and for the US, duties later) appear on top. International checkout completion is 10–14% against 51% in the UK.

Overseas sales are small (14 orders, £877, 1.5% of net sales in 12 months). The US and the Eurozone have the traffic and checkout intent to justify fixed local prices; everything else stays automatic.

## Completed

- **Analysed:** sales, sessions and checkout funnel by country (12 months = store lifetime, 90 days), orders and abandoned checkouts with an international address. See FINDINGS F1.
- **Audited:** every Market (countries, currency, local currencies, rounding, catalogs, adjustments, duties/tax inclusion, web presence). FINDINGS F2.
- **Audited:** shipping profile, zones and rates; compared with Royal Mail's published October 2026 online prices. FINDINGS F6.
- **Audited:** HS codes, country of origin and weights on all 25 live products. FINDINGS F5.
- **Tested:** storefront from a US IP (collection, product page, product JSON, `?country=` and `?currency=` parameters). FINDINGS F4.
- **Researched:** Shopify conversion fee, rounding, catalogs, duty collection; US tariff stack on China-origin goods (Oct 2026); EU €3 duty (from 1 Jul 2026); Royal Mail US PDDP.
- **Built:** tiering, USD and EUR price ladders with net-vs-UK check, shipping matrix with margin/subsidy, Shopify change list, ROI scenarios. [artifacts/PROPOSAL.md](artifacts/PROPOSAL.md), [artifacts/price-matrix.md](artifacts/price-matrix.md).
- **Live:** nothing.

## Currently working on

Nothing running.

## Blockers

### Blocker 1 — Every price, shipping and duty change needs George's yes

**Blocking:** all implementation  
**Needs:** answers to Q1–Q3 and Q5–Q8 in QUESTIONS.md  
**From:** George  
**Severity:** P2  
**Can work around it?:** Partly  
**Workaround:** the four no-price-impact items (selector, draft market, market overlap, product data) can go first once George says go.

### Blocker 2 — Real carrier costs and how US orders ship

**Blocking:** final shipping rates; the US duty decision  
**Needs:** Q4 — carrier and label cost for recent international parcels; whether Royal Mail has invoiced US duties  
**From:** George  
**Severity:** P2  
**Can work around it?:** Yes  
**Workaround:** the shipping matrix uses Royal Mail's published online prices as the cost basis, labelled as such.

### Blocker 3 — No unit costs in Shopify

**Blocking:** a real margin check and any international free-shipping threshold  
**Needs:** Q7 — unit cost per product line  
**From:** George  
**Severity:** P3  
**Can work around it?:** Yes  
**Workaround:** margin is checked as net revenue against the same product's UK net revenue.

## Waiting on George

All questions, with options and answer lines, are in [QUESTIONS.md](QUESTIONS.md).

## Waiting on external systems

- Theme workstream (`cowork/theme-editor`) for the country selector.
- Product-data workstream (`cowork/product-data`) for HS codes, origin and weights.

## Next actions

See [NEXT.md](NEXT.md).

## Expected impact

**Commercial:** Medium (US/EU checkout completion; stops £2–£19 shipping losses per overseas parcel)  
**SEO:** Low  
**GEO:** Low–Medium (shopping surfaces get market-correct prices once local prices show on the storefront)  
**Confidence:** Medium — the funnel signal is clear but the samples are small; no improvement will be claimed without the 30/60-day re-pull.
