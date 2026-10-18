<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 3 → implementer handoff: feed clean-up before 2 Nov 2026

Owner of these changes: the "Crooks GEO and SEO programme" thread. Source audit: [03-merchant-feed.md](03-merchant-feed.md). Written 16 Oct 2026.

## The user's decision (16 Oct)

The user chose to opt in to Google auto-adding products on 2 Nov, provided the feed is clean beforehand. Opting in means doing nothing in GMC, because auto-add happens by default. So the work is to make the data clean by **31 Oct**, which leaves a day to check the GMC export before the 1 Nov opt-out cut-off. If the export still shows disapprovals on core items on 31 Oct, the fallback is to opt out in GMC and re-assess. The user does that step.

Barcodes (F2) and the oversold tees (F8) are owned by the "Product schema and commerce data" thread (user items 3 and 4). They're not repeated here.

## Store changes (each needs the user's explicit OK naming the change, per memory)

### 1. Gender and age group (F3)
- **Evidence (16 Oct):** no product, collection, nav or homepage text says men's, women's or unisex. Bottoms run waist 76.2–96.5 cm (30–38"), which is menswear waist sizing. Tops are oversized, with height guidance from about 5'4" (XS) to 5'10" (M).
- **Status:** the user's rule is "unisex only where sizing and positioning support it". This evidence doesn't clearly support unisex. The value is pending the user's answer on the decision card in the Merchant Center feed parity thread.
- **Change once decided:** for all 24 active apparel products, set `shopify.age-group` = adult, and `shopify.target-gender` = the chosen value. Use the category metafields so the same value can feed JSON-LD `audience` later.

### 2. Colour on 8 products (F4; overlaps workstream 2)
| Product | Value | Basis |
|---|---|---|
| hydrocuff-windbreaker | Black | product tag "black" |
| blue-wash-yard-jeans | Blue | title, tag |
| grey-set | Grey | title, components |
| pink-set | Pink | title, components |
| black-set | Black | title, components |
| cellblock-set | Charcoal | title, components |
| major-league-crooks-cap-cream | Cream | title |
| double-agent-puffa | **unknown** | the page names no colour. Ask the user for the base colour. Don't guess, because it changes with heat. |

### 3. Descriptions on 4 live products (F5)
These are drafts built only from facts already on the store. GSM figures are left out until the user supplies a spec sheet (user item 22).
- **grey-set:** "The Grey Convict Hoodie and Grey Convict Sweats together: brushed fleece, baggy fit, with the sweats cuffed at the bottom. Choose a size for each piece. £110 for the set, against £120 bought separately."
- **black-set / pink-set:** the same text with Black or Pink.
- **crooks-express-t-shirt:** "Crooks Express logo tee in White or Black. Cotton, with full measurements for every size in the size chart."
- Check: £120 = 2 × £60 (component variant prices, 16 Oct). Fabric per the `crooks.fabric` metafields. "Cotton" comes from the product tag and SEO title.

### 4. Categories (F7 and F9)
- grey-set, pink-set, black-set (Uncategorized) and cellblock-set (currently Sweatpants): set to Apparel & Accessories > Clothing > Outfit Sets.
- major-league-crooks-cap-cream (Sports Collectibles): set to Apparel & Accessories > Clothing Accessories > Hats > Baseball Caps.
- Check each value exists in Shopify's taxonomy before writing.

### 5. Cap with no photos (F9)
Least destructive option: unpublish it from the **Google & YouTube** channel only, and republish when the user's Cream cap photo arrives (user item 25). It stays on the site. Otherwise it's a guaranteed disapproval.

## Theme change (workstream 2 owns the schema file; coordinate)
- In `snippets/crooks-schema-product.liquid`, emit `color` from `shopify.color-pattern` when the product has no Colour option. Once item 1 is set, add `audience` (PeopleAudience with suggestedGender and suggestedMinAge). Auto-added items are built from this JSON-LD, so it matters for the 2 Nov path.

## GMC-side (only the user can do these; there's no GMC access from the project)
- Download Products > All products CSV, upload it to the project, and repeat on about 30 Oct to confirm before the opt-out cut-off.
- Optional, after the export: a supplemental feed for sentence-case titles (F6) and `is_bundle = yes` on the 4 sets (F7).

## Metric to watch
GMC approved vs limited vs disapproved item counts (from the export), and the number of auto-added items after 2 Nov. Watch for duplicates of channel items.

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

## Workstream 3 corrections after the owner's facts (16 Oct 2026, evening)

These replace items 1 and 3 above, and F2 and F8 in the audit, wherever they conflict.

### A. Gender per product (replaces item 1)
- Assign it per product. Age group = adult on all 24 apparel products; that part is ready now.
- No product, tag, title or collection in Shopify marks anything as women's (searched 16 Oct). So **which products are women's (or for both) has to come from the owner.** Until then, leave gender unset rather than defaulting to male, so nothing gets mislabelled.
- Write it to `shopify.target-gender` per product, then to JSON-LD `audience` (theme, on hold with the P1 theme).

### B. Material, 100% cotton (new)
- Hoodies and joggers only: v1-hoodie, convict-hoodie-1, pink-crsdr-hoodie, v2-baggies, black-joggers, pink-crsdr-joggers. The Grey, Black and Pink sets are these same garments, so the same value applies; cellblock-set does not.
- `shopify.fabric` on these is currently "Fleece" (metaobject fleece-1). Add the existing "Cotton" metaobject (gid://shopify/Metaobject/599082402135). Whether to keep Fleece alongside is the implementer's call; Google's `material` should read Cotton.
- `crooks.fabric` text (which drives JSON-LD `material`): change "550gsm brushed fleece" to "100% cotton, 550gsm brushed fleece".

### C. Country of origin (new)
- Google Shopping UK does not need origin in the feed, so there's no feed change.
- Shopify customs origin is set to CN on only 6 products (both Grey and Black Convict pieces, Pink Convict Hoodie, Grey Wash Yard Jeans). It's blank on the other 19. The owner has confirmed China for all, so set CN on the rest. This matters for the enabled international markets (duties at checkout). It's store data, so it goes via the product-schema thread's batch.
- Removing the "Made in Portugal" text stays with the product-schema thread.

### D. Print-on-demand tees: availability and dispatch honesty (replaces F8)
Current state (16 Oct): all 30 tee variants have inventory *tracked*, with policy CONTINUE. Stock sits at 0 or below (−4 on two Crooks Express variants, −2 on one CRXST★RZ). The page says "Order before 18:00 and it ships today" and shows a "deferred, subscription, or recurring purchase" notice from an old pre-order selling plan.
1. **Shopify:** turn off inventory tracking on the tee variants. Continued selling then needs no negative stock, and the theme's offer state resolves to InStock rather than PreOrder (it only marks PreOrder for tracked, zero-stock items). The 2 negative counts disappear with it.
2. **Old selling plan:** detach the leftover pre-order plan (app "ReStock", per the theme comment) from the tees, so checkout stops calling them a recurring or deferred purchase. Confirm first that the app is no longer in use.
3. **Google:** `in_stock` is the right availability for made-to-order items that ship within the stated handling time (confidence: medium; check against the GMC export). Give tees a `shipping_label` (e.g. "print-on-demand") and a handling time in GMC shipping that equals the real production plus dispatch time.
4. **Site:** replace "ships today" on tees with the true production and dispatch time. Set the JSON-LD `handlingTime` for tees to the same number (theme change; on hold with the P1 theme).
- **Needed from the owner:** how many working days a tee takes from order to dispatch.

### E. Invalid GTINs fixed in Merchant Center, Shopify barcodes untouched (replaces the F2 store-side route)
Yes, this can be done entirely in Merchant Center. In MC 5860086407, open Data sources, then the Shopify (Content API) source, then Attribute rules:
1. On `gtin`: find and replace with the regex `^\d{8}$` → empty. This catches only 8-digit codes, so any future real 12–14-digit GTIN still passes. That's the same rule the theme already applies.
2. On `identifier_exists`: set it to `no` where `brand` = CROOKSLDN and `gtin` is empty.

All 112 invalid codes are 8 digits, so the rule covers every one. The item-bag barcodes in Shopify stay exactly as they are. The owner (or anyone with GMC access) applies this; there's no project access to GMC. Confidence: high that it fixes the GTIN issue, medium on the exact rule UI wording.
