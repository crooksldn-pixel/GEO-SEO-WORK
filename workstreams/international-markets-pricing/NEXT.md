# Next

## Waiting on George's "go" (in this order)

1. **USD prices.** Load 44 products by product (USD column of the approved list) and the 8 sock packs by variant, set the US catalog ACTIVE, then test (see the script below). Sock packs, both colours: 1pc $9, 3pc $22, 6pc $35, 12pc $65 (EUR: €8, €20, €30, €55). Manual route: Markets → Catalogs → Import → [artifacts/catalog-prices-USD.csv](artifacts/catalog-prices-USD.csv), then set the sock packs in the catalog by hand.
2. **Eurozone (Q12, option A).** New market "Eurozone": the 21 euro states plus MC, AD, SM, VA, ME, XK; base EUR. Take the 21 out of "European Union" and rename it "European Union (non-euro)". Add a EUR catalog "Eurozone — EUR fixed prices" with [artifacts/catalog-prices-EUR.csv](artifacts/catalog-prices-EUR.csv) + sock packs. Test DE, IT, FR, IE, BG.
3. **Shipping zones (Q13).** Split "International" into United States (fixed USD), Australia/New Zealand and rest of world; split "EU (European Union)" into Eurozone (fixed EUR) and Rest of Europe; value-band rates per Q13; move the Isle of Man to the Channel Islands zone.
4. **US duties (Q3b).** Only after every product has an HS code.

## Other workstreams

- **Theme:** Horizon country/region selector in header and footer. Without it, local prices only show at checkout.
- **Product-data:** weights on 31 products, HS codes on 37, origin CN on the Blue and Brown caps, HydroCuff HS to 6201.40, tee origin once the blank is known (F5).
- **Ops / CROOKS Shipping:** Channel Islands parcels must route Royal Mail Tracked 48, not Parcelforce (F10).
- **Accountant:** the three VAT points in F9.

## Tier 1 test script (after each go-live)

1. contextualPricing for every price point in US / DE / IT / FR / GG; must match the list exactly.
2. With the selector (once live): homepage, collection, product page, cart, checkout for US, DE, IT and GG. Pass = same currency and price at every step; shipping matches the matrix; no tax line in US/EU; US duty line present and plausible once enabled.
3. One checkout to the payment step per Tier 1 market with a real address — George, or with his OK.
4. Screenshots into `artifacts/tests/`.

## Measurement

Baseline is F1 (checkout completion by country, 18 Oct 2026). Re-pull at 30 and 60 days after the US and Eurozone prices go live. Nothing is recorded as an improvement without that re-pull.

## Ongoing

Fixed prices don't move with FX. Re-check quarterly, or sooner if GBP/USD or GBP/EUR moves more than ~5% from 1.334 / 1.186.
