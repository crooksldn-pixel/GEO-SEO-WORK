# Next

## George

1. **Fixed prices** — import [catalog-prices-USD.csv](artifacts/catalog-prices-USD.csv) and [catalog-prices-EUR.csv](artifacts/catalog-prices-EUR.csv) (Markets → Catalogs → Import → Adjust prices → Import CSV), set the 8 sock packs by hand, set both catalogs Active. Or tell me in plain words to load and activate them and I retry once.
2. **US duty** — Settings → Taxes and duties → Duties and import taxes → Set up: United States only, add at checkout (not included in price), postal duty rates, confirm DDP (Royal Mail US is duty pre-paid), Agree and activate.
3. **Tee label** — the "Made in" country on one Gildan tee per style.
4. **CLIVE Shipping** — treat GG, JE, IM as domestic (Royal Mail Tracked 48), not international.

## Me, once unblocked

1. Read back both price lists; contextualPricing for every price point in US, DE, IT, FR, IE, BG; confirm PL/DK/SE unchanged.
2. Tees: HS 6109.10 + origin on all 630 tee variants.
3. After duty activation: draftOrderCalculate a US basket and check a duty line appears at ~36% of goods (China origin) / ~16.5% (tees).
4. Update FINDINGS, CHANGES, STATUS.

## Other workstreams

- **Theme:** country/region selector in header and footer.
- **Product-data:** weights on the 31 zero-weight products (needed if shipping moves to weight bands, and for Swiss duties).
- **Accountant:** the three VAT points in FINDINGS F9.

## Tier 1 test script (after prices go live)

1. contextualPricing for every price point in US / DE / IT / FR / GG; must match the lists.
2. With the selector: homepage, collection, product page, cart, checkout for US, DE, IT, GG. Pass = same currency and price at every step; shipping matches the matrix; US duty line once on.
3. One real checkout to the payment step per Tier 1 market — George, or with his OK.

## Measurement

Baseline is F1 (checkout completion by country, 18 Oct 2026). Re-pull at 30 and 60 days after fixed prices go live.

## Ongoing

Fixed prices don't move with FX. Re-check quarterly, or sooner if GBP/USD or GBP/EUR moves more than ~5% from 1.334 / 1.186. Shipping bands are "fine for now" per George; revisit once weights exist or Easyship quotes are available.
