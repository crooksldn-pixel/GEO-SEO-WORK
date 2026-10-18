<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 02 · Product structured data, variants and commerce data

Status: audit done, read-only. Nothing changed in Shopify or the theme. Last updated 16 Oct 2026 16:00 UTC (verification of user answers 3, 4, 20 added below).
Implementer: workstream 01 thread (owns the master queue and all store/theme writes).
Sources: Shopify Admin API reads of all 25 active products (variants, inventory items, selling plans, metafields, publications), shop policies, live theme "CROOKSLDN — SEO round 2 (from live 16 Oct)" files `snippets/crooks-schema-product.liquid`, `crooks-schema-offer-state.liquid`, `crooks-schema-shipping.liquid`, `crooks-schema-site.liquid`, `snippets/meta-tags.liquid`, `sections/crooks-exhibit-record.liquid`, product templates and app embeds; live page reads of /products/black-joggers and /products/crx-garms-t-shirt.
Limits: rendered JSON-LD can't be fetched from this environment (scripts stripped), so schema findings come from the theme code. No Merchant Center access, so feed findings are inferred from what the Google & YouTube channel is sent (Shopify product data).

## Current state (verified)

What already works, so no work is needed here:
- PDP JSON-LD is server-rendered by `crooks-schema-product` from `sections/crooks-exhibit-record.liquid:81`. Multi-variant products emit `ProductGroup` + `hasVariant` Products with `variesBy`, `productGroupID`, per-variant `@id`/Offer URL `?variant=<id>`, size and colour from options, image, price, availability, `itemCondition`, seller → Organization `@id`, brand → Brand `@id`, UK `shippingDetails`. Single-variant products emit a plain `Product`.
- Pre-orders made with the CROOKS Operations app (`clive-preorders`) are emitted as `PreOrder` at the plan price.
- `gtin` is only emitted for 12–14 digit barcodes, so the store's fake 8-digit barcodes are kept out of the schema.
- `MerchantReturnPolicy` (14 days, by mail, customer pays change-of-mind postage, free for faulty) sits on the Organization and matches the refund policy.
- Canonical is Shopify's `canonical_url` (variant query stripped). BreadcrumbList on PDPs uses the product's first real collection.
- Material, country of origin, cut and care come from `crooks.*` metafields.

## Ranked opportunities

| Rank | Class | Action | Commercial ROI | SEO | GEO | Effort | Confidence | Dependencies | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P0 | Zero-stock tees: record real stock, stop selling at 0, remove legacy ReStock plan | High: oversell and refund risk on 3 of 3 live tees; checkout shows a recurring-purchase notice | Availability mismatch is a Merchant Center disapproval reason | AI shopping answers repeat "in stock" | 10 min | High (verified: shipped from stock, not print-to-order) | **User: shelf count per variant** | Verified; awaiting count |
| 2 | P0 | Country of origin: remove unsupported "Made in Portugal" on 7 products; establish origin per SKU from supplier records | Trust and legal (origin claims, customs) | Low | Medium: schema states "Portugal" | 15 min | High that Portugal is unsupported | **User: remove now? + supplier records** | Verified; decision asked |
| 3 | P1 | Replace fake barcodes: move to SKU, clear barcode | High for Shopping: invalid and duplicated GTINs on 112 variants | Medium: free listings | Medium: clean identifiers for shopping agents | 30–45 min bulk edit | High | User OK given 16 Oct; operational use checked (none) | Ready for implementer |
| 4 | P1 | Fill Shopping apparel attributes: category metafields (colour, fabric), fix wrong colours, product type and category on Puffa/Cap; confirm gender and age group in the Google channel | High: outerwear (£85, £140) is weakest-specified | Medium | Medium | 30 min | Medium-high | Overlaps WS03 (feed parity); Puffa type also needed by WS01 | Proposed |
| 5 | P1 | Major League Crooks Cap: active and published with no images | Can't list in Shopping; broken PDP | Low | Low | 10 min + photo | High | Needs a product photo from the brand | Escalated (asset) |
| 6 | P2 | Show Judge.me reviews on PDPs, then add `aggregateRating` to the schema | Medium: 37 reviews on 15 products, none visible | Review snippets for merchant listings | Medium: AI shopping answers cite ratings | 1–2 h theme | Medium | Theme (WS01 lock); note three products sit at 1.0 | Proposed |
| 7 | P2 | Schema: emit `color` and `material` for single-colour products from `shopify.color-pattern` / `shopify.fabric` | Low-med | Medium: colour is a key apparel attribute | Medium | 30 min theme | High | Rank 4 data first | Proposed |
| 8 | P2 | Set shipping weights on 11 products at 0 | Medium: international rates are weight-based, so these ship under-charged | Low | Low | 15 min | High | Weights from the brand | Proposed |
| 9 | P2 | Shipping parity: PDP says "Free UK Tracked 24 included" on a £60 item; policy says free Tracked 24 from £80; schema uses £3 / free from £30 | Medium: customer promise and Merchant Center shipping must match | Low | Low | 15 min check | Medium | Check checkout rates and Google channel shipping | Proposed |
| 10 | P3 | Sets: remove duplicate `size` keys in variants, set a category, decide whether noindexed sets should be in Shopping | Low-med | Low | Low | 30 min | Medium | Business call on sets in Shopping | Proposed |
| 11 | P3 | Pink Convict Hoodie "Variant V1/V2" option: say what it is on the page and in `variesBy` | Low | Low | Low | 15 min | Medium | User: what is V1 vs V2? | Proposed |
| 12 | P4 | Stale schema comment (says no reviews app); reaction templates exist but HydroCuff/Puffa use the default template; returns schema is GB only; `handlingTime` 0–2 vs same-day dispatch | Low | Low | Low | — | — | — | Note only |

