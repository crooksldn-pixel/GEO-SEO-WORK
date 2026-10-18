<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 01 · Collection architecture and internal linking

Status: audit done; copy drafted; **implementation blocked on store-write permission** (see bottom). Last updated 16 Oct 2026 14:40 UTC.
Sources: Shopify Admin API reads (products, collections, menus, theme files) and live page reads, 16 Oct 2026. Every product fact below comes from Crooks' own product data; nothing is invented.

## Current state (verified)
- Collections live: sweats (8), denim (5), tees (3), tracksuits (6), accessories (3), new, all. No outerwear.
- Collection template (`sections/crooks-exhibit-log.liquid`) already renders H1 = collection title, the collection description under it, and CollectionPage + ItemList + BreadcrumbList JSON-LD. Canonicals are self-referencing.
- Meta titles/descriptions come from collection SEO fields, with a theme fallback (`snippets/meta-tags.liquid`) that also caps titles at 56 characters including " | CROOKSLDN".
- Main menu already links to the clean handles. Footer SHOP column (`sections/footer-group.json`, block c1) has one free slot (6).
- No visible breadcrumbs. No collection-to-collection or collection-to-guide links in body copy. Homepage body links to products only.
- Double-Agent Puffa has a blank product type and no tags, so no smart collection can include it.

## Opportunities (ranked)

| Rank | Class | Action | Commercial | SEO | GEO | Effort | Confidence | Dependencies | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P1 | Create /collections/outerwear + set Puffa type/tags | High: £85 + £140 SKUs | New indexable category for reactive outerwear | Category page AI can cite for "water/heat reactive jacket" | 20 min | Med-high | Store write permission | Blocked |
| 2 | P1 | Rewrite Sweats copy to the user's chain (British streetwear → heavyweight fleece → baggy → hoodies/joggers → sets) with links to Tracksuits and Sets | High: top revenue category | Adds "heavyweight", "550gsm", "matching tracksuit" semantics | Clear category definition | 10 min | Medium | Store write | Draft ready |
| 3 | P1 | Tracksuits copy: link back to Sweats, add measurements pointer | Med-high | "heavyweight tracksuit UK" | Medium | 10 min | Medium | Store write | Draft ready |
| 4 | P2 | Add Outerwear to main menu + footer slot 6 | Medium | Sitewide internal link to new collection | Low | 10 min | High | #1 first | Waiting |
| 5 | P2 | Denim copy: add cross-links to Sweats/Tracksuits; keep the copy rewritten today | Medium | Internal linking | Low | 5 min | Medium | Store write | Draft ready |
| 6 | P2 | Collection titles (H1) carry the category term: "Heavyweight Sweats", "Heavyweight Tracksuits" | Medium | H1 relevance | Low-med | 5 min | Low-med (no GSC data yet) | Search Console (WS04) ideally | Hold for GSC |
| 7 | P3 | Visible breadcrumbs on collections (theme) | Low-med | UX + matches existing BreadcrumbList | Low | 1 h theme | Medium | Theme port | Later |
| 8 | P3 | Homepage: category link row | Medium | Internal linking from strongest page | Low | 1 h theme | Medium | Theme port; design review | Later |
| 9 | P4 | Tees copy | Low | Thin, 3 products | Low | — | — | 200gsm tee drop (15 drafts) | Revisit at drop |
| 10 | — | Guide links from collections | — | — | — | — | — | Content pages from WS05 | Not yet possible |

## Draft copy (ready to paste into each collection's description, or for me to apply once permitted)

### Sweats · /collections/sweats
Revised 16 Oct 16:05 UTC: GSM figures and "made in Portugal" removed until supplier/customs evidence exists (user answers 20 and 22). Re-add them once evidenced.
- SEO title: `Heavyweight Hoodies & Joggers | Baggy Fleece Sweats`
- Meta: `Convict hoodies and sweats in heavyweight brushed fleece, baggy fit, in matching colours. Cellblock crewneck and shorts. XS–XL. Free UK shipping over £30.`
- Description:
> CROOKSLDN sweats are heavyweight brushed fleece cut baggy. The Convict Hoodie and Convict Sweats come in Black with white contrast piping, Grey with the embroidered handcuff logo, or Pink with white piping and handcuff embroidery, with the sweats cuffed at the hem. Each piece is £60; wear hoodie and sweats together as a tracksuit from the <a href="/collections/tracksuits">Tracksuits</a> collection.
>
> The Cellblock Crewneck (£[redacted]) and Cellblock Shorts (£[redacted]) are a lighter brushed fleece in a relaxed cut with 3D embroidery, and come together as a matching co-ord, the <a href="/products/cellblock-set">Cellblock Set</a>.
>
> Sizes run XS to XL and are true to size. Every product page lists the garment's own measurements: the Convict Hoodie's chest runs from 116.8cm in XS to 132.1cm in XL. Pair them with <a href="/collections/denim">Yard Jorts</a> when it's warm.

### Tracksuits · /collections/tracksuits
- SEO title (live): `Heavyweight Tracksuits: Matching Fleece Sets`. 550gsm is owner-confirmed (18:26) and now in the description; title left as is until GSC shows whether "550gsm" queries exist.
- Meta: keep current.
- Description:
> A CROOKSLDN tracksuit is the Convict Hoodie with the matching Convict Sweats: 550gsm brushed fleece, baggy fit, sweats cuffed at the hem. Three sets: Black, with white contrast piping; Grey, with the embroidered handcuff logo; and Pink, with white piping and handcuff embroidery. Each piece is £60, sizes XS to XL, and you can buy them separately in <a href="/collections/sweats">Sweats</a>. Measurements for every size are on each product page.

### Outerwear · /collections/outerwear (new)
- SEO title: `Water-Reactive & Heat-Reactive Jackets`
- Meta: `The HydroCuff windbreaker shows a cuff pattern in the rain. The Double-Agent Puffa changes appearance with temperature. Free UK shipping over £30.`
- Description:
> CROOKSLDN outerwear reacts to the weather. The <a href="/products/hydrocuff-windbreaker">HydroCuff Windbreaker</a> (£85) has a water-activated cuff pattern that comes through in the rain; it is hooded, with zipped front pockets and contrast stitching. The <a href="/products/double-agent-puffa">Double-Agent Puffa</a> (£140) is a heat-reactive puffer that changes appearance with temperature, with Crooks handcuff embroidery on the chest and hood, a padded fit and concealed hand pockets.
- Rule: smart collection, product type = Outerwear.

### Denim · /collections/denim (copy rewritten today; append one line only)
> Wear them with the <a href="/collections/sweats">Convict Hoodie</a> or a <a href="/collections/tees">graphic tee</a>.

## Gaps needing brand facts (do not fill without the user)
- Fabric composition (e.g. cotton/poly split), country of make for Convict and OG pieces, Puffa/HydroCuff materials. Product pages show "Specification" headings but no text was readable.

## Blocker
Every write to products, collections and menus was refused by this session's safety check ("modifying shared resources"); reads were later refused too. The user can unblock by approving the specific changes in the thread, or by applying the drafts above in Shopify admin.

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

## Done after the 18:30 decisions (16 Oct ~19:05 UTC)
- Tracksuits now lists the 3 Convict Sets (9 products) and its description links them (£110 set vs £60 pieces), with 550gsm, 100% cotton (C-007).
- Sweats draft: GSM may go back in ("550gsm, 100% cotton" for Convict, "450gsm" for Cellblock); still no origin. Still needs a manual paste because the live Sweats/Denim collections aren't reachable by API (C-003).
