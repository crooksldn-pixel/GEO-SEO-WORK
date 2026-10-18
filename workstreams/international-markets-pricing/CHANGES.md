# Changes

Every change below is on the live store, made after George's approval in this workstream's chat on 18 Oct 2026, and read back after the write. Suggested IDs for the central change log: IMP-1 to IMP-8 (this branch doesn't write to `project-files`).

### IMP-1 · "all world" made rest-of-world only · 18 Oct 2026, 18:10–18:31 BST

- **Why:** overlapping markets at the same level resolve to the lowest price, so a fixed $85 could be undercut by "all world", which also contained the US.
- **Baseline:** "all world" (`110937997655`) held 230+ regions including GB, GG, JE, US, CA, AU, NZ and all 27 EU states.
- **Change:** removed those 34 countries.
- **Validation:** BLACK CONVICT SWEATS (XS, £60) unchanged: US $82, CA C$116, DE €72.95, PL 318 zł, JP ¥12,900, AU A$118, GG £60, GB £60.
- **Revert:** add the 34 back.

### IMP-2 · Single-country United States market · 18 Oct 2026, 18:10–18:31 BST

- **Change:** created "United States" (`116162724183`, base USD, local currencies on, rounding on). Removed US from `109860651351` and renamed that "Canada" (handle left as `united-states-and-canada`).
- **Validation:** US $82, Canada C$116 (unchanged).
- **Revert:** US back into `109860651351`, rename, delete `116162724183`.

### IMP-3 · US catalog and USD price list, DRAFT · 18 Oct 2026, 18:10–18:31 BST

- Catalog `MarketCatalog/200097071447` "United States — USD fixed prices" (DRAFT, United States); publication `340798931287` (all products, auto-publish); price list `PriceList/31662080343` (USD, 0%).
- No customer effect while DRAFT. Price load refused by the permission check (18:3x and again ~19:00 BST after George's "go").

### IMP-4 · Channel Islands free Tracked 48 from £30 · 18 Oct 2026, 18:37 BST

- **Approval:** George "SURE" (Q6).
- **Change:** Tracked 48 £3.99 (`1249190347095`) now £0–£29.99; new Tracked 48 £0 from £30 (`1424792158551`). Tracked 24 £7 unchanged.
- **Validation:** read-back; order calculator: GG £6 basket → £3.99, £60 basket → £0.
- **Revert:** delete `1424792158551`; remove the ≤ £29.99 condition.

### IMP-5 · Eurozone market split · 18 Oct 2026, ~19:05 BST

- **Approval:** George "sure do that" (Q12 A).
- **Change:** new market "Eurozone" (`116163477847`, handle `eurozone`, base EUR, local currencies on, rounding on): AT, BE, BG, HR, CY, DE, EE, FI, FR, GR, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES + MC, AD, SM, VA, ME, XK. Removed the 21 euro states from "European Union" (`109860684119`), renamed it "European Union (non-euro)" (now CZ, DK, HU, PL, RO, SE). Removed MC, AD, SM, VA, ME, XK from "all world".
- **Validation:** £60 sweats unchanged: €72.95 in DE, FR, IT, IE, BG, MC, ME, XK; 318 zł PL; 543 kr DK; 809 kr SE; US $82; JP ¥12,900.
- **Revert:** move the 21 back to `109860684119` and rename; the 6 back to "all world"; delete `116163477847`.

### IMP-6 · Eurozone catalog and EUR price list, DRAFT · 18 Oct 2026, ~19:07 BST

- Catalog `MarketCatalog/200099299671` "Eurozone — EUR fixed prices" (DRAFT, Eurozone); publication `340802044247` (all products, auto-publish); price list `PriceList/31662113111` (EUR, 0%).
- No customer effect while DRAFT. Price load not attempted (same permission block as the USD one).

### IMP-7 · International shipping zones on real costs · 18 Oct 2026, ~19:15 BST

- **Approval:** George "yes thats fine for now" (Q13 A).
- **Baseline:** zone "EU (European Union)" (`684278907223`, 50 countries) £12.99 flat; zone "International" (`684278939991`, 164 countries) £18.99 flat.
- **Change:** deleted both and created, in one write:
  - **United States** (`725565833559`): $25 up to $99.99, $30 from $100 (rates and thresholds in USD).
  - **Eurozone** (`725565931863`, same 27 countries as the market): €15 up to €89.99, €18 from €90 (in EUR).
  - **Australia and New Zealand** (`725565899095`): £20.99 up to £74.99, £26.99 from £75.
  - **Rest of world** (`725565964631`, the other 161 countries of the old International zone): £22.99 up to £74.99, £30.99 from £75.
  - **Rest of Europe** (`725565866327`, the other 23 countries of the old EU zone incl. NO, CH, IM, GI, PL, DK, SE): £12.99 flat.
  - Same set of shippable countries as before; UK and Channel Islands zones untouched; method name stays "Standard international".
- **Validation:** read-back of every zone; Shopify's order calculator (calculation only, nothing saved) — see [tests](artifacts/tests/2026-10-18-tier1.md).
- **Revert:** recreate "EU (European Union)" (£12.99) and "International" (£18.99) from the country lists in FINDINGS F6/F8 and delete the five zones.

### IMP-8 · HS codes for US duty collection · 18 Oct 2026, ~19:20 BST

- **Approval:** George "Yes" to collecting US duty at checkout (Q3b A), which needs HS codes.
- **Change:** `harmonizedSystemCode` on all 176 variants of 17 products:
  - MotionTec socks, both: 6115.95 (cotton hosiery; product copy says "cotton blend")
  - OG Jeans, Blue Wash Yard Jeans, both Yard Jorts: 6203.42 (cotton denim trousers/shorts)
  - Charcoal Cellblock Shorts, Pink CRSDR Joggers: 6103.42 (knitted cotton trousers/shorts)
  - Cellblock, Grey, Pink, Black Sets: 6103.22 (knitted cotton ensembles — matching top and bottom, same fabric, sold as one)
  - Major League caps, all three: 6505.00
  - Double-Agent Puffa: 6201.40; HydroCuff: 620193 → 6201.40 (HS 2022 code for man-made-fibre anoraks/windcheaters)
  - Origin CN added on the Blue and Brown caps (owner fact: everything is made in China).
- **Assumptions to confirm:** Puffa shell and fill are synthetic; socks are majority cotton by weight.
- **Not changed:** the 21 tees (HS 6109.10 and origin go on together once the Gildan label country is known); the 8 products that already had codes; weights.
- **Validation:** userErrors empty on all 17 writes.
- **Revert:** clear `harmonizedSystemCode` on those variants (HydroCuff back to 620193).

## Not changed

- No GBP or product price; no tax setting; duty collection not switched on (needs George's "Agree and activate").
- Draft duplicate "United Kingdom" market left in place.

## Read-only actions

- Shopify Admin API reads and ShopifyQL analytics; storefront fetches from a US IP; Parcel2Go quotes and the CROOKS Operations shipping screen (nothing booked); read-only clone of the CLIVE repo to find where Channel Islands parcels get routed; `draftOrderCalculate` shipping checks (calculation only, no draft order saved).