## Detail

### 1. Zero-stock tees (P0)
- Evidence: CRX Garms tee total stock 0 (all 10 variants), CRXST★RZ −2 (all 10), Crooks Express 35 with 4 variants at ≤0. All three use inventory policy CONTINUE and carry only the old `ReStock` "preorder" selling plan, which `crooks-schema-offer-state` ignores, so every variant is emitted `InStock` at £25 with 0–2 day handling.
- Live /products/crx-garms-t-shirt (16 Oct): all sizes selectable, "Order before 18:00 and it ships today", plus Shopify's "deferred, subscription, or recurring purchase" consent text from the ReStock plan.
- Affected: /products/crx-garms-t-shirt, /products/crxst-rz-t-shirt, /products/crooks-express-t-shirt; Google & YouTube feed.
- Recommended: if the tees are not printed to order, set those variants to DENY (stop selling at 0). If they are pre-orders, attach the `clive-preorders` plan (the schema then emits PreOrder by itself, as on Pink Convict Sweats) and remove the old ReStock group. Either way remove the ReStock plan so the recurring-purchase notice goes.
- Monitor: Merchant Center availability mismatches; refunds on tee orders.

### 2. Country of origin conflict (P1, needs brand facts)
- `crooks.origin` says "Made in Portugal" on Grey Convict Sweats and Grey Wash Yard Jeans, while the same products' inventory-item country of origin (used for customs) is **CN**. The three Convict Hoodies and Black Convict Sweats are also CN. Blue Yard Jeans, Yard Jorts and Cellblock say Portugal with no customs value.
- The schema publishes `countryOfOrigin: Portugal`. One of the two fields is wrong, and I can't tell which.
- Recommended: the user confirms origin per line; then set both fields to agree. Never guess.

### 3. Fake barcodes (P1)
- Every barcode is the last 8 digits of the variant ID (e.g. variant …78347351 → 78347351). 107 of the 112 barcoded variants fail the GTIN check digit. OG Jeans' five codes are copied onto Grey/Blue Yard Jeans and both Yard Jorts, so five products share identical "GTINs". SKUs are empty on 219 of 224 variants (only CRXST★RZ black has SKUs). The other 112 variants (the four sets, the Puffa, the Cap and one Grey Convict Sweats size) have no barcode at all.
- Shopify's Google & YouTube channel sends barcode as GTIN, so Merchant Center most likely shows invalid or mismatched GTIN warnings (not verified: no MC access).
- Recommended: copy each barcode into the empty SKU field (or a proper SKU scheme like the existing CRKTRSBLKXS), then clear barcode. The theme already emits `sku`, and the channel can then send brand + MPN with no GTIN, which is correct for an own-brand label. Before clearing, check that the warehouse (Oairo / Click & Drop / POS) doesn't scan these codes.
- Monitor: Merchant Center item issues (GTIN), free-listing impressions.

### 4. Apparel attributes for Shopping (P1)
- Category metafields missing entirely on HydroCuff Windbreaker, Double-Agent Puffa, the Cap, all four Sets, and Blue Wash Yard Jeans (size only).
- Wrong values: Grey Wash Yard Jorts colour = Black; both MotionTec socks colour = "Geometric" (a pattern).
- Product type blank on Puffa and Cap; Cap's category is "Sports Collectibles > Caps" (should be Apparel & Accessories > Clothing Accessories > Hats > Baseball caps). Sets: three Uncategorized, Cellblock Set filed as Sweatpants. Pink Convict Hoodie sits under "Clothing Tops > Hoodies" while the other two are under "Activewear > Hoodies".
- No gender or age group in product data; UK apparel listings require both. They may be set as channel defaults; check in the Google & YouTube app.
- Puffa: no tags, no fabric/origin metafields, both images have empty alt (WS08).

