<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 3: Google Merchant Center / feed parity

Audit date: 16 Oct 2026. Read-only: no store, theme or feed edits made. The "Crooks GEO and SEO programme" thread is the sole implementer.

## Current state

- **Merchant Center account:** ID 5860086407 (from a Google email to team@crooksldn.com, 2 Oct 2026). No Merchant Center connector exists in this project, so diagnostics, item statuses and feed rules could not be read.
- **Feed source:** the Shopify "Google & YouTube" sales channel (publication 333206487383). All 25 ACTIVE products are published to it; no draft or archived product is. That is 244 variant-level feed items, and 125 of them (51%) are the four Sets.
- **Site structured data:** the live theme "CROOKSLDN — SEO round 2" emits ProductGroup/Product JSON-LD from `snippets/crooks-schema-product.liquid`, with offer state from `crooks-schema-offer-state.liquid` and UK shipping from `crooks-schema-shipping.liquid`.
- **Shipping parity:** this one is OK. The Shopify UK rates (Tracked 48 £3, free from £30; Tracked 24 £4.99, free from £80) match the JSON-LD (£3 / free ≥ £30, GB only). I could not see the GMC shipping settings.
- **Markets:** UK is primary. EU, US/CA, AU/NZ, Channel Islands and "all world" are enabled. JSON-LD offers are emitted only when the currency is GBP.

## Access that would unlock the rest

1. The quickest route is a GMC export. In Merchant Center 5860086407, go to Products > All products (or "Needs attention") > Download, and upload the CSV to this project. That lets every finding below be confirmed against Google's own item issues.
2. A Merchant Center or Content API connector would allow ongoing monitoring. None is available in the registry today.
3. Shopify app-installation scope: the Admin token is denied `appInstallations`, so I can't confirm the Google & YouTube app's sync status or settings from here.

## Ranked findings

Fields per item: current state · evidence · affected URLs/files · opportunity · commercial impact · SEO impact · GEO impact · effort · confidence · dependencies · recommended implementation · status.

### F1. P0: Google will auto-add "more than 30" missing products on 2 Nov unless opted out by 1 Nov

- **Current state:** Google's 2 Oct email says more than 30 products from the online store aren't in Merchant Center. Google will add them automatically from the website on 2 Nov 2026, unless the account opts out by 1 Nov. It will then re-check the site every 24 hours.
- **Evidence:** Gmail thread "More than 30 of your products aren't on Google" (googlebase-noreply@google.com, 2 Oct 2026, still unread). The store's feed should contain 244 variants, so a gap of more than 30 means the Shopify channel is not getting everything into GMC.
- **Affected:** the whole Shopping catalogue.
- **Opportunity:** know which items are missing and why before Google fills the gap from crawled pages. Crawled items take their data from on-page JSON-LD, which currently lacks gender, age group and (on several products) colour. They would also sit alongside channel-fed items, which creates a duplicate and conflicting-source risk.
- **Commercial impact:** high. Items missing from GMC get no free listings or Shopping ads.
- **SEO impact:** medium (free product listings and the Shopping tab).
- **GEO impact:** medium. Google's Shopping Graph feeds AI Mode and AI Overviews product answers.
- **Effort:** low to check, which takes about 15 minutes in GMC. Fixing the sync depends on the cause.
- **Confidence:** high that the gap exists. Which items are affected is unknown: inferred candidates are the Sets (Uncategorized, no description) and items disapproved for F2–F5.
- **Dependencies:** GMC access (owner).
- **Recommended:** before 1 Nov, the owner opens GMC and lists the missing items and their reasons. Default plan: fix the Shopify-channel causes (F2–F6) so one source owns the catalogue, and let auto-add proceed only if the gap is items the channel genuinely can't send. **Status:** needs owner, deadline 1 Nov.

### F2. P1: Every barcode sent to Google is an invalid GTIN, and five are shared across five different products

