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

## Finding 8 — Since about 20:05 BST on 18 Oct, the password lock has stripped product links from the whole feed

**Finding:**
The Online Store is password-protected. Recorded by `cowork/theme-editor` (Admin API `passwordProtection.enabled = true`, 20:14 BST) and by `cowork/search-console` and `cowork/live-site-checks`, where every public URL ends at `/password`.

Merchant Center's next Shopify sync (data stamped 12:05 PM account time, which is 20:05 BST) arrived without links. The products export at 20:22 BST shows:
- only **47 of 17,452 offers** carry a `link`
- **0 of 306** GB offers carry one

"Not showing on Google" went from 76 to 6.11K at 20:05, 7.04K at 20:19 and **17.4K** at 20:24. The issues export at 20:13 had already disapproved, in the UK, all 90 tee variants, the Puffa, the HydroCuff and all 3 caps for "Missing product page", plus "Invalid checkout URL" on the tees. The rest followed as the sync was processed.

Product pages load normally in George's browser, but only because he's logged in as the store owner.

**Evidence:**
- Products export `products_2026-10-18_12-22-35` (`link` column).
- Issues export `product_issues_2026-10-18_12-13-25`, 49,638 rows:
  - Missing product page: 43,698
  - Invalid checkout URL: 2,466
  - Generic landing page: 336
- Products page counters read at 20:05, 20:19 and 20:24.
- Other workstreams' records of the lock.

**Why it matters:**
While the lock is on, CROOKSLDN has effectively no Shopping or free listings. If it's still on at the 29 Oct check, the feed isn't clean in the UK, and George's Q4 rule means opting out by 1 Nov.

**Confidence:**
High on the effect. High that the lock is the cause: timing matches, it hit every product at once, and pages and data are otherwise unchanged. Not known whether the lock is deliberate (T-shirt Week is presumed to run 19–25 Oct).

**Recommended action:**
George decides when the lock comes off. Nothing to change in Merchant Center: links come back on the next Shopify sync after the store reopens. Re-export within 24 hours of reopening and confirm links on every GB offer.

## Finding 9 — The feed changed on 18 Oct: gender, age group and colour landed; tees are now 30 variants at £20; three caps are live

**Finding:**
Comparing the 18 Oct 20:22 export with 16 Oct:
- **GB offers:** 244 → 306.
- **Gender and age group:** "unisex" / "adult" on 303 of 306. One Puffa variant is blank.
- **Puffa colour:** Black.
- **Tees:** each of the 3 tees has 30 variants (Black, Charcoal, Green, Light Grey, Navy, White × XS–XL) at £20.00, up from 10 variants at £25.
- **Caps:** Major League Crooks Cap in Cream, Brown and Blue are all in the feed, with images and descriptions. Brown and Blue have no colour.
- **Feed labels:** 77 → 58, with a new `EUR_116163477847` label. Shopify Markets were reorganised.
- **Hand-added duplicates:** the 10 `CROOKSRELEASESEPT` products are unchanged.
- **GTIN:** the same 8 variants.

**Evidence:**
`gmc_summary.py` on both exports; `artifacts/findings-map-03.md`.

**Why it matters:**
The tee handling-time file must use the current variant IDs; the 16 Oct ones are out of date. The 14 T-shirt Week tees aren't in the feed yet. When they're published to the Google channel, they need adding to that file. Brown and Blue cap colour is a gap for product-data.

**Confidence:**
High.

**Recommended action:**
- Use `artifacts/gmc-supplemental-tee-handling-GB.tsv`, built from the 20:22 export: 90 GB tee variants, handling 2–3 days, transit per owner decision #3, label `print-on-demand`.
- Re-build it when new tees join the feed.
- Pass the cap-colour gap to product-data.

## Finding 10 — 29 Oct: the UK feed is clean again; the gaps are international links and UK shipping parity

**Finding:**
- **The password lock is gone.** All 306 GB offers carry a link again, and each has "unisex" / "adult", a colour and a description.
- **UK disapprovals:** one variant. The White/Red 12-pack of MotionTec Socks has "Mismatched product price".
- **"Invalid business name" has cleared.** "No Google Ads account linked" is the only account issue left.
- **International labels:** across all 56, the same 76 variants have no link, giving 4,256 "Missing product page" offers. These are:
  - the 4 sets
  - the Pink and Black Convict hoodies
  - the MotionTec socks
  - the Cellblock shorts and crewneck
  - the Puffa
  
  This drives the 4.4K "not approved".
- **UK shipping in the feed has changed** since 16 Oct:
  - Tracked 48 is £0.00 on every order.
  - Tracked 24 is £4.99, free from £50.
  - The live shipping policy page still says standard £3 with free UK shipping over £30, and Tracked 24 free over £80.
- **Unchanged:**
  - the 10 `CROOKSRELEASESEPT` duplicates are still live
  - tee handling is still 0 days
  - the "30 more products" auto-add banner still says 2 Nov
  - GTIN is still 8 variants

**Evidence:**
- [artifacts/check-2026-10-29.md](artifacts/check-2026-10-29.md).
- Overview counters on 29 Oct: approved 12.3K, limited 700, not approved 4.4K.
- The setup and policy issues page.
- `/policies/shipping-policy`, read 29 Oct 09:06 GMT.

**Why it matters:**
George's Q4 rule is met, so he stays opted in. A Shopping shipping price that differs from the policy page can draw a "Mismatched shipping" warning, and it confuses customers. The international link gap removes those products from Shopping outside the UK.

**Confidence:**
High on the data. Not known whether the free Tracked 48 is a deliberate offer, or why international markets drop links for those 76 variants. One possible cause is a Markets product-availability setting.

**Recommended action:**
- **George:** confirm the UK shipping offer. If it's deliberate, update the policy page; if not, restore the Shopify rates.
- **`cowork/international-markets-pricing`:** check why those 76 variants have no URL in international Markets.
- **This workstream:** check what auto-add brought in, on 3 Nov.