### 6. Reviews (P2)
- Judge.me holds 37 reviews across 15 active products (e.g. Grey Convict Sweats 7 × 5.0, Black Convict Sweats 7 × 3.86, Grey Wash Yard Jeans 3 × 4.67). The Judge.me core embed is on, but no review block is placed in the product templates, and the live page shows no reviews. The schema has no `aggregateRating`, and its comment wrongly says no reviews app is installed.
- Google only allows `aggregateRating` when the reviews are visible on the page, so the order is: add the Judge.me block to `templates/product.json` (and the reaction templates), then emit `aggregateRating` from `product.metafields.reviews`. Judge.me's own JSON-LD uses `@id` `/products/<handle>#product`, which resolves to the theme's `@id`, so the two merge rather than duplicate.
- Caveat: Black Convict Hoodie, Crooks Express Tee and Black Set are each 1 review at 1.0.

### 8. Weights at 0
White socks, CRX Garms tee, CRXST★RZ tee, both Yard Jorts, Cellblock Crewneck, Pink Convict Sweats, Cap, Puffa, and all four Sets. International shipping is charged by weight at checkout.

## Verification of user answers 3, 4 and 20 (16 Oct 2026, 16:00 UTC)

Read-only checks: Shopify locations, orders, inventory levels, metafield timestamps; the brand Gmail (team@crooksldn.com / [brand Gmail address]) and Google Drive. Nothing changed.

### Tees (answer 3): not print-to-order; they ship from stock that Shopify doesn't count
- One location only ("Shop location", [town redacted]), no fulfilment service or print partner; every order is fulfilled manually with Royal Mail labels.
- Since 31 Aug 2026, [n] orders containing CRX Garms or CRXST★RZ were fulfilled within about a day (e.g. CROOKS-[order] ordered 1 Oct, fulfilled 2 Oct; CROOKS-[order] within 35 minutes). Print-to-order couldn't do that.
- Shopify shows on-hand 0 for every CRX Garms variant and 0/−2 for CRXST★RZ, with nothing incoming. So the physical stock exists but isn't recorded. The May [n] orders took 2–3 months, which was a genuine pre-order period that has ended.
- Recommended fix (implementer, once counts are in): enter the real counts per variant, switch the variants to stop selling at 0 (DENY), and remove the legacy ReStock "preorder" selling plan from all three tees. That also removes the recurring-purchase notice. The schema then reports availability correctly with no theme change.
- **Needs from the user:** a shelf count of CRX Garms and CRXST★RZ by colour and size, and the Crooks Express sizes at 0 or below (Black/White XS–XL).

