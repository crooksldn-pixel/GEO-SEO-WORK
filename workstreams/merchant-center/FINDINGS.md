# Findings

Evidence is from Merchant Center 5860086407, read in George's signed-in Chrome on 16 Oct 2026 (19:00–19:40 BST) and 18 Oct 2026 (16:30–17:00 BST), unless stated otherwise. The numbers come from the two downloads summarised in [artifacts/baseline-2026-10-16.md](artifacts/baseline-2026-10-16.md).

## Finding 1 — Ten hand-added duplicates sit beside the Shopify feed

**Finding:**
Merchant Center has a second primary source. It shows as "Merchant Center · Feed label: CROOKSRELEASESEPT · Added in Merchant Center · 10 products · Countries: Automatic".

Its 10 products duplicate Shopify products and point at the same URLs:
- Black, Grey and Pink Convict Hoodie
- Black, Grey and Pink Convict Sweats
- Charcoal Cellblock Crewneck and Shorts
- Blue Wash Yard Jeans and Jorts

They differ from the Shopify versions:
- Titles are all caps, with no size.
- IDs are `G-65230983` to `G-65230992`.
- Brand, colour, Google category, GTIN and size are all blank.
- They're priced in GBP but sent to 33 countries.

They're ELIGIBLE_LIMITED. No issue is listed for the UK, so they can show there next to the Shopify versions. Everywhere else they're disapproved:
- "Mismatched currency in shipping information" in 29 countries
- "Unsupported currency" in South Korea
- "Missing shipping info" in Bulgaria, Croatia, Liechtenstein and Malta

**Evidence:**
- Settings > Data sources, first row of 77.
- Products export 16 Oct: the 10 rows with feed label `CROOKSRELEASESEPT`.
- Issues export 18 Oct: 690 issue rows on these 10 IDs.

**Why it matters:**
Commercial: duplicate listings for the same URL compete with the complete Shopify listings, and the duplicates carry no brand or size. GEO: Shopping and AI shopping surfaces can pick up the unbranded all-caps version. They're also the only source of the currency issues in the account.

**Confidence:**
High on the data. Not known who added them or why (the label suggests the September release).

**Recommended action:**
Ask George whether they're a leftover. If yes, delete the 10 products, not the Shopify sources. The brief says no deletes without George, so this waits for his explicit yes.

## Finding 2 — The invalid-GTIN fix in the brief can't be done as written, and no GTIN issue is live

**Finding:**
1. Shopify's sources are "Shopify App API" sources of type Merchant API. Each one's detail page has only a "Data source setup" tab, with no Attribute rules. There are also 76 of them, one per feed label, not one "Shopify (Content API)" source.
2. Merchant Center lists no GTIN issue at all. On 18 Oct the issues export holds only 4 issue types: missing shipping info, missing image, mismatched currency and unsupported currency.
3. Only **8 variants** send a GTIN. That's 608 offers across 76 labels. They're the L and XS sizes of Blue and Grey Wash Yard Jeans and Jorts, and they share 2 codes between them:
   - `78445655` on every L
   - `78347351` on every XS
   
   Both fail the GS1 check digit. Every other variant sends no GTIN and no `identifier_exists`.
4. The brief's figure of "112 invalid codes" doesn't appear anywhere in the current data.

**Evidence:**
- Data source detail page: Source ID 10750420649, the CHF label.
- Products export 16 Oct: `gtin` and `identifier exists` columns. The check-digit test is in `gmc_summary.py`.
- Issues export 18 Oct.

**Why it matters:**
There's nothing to fix today. If Google starts flagging the two codes, the fix can't be an attribute rule. It would need a supplemental source, or a change on the Shopify side, which product-data owns and the brief forbids for barcodes.

**Confidence:**
High on the UI and the data. Medium on why only 8 variants send a barcode. The product-data brief says 5 bag codes are shared across 5 denim products by size, so Shopify may hold more barcodes than the channel sends.

**Recommended action:**
Don't build a GTIN workaround now. Re-check on 29 Oct. If an invalid-GTIN issue appears, test a supplemental source that blanks `gtin` and sets `identifier_exists` to "no" for those variants, and show George before saving.

## Finding 3 — UK shipping matches £3 and free from £30, but handling is 0 days everywhere

**Finding:**
In Merchant Center (Shipping and returns), the UK has 4 policies, all created by Shopify:

| Policy | Cost | Applies | Delivery shown |
|---|---|---|---|
| `flat_3.00_GBP_…_tracked 48` | £3.00 | all orders | 2–3 business days (handling 0–0, transit 2–3, cut-off 12:00 AM, Mon–Fri) |
| `price_based_GBP_…` | £0.00 | orders ≥ £30 | 2–4 business days |
| `price_based_GBP_…2` | £0.00 | orders ≥ £80 | 2–4 business days |
| `flat_4.99_GBP_…_tracked 24` | £4.99 | all orders | 1–2 business days |

Shopify also sends item-level shipping on every GB offer, and that overrides these policies:
- Tracked 48: £3.00, free from £30, handling 0, transit 2–3
- Tracked 24: £4.99, free from £80, handling 0, transit 1–2

Prices and thresholds match the brief, the shipping policy page and the live checkout (`cowork/live-site-checks` Finding 3). There are three mismatches:
1. Handling is 0 days on every offer, tees included. The tees are print on demand, and the tee page says "Order before 18:00 and it ships today".
2. The two free tiers say 2–4 days. Checkout says 2–3 for Tracked 48 and 1–2 for Tracked 24.
3. The cut-off is 12:00 AM, Mon–Fri. The site says 18:00, Mon–Sat.

