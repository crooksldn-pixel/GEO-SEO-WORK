# Changes

Every change below is on the live store, made after George's approval in this workstream's chat on 18 Oct 2026 ("APPROVE" to the tiers and USD/EUR lists; "SURE" to Channel Islands free Tracked 48). Each was read back. Suggested IDs for the central change log: IMP-1 to IMP-4 (this branch doesn't write to `project-files`).

### IMP-1 · "all world" made rest-of-world only · 18 Oct 2026, 18:10–18:31 BST

- **Why:** markets at the same level that overlap resolve to the lowest price, so a fixed $85 in a US catalog could be undercut by "all world", which also contained the US. Prerequisite for every fixed-price catalog.
- **Baseline:** Market `110937997655` "all world" held 230+ regions including GB, GG, JE, US, CA, AU, NZ and all 27 EU states.
- **Change:** removed those 34 countries. Each still sits in its own market (UK, Channel Island, United States, Canada, Australia and New Zealand, European Union).
- **Validation:** read-back shows none of the 34 in "all world"; JP, ID, NO, CH, IM, GI and the rest remain. contextualPricing on BLACK CONVICT SWEATS (XS, £60) unchanged: US $82, CA C$116, DE €72.95, PL 318 zł, JP ¥12,900, AU A$118, GG £60, GB £60.
- **Revert:** add the 34 countries back to "all world".

### IMP-2 · Single-country United States market · 18 Oct 2026, 18:10–18:31 BST

- **Baseline:** US shared "United States and Canada" (`109860651351`, base GBP, local currencies on).
- **Change:** created "United States" (`116162724183`, handle `united-states`, ACTIVE, region US, base currency USD, local currencies on, rounding on). Removed US from `109860651351` and renamed it "Canada" (handle left as `united-states-and-canada`).
- **Validation:** US still $82 (automatic conversion; no active catalog), Canada C$116.
- **Revert:** add US back to `109860651351`, rename it, delete `116162724183`.

### IMP-3 · US catalog and USD price list, DRAFT · 18 Oct 2026, 18:10–18:31 BST

- **Change:** catalog `MarketCatalog/200097071447` "United States — USD fixed prices", status DRAFT, assigned to United States; publication `Publication/340798931287` (all products, auto-publish); price list `PriceList/31662080343`, USD, 0% adjustment.
- **Validation:** read-back: DRAFT, 0 fixed prices. US price unchanged ($82).
- **Next step (not done):** load the fixed prices, then set the catalog ACTIVE. The price write was refused by this session's permission check; waiting on George (STATUS blocker 1).

### IMP-4 · Channel Islands free Tracked 48 from £30 · 18 Oct 2026, 18:37 BST

- **Approval:** George, "SURE" (Q6).
- **Baseline:** Channel Islands zone: Tracked 48 £3.99 at any order value; Tracked 24 £7.00; no free threshold.
- **Change:** existing Tracked 48 £3.99 (method `1249190347095`) now applies £0–£29.99 only; new method "Tracked 48" (description "Free over £30", `1424792158551`) at £0 from £30. Tracked 24 untouched.
- **Validation:** delivery-profile read-back shows both Tracked 48 rates with those conditions. Not tested through a live checkout (no address typed into the live checkout).
- **Risk:** profitable only while CI parcels go Royal Mail Tracked 48 (F10, Q14).
- **Revert:** delete method `1424792158551`; remove the ≤ £29.99 condition from `1249190347095`.

## Not changed

- No GBP or product price, tax setting, duty setting or international shipping rate.
- The draft duplicate "United Kingdom" market is still there (deleting can't be undone and it's harmless as a draft).

## Read-only actions

- Branch created from `main`.
- Shopify Admin API reads: shop info, Markets, delivery profiles, products and contextual prices, orders, abandoned checkouts.
- ShopifyQL analytics queries: sales by country (12 months, 90 days, lifetime); sessions and funnel by country.
- Storefront page fetches from a US IP. No cart created, no checkout fields filled.
- Parcel2Go quotes in George's account and the CROOKS Operations shipping screen (no labels bought, nothing booked).