### Barcodes (answer 4): not used operationally, so clearing is safe
- iPacky: trial installed 17 May 2026 and uninstalled by 30 May 2026 (iPacky's own emails). It isn't installed now.
- No warehouse or 3PL: one location, manual fulfilment, Royal Mail Click & Drop labels. None of these use the barcode field.
- The codes couldn't work with a scanner anyway: OG Jeans, both Yard Jeans and both Yard Jorts share the same five codes, so one scan would match five products.
- Shopify POS has been used for [n] orders (CROOKS-[order]/1708, 15 Jul 2026). POS can scan barcodes, but with duplicates across products it isn't relied on. One residual check for the user (also raised by the feed thread, WS03 F2): if printed swing tags carry these codes and get scanned at pop-ups, POS would stop finding the product after clearing, because POS scans barcode, not SKU.
- Recommended (implementer): copy each variant's current barcode into its empty SKU field first, so nothing is lost and it stays reversible, then clear the barcode field. This applies to all 112 barcoded variants. Leave CRXST★RZ Black's existing SKUs (CRKTRSBLK*) as they are.

### Country of origin (answer 20): P0. "Made in Portugal" has no supporting record
- All seven "Made in Portugal" values (`crooks.origin` on Grey Convict Sweats, Grey/Blue Wash Yard Jeans, Blue/Grey Wash Yard Jorts, Cellblock Crewneck, Cellblock Shorts) were written in one batch on 6 Aug 2026 at 11:24 UTC. That pattern is a bulk edit, not per-product data entry.
- Customs origin `CN` with HS codes was entered on 5–8 Oct 2026 for Grey/Black Convict Sweats, all three Convict Hoodies and Grey Wash Yard Jeans, which looks like operational international-shipping data.
- Brand email shows Chinese supplier activity (Alibaba Trade Assurance orders, a refund case in Aug 2026, a bulk-order quote from a +86 supplier in Jul 2026) and Pakistani manufacturer outreach. I found no Portuguese manufacturer, invoice or correspondence. The only Drive "Portugal" files are football-jersey designs.
- What it means: the site, the spec panel and the Product schema (`countryOfOrigin: Portugal`) state an origin that nothing in the records supports, for 7 products. I can't confirm China per SKU either, because customs CN covers only 6 products and the Yard jorts/Cellblock have none.
- **Decision for the user:** remove the 7 "Made in Portugal" values now (stops the unsupported claim; schema and spec panel drop origin automatically), or leave them until the supplier records are found. Recommended: remove now. It asserts nothing new and is reversible.
- Still needed per SKU: supplier invoice or packing list naming the factory country, for every active product. Customs values are blank on 15 products.

## Dependencies and file ownership
- All product/variant/metafield edits (ranks 1–5, 8, 10, 11) are Shopify writes: workstream 01 thread only, after the user's OK.
- Schema changes (ranks 6, 7, 10) are in `snippets/crooks-schema-product.liquid` and product templates: same lock, port onto the live theme copy, never publish wholesale.
- Rank 3 and 4 overlap WS03 (Merchant Center/feed). WS03 should verify them in Merchant Center before and after.

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

## Implementation and audits after the owner's facts (16 Oct 2026, ~18:45 UTC)
This section supersedes the "Verification" conclusions above on tees (they are print on demand), barcodes (keep them: item bags carry them) and origin (China).

**Done (change log C-WS02-1):** the 7 "Made in Portugal" values are removed, and the crewneck copy is cleaned. Customs origin is now CN on every active non-tee product, 25 products in all. The spec panel and schema drop origin by themselves, so no theme change is needed. Barcodes are untouched.

**Batch 2 (Q9–Q12, Q16):** the programme thread wrote these at 18:36–18:37 UTC. Admin read-back confirms:
- colours on the sets and the cap, and the grey jorts and socks fixed;
- categories: Outfit Sets and Baseball Caps;
- the cotton fabric metaobject and "100% cotton, 550gsm brushed fleece" text on the hoodies and joggers;
- descriptions on the 3 Convict Sets and Crooks Express (Express now says "printed to order");
- bottoms images and alt text on the Pink, Black and Cellblock Sets;
- the Puffa heat-reacted image (position 2) and its alt text.

The cap was still on Google & YouTube at 18:40 (Q16). This thread did not write any of these, to avoid double edits.

**Tee (print-on-demand) audit:**
- All tee variants are tracked, with policy CONTINUE. Selling continues correctly, but stock goes negative.
- Recommended: turn tracking off on the 30 active tee variants. The theme then shows InStock instead of PreOrder, and the negative counts go away.
- 4 Crooks Express and all CRX Garms and CRXST★RZ variants carry the app-owned "preorder" selling plan (app "ReStock", created 23 Mar 2026, attached to 480 variants including drafts). It is not visible to this connection as a group, so it can't be detached from here.
- Of the last [n] orders (10 Sep to 16 Oct), none used any selling plan, including about [n] tee orders. The plan is therefore unused at checkout but still triggers the "deferred/recurring purchase" notice.
- Fix: in the ReStock app (or by uninstalling it, once confirmed unused), remove the plan from the tees. The owner or programme thread does this in admin.
- "Ships today" on tees is untrue for print on demand.
- Needed from the owner: the working days from order to dispatch for a tee. That one number drives the PDP line, the JSON-LD handlingTime and the Merchant Center handling time.
- Tee customs origin is left blank: where a print-on-demand blank is made and printed is not on record.

**Bag barcode audit:**
- Every Shopify barcode, 99 of 99 checked, equals the last 8 digits of its own variant ID. They are Shopify-generated label codes, not GS1 GTINs, which is consistent with bag labels printed from Shopify.
- Problem found: 5 codes are shared across 5 denim products by size. For example, 78347351 is the XS of OG Jeans, Grey Wash Yard Jeans, Blue Wash Yard Jeans, Blue Wash Yard Jorts and Grey Wash Yard Jorts. A scan of a denim bag can't tell these apart, so POS or scanner picking will offer 5 matches or the wrong one.
- To confirm the bags match Shopify, a photo of one bag label per product is needed (the denim ones especially). None is in the project.
- Moving codes to SKU would break any scan that reads the barcode field, so don't move them. The Merchant Center GTIN fix stays feed-side (03 handoff, section E).
- Fixing the denim duplicates means new codes on 20 variants plus relabelled bags. That's an owner decision, not an SEO one.
