# Next

## On George's go (no price impact — can go first)

1. Theme workstream: turn on Horizon's country/region selector in header and footer. Optional: a geolocation popup app (e.g. Selecty, free plan) to suggest the right country on arrival, because the Grow plan has no automatic detection.
2. Delete the draft duplicate "United Kingdom" market.
3. Take GB, GG, JE, US, CA, AU, NZ and the EU states out of "all world" so it's genuinely rest of world. Must happen before any fixed-price catalog: overlapping catalogs that aren't nested resolve to the lower price.
4. Product-data workstream: HS codes on the 17 products without one, origin CN on China-made products, weights on the 11 at 0g, HydroCuff HS to 6201.40.

## On approval of the price architecture (Q1, Q2)

5. Create a single-country "United States" market; take US out of "United States and Canada" and rename it "Canada".
6. Build the USD catalog (fixed prices, CSV import) and assign it to United States.
7. Build the EUR catalog and assign it to European Union. Optional: move MC, AD, SM, VA, ME, XK into it.
8. Preview each market with Products → View as, then check the storefront with the selector.

## On approval of shipping and duties (Q3, Q5–Q7)

9. Split zones: United States (fixed USD), Eurozone (fixed EUR), Rest of Europe, World Zone 1, World Zone 2; move Isle of Man next to the Channel Islands.
10. Channel Islands free Tracked 48 from £30, if approved.
11. US duties: enable collection for the US only, line item; ship US on Royal Mail PDDP; compare the first 3 Royal Mail duty invoices with what Shopify collected.

## Tier 1 test script (after go-live)

For US, Eurozone (DE, IT) and Channel Islands, using the selector: homepage, collection, product page, cart, checkout. Pass = same currency and same price at every step; shipping matches the matrix; tax line absent (US, EU) or correct; US duty line present and plausible. Screenshot each step into `artifacts/tests/`.

## Measurement

Baseline is F1 (checkout completion by country, 18 Oct 2026). Re-pull at 30 and 60 days after go-live. Nothing is recorded as an improvement without that re-pull.

## Ongoing

Fixed prices don't move with FX. Re-check quarterly, or sooner if GBP/USD or GBP/EUR moves more than ~5% from 1.334 / 1.186.