- **Current state:** 112 of 119 barcodes on active variants are 8-digit internal labels. All 112 fail the GS1 check digit. Codes 78347351, 78380119, 78412887, 78445655 and 78478423 are reused on og-jeans, grey-wash-yard-jeans, blue-wash-yard-jeans, blue-wash-yard-jorts and grey-wash-yard-jorts. The theme already knows this and suppresses them from JSON-LD (comment in `crooks-schema-product.liquid`, SEO audit 30 Sep). The Google & YouTube channel sends variant barcode as `gtin`, so feed and page disagree.
- **Evidence:** Admin API variant barcodes, with a check-digit test run in this audit.
- **Affected:** 19 products. Sets, the cap and the puffa have no barcode.
- **Opportunity:** stop declaring fake GTINs. GMC flags "Invalid GTIN" and limits the affected items. Duplicate GTINs across different products can merge or suppress offers.
- **Commercial impact:** high, because it touches almost the whole range. **SEO impact:** medium. **GEO impact:** low to medium (product identity in the Shopping Graph).
- **Effort:** low. **Confidence:** high on invalidity; medium on how GMC is treating them today (needs F1 export).
- **Dependencies:** barcodes may be used by POS or Click & Drop labels, so **don't clear them in Shopify**.
- **Recommended:** in GMC, add a feed rule on the Shopify data source: set `gtin` to empty and `identifier_exists` to `no` (own-brand goods without GS1 codes). This is reversible and touches no store data. The alternative is the channel's per-product "custom product" flag. **Status:** proposed, needs GMC access.

### F3. P1: No gender or age group on any product

- **Current state:** none of the 25 active products has `shopify.target-gender`, `shopify.age-group` or `mm-google-shopping.gender/age_group` set. Google requires both for apparel sold in the UK.
- **Evidence:** a metafield dump of all active products (namespaces present: crooks, global, judgeme, reviews, seo, shopify colour/fabric/fit/size etc., mc-facebook, mm-google-shopping category only).
- **Affected:** all 24 apparel products (the socks count as apparel too).
- **Opportunity:** remove a likely disapproval or limitation across the catalogue.
- **Commercial impact:** high if items are being limited. **SEO impact:** medium. **GEO impact:** low.
- **Effort:** low (bulk metafield or channel setting). **Confidence:** medium. The channel might apply a default I can't see, and the F1 export confirms it.
- **Dependencies:** **a brand fact is missing**: is the range unisex/adult, or men's? This should not be guessed.
- **Recommended:** once the owner confirms, set age group "adult" and the confirmed gender for all apparel. Use the Shopify category metafields so the same value can feed JSON-LD later. **Status:** needs brand fact.

### F4. P1: Colour missing on the flagship specialist products, and absent from JSON-LD on all single-colour items

- **Current state:** these items have no colour option and no `shopify.color-pattern`: hydrocuff-windbreaker, double-agent-puffa, all 4 sets, the cap and blue-wash-yard-jeans. Separately, the theme emits `color` only from a Colour option, so even single-colour products that do have the colour metafield (e.g. Grey Convict Hoodie) carry no colour in JSON-LD.
- **Evidence:** metafield dump; `crooks-schema-product.liquid` (colour derived from `options_with_values` only).
- **Affected:** feed for 8 products; JSON-LD for about 17 single-colour products.
- **Opportunity:** colour is a required apparel attribute. The HydroCuff and Puffa are the products behind "water reactive jacket" and "heat reactive puffer".
- **Commercial impact:** medium to high. **SEO impact:** medium. **GEO impact:** medium (colour is a common filter in AI shopping answers).
- **Effort:** low for the store data; low for the theme change. **Confidence:** high on the gaps.
- **Dependencies:** the theme change belongs to workstream 2 (product schema), so it should be one coordinated edit.
- **Recommended:** set colour-pattern on the 8 products (values as photographed). In the theme, fall back to the colour-pattern metafield for `color` when no Colour option exists. **Status:** proposed.

### F5. P1: Live, Google-published products with no description