**Evidence:**
- Each UK policy row expanded on 18 Oct; the £3 policy's delivery step was opened and closed without saving.
- `shipping(...)` column in the 16 Oct export.
- WebFetch of `/policies/shipping-policy` and `/products/crx-garms-t-shirt`, 16 Oct.

**Why it matters:**
Merchant listings and Shopping show delivery estimates, and the tee estimate is wrong by however long printing takes. Policies created by Shopify and item-level shipping are likely to be regenerated by the Shopify app, so editing them in Merchant Center may not stick.

**Confidence:**
High on the values. Medium on whether edits made in Merchant Center would survive the next Shopify sync.

**Recommended action:**
Task D: get the tee print-on-demand time from George, then find a route that only touches the tees. A supplemental source carrying `min_handling_time`, `max_handling_time` and `shipping_label` is the candidate; whether it can link to Merchant API sources still needs checking. Fix the 2–4 day free tiers and the cut-off at the source, in Shopify shipping settings, which no workstream currently owns.

## Finding 4 — Merchant Center rejects the business name "CROOKSLDN"

**Finding:**
Setup and policy issues show "Invalid business name. Provided name: CROOKSLDN. Used name: crooksldn.com." Google shows the domain instead of the brand as the seller name. The other account-level item is "No Google Ads account linked". That's expected, because the brief allows no paid campaigns.

**Evidence:**
Products > Needs attention > View setup and policy issues (2), 18 Oct.

**Why it matters:**
GEO and brand: the seller name on Shopping and free listings reads "crooksldn.com", not a brand name. George's confirmed alternates are "Crooks LDN" and "Crooks London".

**Confidence:**
High that the issue exists. Medium that "Crooks LDN" will pass. Google's exact objection isn't stated, and all caps is the likely cause.

**Recommended action:**
On George's yes, set Business info > business name to "Crooks LDN". Re-check the issue after 3–5 days.

## Finding 5 — The remaining limits are in markets CROOKSLDN barely sells to

**Finding:**
- **Liechtenstein:** "Missing shipping info" on all 244 Shopify variants. The CHF source targets Liechtenstein and Switzerland, but only Switzerland has a policy.
- **Missing shipping countries:** Merchant Center lists Bosnia & Herzegovina, Bulgaria, Croatia, Lebanon, Liechtenstein, Malta, Moldova, Montenegro, North Macedonia, Puerto Rico and Serbia.
- **South Korea:** "Missing Korean business registration number" on 254 offers.

**Evidence:**
Issues export 18 Oct; Shipping and returns > Next steps; the Needs attention summary.

**Why it matters:**
Little commercial effect. It inflates the "Limited" count that Google's emails quote. These markets come from Shopify Markets, so a fix belongs in Shopify Markets, not in Merchant Center.

**Confidence:**
High.

**Recommended action:**
Leave it unless George sells to these countries. Note it so the 29 Oct comparison doesn't read these as core-feed problems.

## Finding 6 — Feed titles carry "cotton" on the tees, and two titles are all caps

**Finding:**
Shopify feed titles (GB):
- "Crooks Express Tee — Cotton Logo T-Shirt | CROOKSLDN"
- "CRX Garms T-Shirt — Premium Cotton Tee | CROOKSLDN"
- "CRXSTARZ T-Shirt — CROOKS Logo Cotton Tee | CROOKSLDN"

The cotton claim is confirmed only for hoodies and joggers. "CHARCOAL CELLBLOCK CREWNECK" and "MAJOR LEAGUE CROOKS CAP (CREAM)" are all caps. The Puffa title has no "| CROOKSLDN". All four sets already send `is_bundle = yes`.

**Evidence:**
`title` and `is bundle` columns in the 16 Oct export.

**Why it matters:**
Feed titles are what Shopping and AI shopping answers quote. Titles can't be edited in Merchant Center, because Merchant API sources have no attribute rules, so every title change has to come from Shopify.

**Confidence:**
High.

**Recommended action:**
The feed title is the Shopify SEO title, plus the variant. The three tee titles above match the "before" SEO titles in `cowork/product-data` C2–C4 exactly, so those planned edits will change the Shopping titles too. The crewneck and the cap appear to have no SEO title, so the all-caps product title is used. The title proposals in `artifacts/04-merchant-center.md` (task F) are therefore SEO-title proposals for product-data to apply.

## Finding 7 — Auto-add skips products already in a data source, but would pick up anything taken off the Google channel

**Finding:**
Merchant Center says Google found 30 more products on crooksldn.com, which it will add on 2 Nov. It doesn't list them unless you click "Add all products found". Google's help page says products already in another data source aren't auto-added. So anything removed from the Shopify Google channel, such as the Cream Cap under product-data item A, becomes a candidate for auto-add from the crawl. It would then be disapproved again for having no image.

**Evidence:**
- Data sources > Found by Google, 18 Oct.
- [Add products automatically from your online store](https://support.google.com/merchants/answer/12158480).

**Why it matters:**
It's the main argument for opting out even when the feed is clean: staying in takes away control over which products show.

**Confidence:**
Medium. The 30 products couldn't be identified without adding them. The cap outcome is inferred from Google's stated rule.

**Recommended action:**
Raise it with George now, and decide on 29 Oct with the fresh export.
