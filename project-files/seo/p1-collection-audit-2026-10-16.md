<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# P1 collection audit, 16 Oct 2026

Sources: live pages read on 16 Oct 2026 (14:00–14:15 UTC), Shopify Admin API (collections, products, URL redirects, theme), crooksldn.com sitemap.
Score = commercial impact × likelihood × speed, each 1–5 (max 125). Every copy suggestion uses only facts already in Shopify product data.

**Heads-up:** the store was being edited while this audit ran. /collections/denim went from 1 product with meta "Jorts, jeans and denim." to 5 products with new title, meta and copy between two fetches, and the live theme is "CROOKSLDN — SEO round 2 (from live 16 Oct)", last saved 13:33 UTC. Findings below reflect the latest read.

**Not verifiable from here:** raw HTML and HTTP status codes (this environment's network blocks direct requests to crooksldn.com; pages were read through a text extractor that drops `<script>` tags). So JSON-LD on collection pages and the exact status of /collections/outerwear are unconfirmed.

**Correction, 14:30 UTC:** a recheck against the theme code and Shopify admin showed three findings below were wrong or already fixed. The homepage title and meta are set by the theme ("Crooks London Streetwear | Fleece, Denim & Tees" plus a description); my first read was faulty. The main menu already links to the clean /collections/tees, /denim, /sweats, /new URLs. Collection pages already output CollectionPage, ItemList and BreadcrumbList JSON-LD, and the site outputs Organization, Brand and WebSite. Items 3, 4 and 6 in the table are struck. The zero-stock tees are set to "continue selling when out of stock", which may be deliberate (pre-order or print on demand), so item 1 is a question, not a fix.

## Ranked fixes (ROI class P0–P4)

| Rank | Class | Fix (section) | Impact | Evidence | Effort | Confidence | Action |
|---|---|---|---|---|---|---|---|
| 1 | P0 | Stock showing AVAILABLE at −2 / 0 units (7) | Overselling, refunds, Merchant Center disapprovals | Admin inventory vs live /collections/tees | 10 min | High | Check "continue selling when out of stock" on CRXST★RZ and CRX Garms |
| 2 | P1 | Create Outerwear collection (1) | £85 and £140 products gain a category page for reactive-jacket queries | No collection in admin; URL unreadable; not in menus | 30 min | Med-high | Do now with OK |
| ~~3~~ | done | ~~Homepage title, meta (2)~~ already set by theme; optional brand line + category links is P3 | Entity clarity for "British streetwear brands" family | Title "CROOKSLDN", no meta, no "streetwear" on page | 30 min + theme edit | Medium | Do now with OK; needs "London" confirmed |
| 4 | P2 | ~~Nav menus to final URLs~~ already done; add Outerwear to menu and footer (4) | Cleaner sitewide internal links | Menu links to -1 handles | 10 min | Medium | Do with OK |
| 5 | P2 | Sweats/Tracksuits title and H1 terms (3) | "heavyweight hoodie/tracksuit UK", "550gsm" | Terms absent from title; no query data yet | 10 min | Low-med | Wait for Search Console unless you want it now (meta was rewritten today; guardrail on evidence-free rewrites) |
| ~~6~~ | done | ~~Breadcrumb/ItemList JSON-LD (5)~~ already in theme; visible breadcrumbs optional P3 | Rich results, clearer hierarchy | None visible; JSON-LD unconfirmed | 1–2 h theme | Medium | Inspect theme code first |
| 7 | P2 | Product-type gaps: Puffa, Cream cap (7) | Collections and feed categorisation | Blank productType in admin | 5 min | High | Do with #2 |
| 8 | P3 | Alt text on second images (8) | Image search, small | Missing on 4 denim cards | 20 min | Medium | Batch with P2 product work |
| 9 | P4 | Denim title/H1 tweak (6) | Marginal | Rewritten today | 5 min | Low | Skip until data |
| 10 | P4 | Tees | Thin category | 3 products; 15 drafts pending | — | — | Revisit at the tee drop |

### 1. Outerwear collection (new)
- /collections/outerwear could not be read (fetch error) and no Outerwear collection exists in Shopify. It is not in the header or footer menus.
- HydroCuff Windbreaker (£85, type Outerwear, tagged water-reactive) and Double-Agent Puffa (£140, **blank product type, no tags**) have no category page, so "water reactive jacket", "heat reactive puffer" and "streetwear jacket UK" only have product pages to rank.
- Do: set Puffa product type to `Outerwear` and tag `heat-reactive`, `puffer`, `outerwear`. Create smart collection handle `outerwear`, rule product type = Outerwear.
- Title: `Outerwear: Water-Reactive & Heat-Reactive Jackets | CROOKSLDN`
- Meta: `The HydroCuff windbreaker shows a cuff pattern in the rain. The Double-Agent Puffa changes appearance with temperature. Free UK shipping over £30.`
- H1: `Outerwear`
- Copy (draft, facts from product data only): "CROOKSLDN outerwear reacts to the weather. The HydroCuff Windbreaker has a water-activated cuff pattern that comes through in the rain; it is hooded, with zipped front pockets and contrast stitching. The Double-Agent Puffa is a padded, heat-reactive puffer that changes appearance with temperature, with handcuff embroidery on the chest and hood and concealed pockets."
- Later (P4): link to water-reactive and heat-reactive guides once written.

### 2. Homepage
- Title is just `CROOKSLDN`; no meta description (OG/Twitter description is "CROOKSLDN."); the word "streetwear" never appears; the body links to no collections.
- Title: `CROOKSLDN | Independent British Streetwear, London`
- Meta: `Heavyweight 550gsm hoodies and joggers, baggy denim, graphic tees and reactive outerwear from CROOKSLDN (Crooks LDN). Free UK shipping over £30.`
- Add one visible line near the H1 and a row of category links (Sweats, Tracksuits, Denim, Tees, Outerwear). Needs your confirmation that "London" is accurate for where the brand is based.

### 3. Sweats and Tracksuits
Sweats (8 products, good copy already):
- Title now: `Hoodies, Sweatshirts & Joggers | CROOKSLDN` → `Heavyweight Hoodies & Joggers, 550gsm Fleece | CROOKSLDN`
- H1 now: `Sweats` → `Heavyweight Sweats` (keeps the brand's word, adds the query term)
- Add one copy line linking to /collections/tracksuits for the matching sets (Black/Grey/Pink Set products are not in this collection).

Tracksuits (6 products):
- Title now: `Convict Tracksuits: Matching Fleece Sets | CROOKSLDN` → `Heavyweight Tracksuits, 550gsm Fleece Sets | CROOKSLDN`
- Not in the footer menu; add it.

### 4. Navigation
- Header SHOP dropdown links to /collections/tees-1, denim-1, sweats-1, new-1. Shopify still holds those four as smart collections with broken rules (sweats-1 = type "Sweats", 0 products; denim-1 = type "Denim", 0 products; tees-1 = type "T-Shirt", matches 3 archived tees) plus redirects to the clean handles. Live, they currently land on the right pages, but every page sends its main category links through an extra hop.
- Do: repoint the header menu to /collections/tees, /denim, /sweats, /new; add Outerwear to header and footer, Tracksuits to footer. Then retire the four -1 collections (keep the redirects).
- Note: the Admin API connected here does not return the live tees/denim/sweats/new collections even though they are in the sitemap, so whoever edits them is using access this thread can't see. Worth checking before deleting anything.

### 5. Breadcrumbs and structured data
- No visible breadcrumbs on any collection page; no collection JSON-LD seen (unconfirmed, see top).
- Do: theme snippet for `Home > Shop > {collection}` plus BreadcrumbList and ItemList JSON-LD on collection templates.

### 6. Denim (rewritten today, 5 products)
- Title `Denim Jeans & Jorts | CROOKSLDN` is fine. Option: `Jeans & Jorts: Baggy and Straight Denim | CROOKSLDN` to catch "baggy jeans". Only OG Jeans and Yard Jorts are baggy (Yard Jeans are straight), so don't over-claim "baggy jeans".
- H1 `Denim` → `Denim: Jeans & Jorts`.

### 7. Product data flags (feeds into P2)
- Double-Agent Puffa: blank product type, no tags (blocks #1 and Google product category mapping).
- Major League Crooks Cap (Cream): active, blank product type and SEO fields, so it falls outside the Accessories smart collection (rules: type Accessories or Socks).
- CRXST★RZ T-Shirt total inventory −2 and CRX Garms T-Shirt 0, yet both show AVAILABLE on /collections/tees. Check overselling settings; stock status must match the Merchant Center feed.

### 8. Images
- Second images on Yard Jorts (both), Grey Wash Yard Jeans and OG Jeans have no alt text.

### 9. Tees
- 3 live tees at £25; 15 draft tees tagged `t-shirt-week` (200gsm) are waiting. Copy/meta are fine for now. Revisit when that drop goes live.

## Access that would unlock more
- **Search Console**: real queries and positions to confirm which collection terms have momentum (P3).
- **Merchant Center**: feed vs site consistency (P2).
- **Network access to crooksldn.com from this environment**: raw HTML for JSON-LD and status-code checks.