- **Current state:** crooks-express-t-shirt (in stock, 35 units), grey-set, pink-set, black-set and the cap have an empty description. GMC requires a description.
- **Evidence:** Admin API `description`.
- **Opportunity:** fix a likely disapproval. The three Convict sets alone are 100 feed items and 389 units of stock.
- **Commercial impact:** high for the Sets (£110 AOV). **SEO impact:** medium (thin PDPs). **GEO impact:** medium.
- **Effort:** low (5 short descriptions from existing component copy). **Confidence:** high.
- **Dependencies:** copy must use only verified facts (550gsm etc. already on the component products).
- **Recommended:** write short, customer-first descriptions reusing component facts. **Status:** proposed.

### F6. P1: Feed titles are ALL CAPS product names with no product-type words

- **Current state:** the channel sends `product.title`, e.g. "GREY CONVICT HOODIE", "OG JEANS", "CRXST★RZ T-SHIRT", "BLACK/BLUE MOTIONTEC™️ SOCKS". The SEO titles are already good feed titles ("Grey Convict Hoodie — 550gsm Brushed Fleece").
- **Evidence:** Admin API titles vs `seo.title`.
- **Opportunity:** Shopping matches mostly on title. "OG Jeans" carries none of "baggy jeans", and the hoodies carry none of "550gsm heavyweight hoodie". GMC's editorial policy also limits excessive capitalisation and symbols.
- **Commercial impact:** high (relevance and CTR for the target product queries). **SEO impact:** medium. **GEO impact:** medium.
- **Effort:** low to medium. **Confidence:** medium-high.
- **Dependencies:** keep the on-site all-caps titles; they're the brand's design language. Change only the feed.
- **Recommended:** a GMC supplemental feed (Google Sheet) or attribute rule that sets `title` to a sentence-case "CROOKSLDN + name + key attribute + type" built from the existing SEO titles. **Status:** proposed, needs GMC access.

### F7. P1: Sets are half the feed and the weakest data in it

- **Current state:** cellblock-set, grey-set, pink-set and black-set make up 125 feed items. Three are "Uncategorized". The Cellblock Set is categorised as Sweatpants. None has a barcode or per-variant image, three have no description (F5), and none is marked as a bundle.
- **Recommended:** category "Apparel & Accessories > Clothing > Outfit Sets", `is_bundle = yes` via feed rule, descriptions (F5) and colour (F4). Keep them in Shopping, since they're the higher-value basket. **Effort:** low. **Confidence:** high. **Status:** proposed.

### F8. P2: Availability on oversold tees may not match what Google sees

- **Current state:** 27 variants have zero or negative stock but are still for sale (policy CONTINUE): all 10 CRX Garms, all 10 CRXST★RZ (one at −2), 4 Crooks Express (two at −4) and 3 Pink Convict Sweats. The page shows "Order before 18:00 and it ships today" plus a "deferred, subscription, or recurring purchase" notice, so a pre-order selling plan is attached. The theme emits `PreOrder` at the plan price for those. The channel likely sends `in_stock` at variant price. The Admin API returns no selling-plan groups (app-owned), so the plan price couldn't be checked.
- **Risk:** a GMC availability or price mismatch, plus a "ships today" promise on items with no stock.
- **Recommended:** confirm with the F1 export and live JSON-LD. If they're pre-orders, send `availability = preorder` with `availability_date` and drop the "ships today" line for those variants. **Confidence:** medium. **Status:** needs verification.

### F9. P2: Major League Crooks Cap (Cream) is live with no images and no description

- **Current state:** ACTIVE, published to Google, 0 media, empty description, category "Sports Collectibles > Caps". The live page shows "Photo 1 of 0". It will be disapproved (no image).
- **Recommended:** add photos and a description, recategorise to "Clothing Accessories > Hats > Baseball Caps", or return it to draft like its blue and brown siblings. **Status:** owner's call.

### F10. P3: Category data tidy-up

- pink-crsdr-hoodie uses "Clothing Tops > Hoodies" while the other hoodies use "Activewear > … > Hoodies".
- charcoal-cellblock-crewneck and -shorts carry legacy `mm-google-shopping.google_product_category` 212/207 overrides.
- Ten products carry `mc-facebook.google_product_category`.
- **Recommended:** align on one Shopify category per type and drop the overrides once confirmed. **ROI:** low.

### F11. P4: SKUs empty on every variant; weights zero on about 10 products

- With flat-rate shipping and F2 handled via `identifier_exists=no`, neither blocks Shopping. Low ROI, so I've left it.

## Implementation order (for the implementer)

1. F1 check in GMC (owner, before 1 Nov). Its export confirms or drops F2, F3 and F8.
2. GMC-side, non-store rules: F2 (gtin off, identifier_exists=no), F6 (titles), F7 `is_bundle`.
3. Store data (needs the owner's explicit OK): F3 (after the gender fact), F4 colour metafields, F5 descriptions, F7 categories.
4. Theme (shared with workstream 2): F4 colour fallback; optionally emit gender/age group in JSON-LD once set.
5. Monitor: GMC item counts (approved, limited, disapproved), free-listing clicks in GMC Performance, and the Search Console Shopping tab / merchant listings report.

## Owner-confirmed facts, 16 Oct 2026 18:26 UTC (override earlier conclusions in this file)
George confirmed these in the project chat. Where this file says otherwise, this section wins.
1. **Origin:** all current products are made in China. Remove all 7 "Made in Portugal" values. Use China only where origin is required (Shopify customs country, any required feed or legal field). Don't add consumer-facing origin copy otherwise.
2. **Fabric weights:** hoodies 550gsm, joggers 550gsm, crewnecks 450gsm, shorts 450gsm, jeans 14oz, jorts 14oz. OG Jeans is read as 14oz under "jeans"; correct this if George says otherwise. Existing claims matching these weights are supported and stay. Tees have no confirmed weight.
3. **Composition:** current hoodies and joggers are 100% cotton. Don't extend this to other categories.
4. **HydroCuff:** reacts to rain and water, returns to normal when dry, wash cold, do not iron, reaction "reasonably durable" (careful wording, no cycle or lifetime claims). Reaction time is still unconfirmed.
5. **Double-Agent Puffa:** heat-reactive; care guidance is to avoid washing where possible. No wash temperatures, durability or lifetime claims until there's supplier care info.
6. **Barcodes:** swing tags don't carry them, but the item bags do. **Do NOT clear the Shopify barcode values.** First establish whether the bag codes match the Shopify variant barcodes, whether any current or planned pick/pack workflow scans them, and whether moving them to SKU would break matching. The fix for the feed's invalid GTINs moves to the Merchant Center side (feed rule or supplemental feed to stop sending them as GTIN, identifier_exists=no), leaving Shopify untouched.
7. **Tees:** ALL tees are print on demand. Zero or negative inventory on tees is NOT overselling, and continue-selling is correct. The task is now an honesty audit: Shopify supports continued selling, Merchant Center availability and handling time are accurate, customers see a true production and dispatch expectation, and nothing describes tees as physically in stock.

## Owner decisions, 16 Oct 2026 18:30 UTC (override earlier recommendations in this file)
- Theme copy "Claude P1 fixes" (schema and popup): **HOLD**, do not publish.
- Product-data batch 2: **APPROVED**, except that barcodes must not be removed or remapped (item bags use them).
- Google Shopping gender: **MIXED.** Crooks sells men's and women's products, so assign gender per product, never one catalogue-wide value.
- Tracksuits: **YES**, list the three Convict Sets.
- Judge.me reviews on product pages: **NO** for now.
- Mida: **KEEP** (in use). Crooks Partner Hub: **KEEP.** Orderify: no live campaigns, so turn the embed off and prepare removal once no other dependency is found.
- About page: **not approved yet**; keep it drafted. "Designed in-house" = true; "free size swaps" = true.
- Official profiles for sameAs: https://crooksldn.com, Instagram @crooksldn, TikTok @crooksldn **only**. Not crooksldn.uk, X, YouTube, Pinterest or Depop.
- Tier-1 creator samples: **declined for now**.
