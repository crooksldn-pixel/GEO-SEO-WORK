# Index hygiene audit (task F)

Live checks made from the storefront on 18 Oct 2026, 16:40 BST, plus Admin API reads of `urlRedirects`, archived products and collection metafields.

**Status:** prepared, not applied. The brief says to wait for `cowork-results/05-search-console.md`, then get George's yes. Shopify URL redirects only fire when the original path 404s, so every redirect proposed below targets a URL that currently 404s.

## Proposed

| # | URL | Live now | Proposed action | Why |
|---|---|---|---|---|
| 1 | `/products/og-crook-tee` | 404 (archived) | URL redirect → `/collections/tees` | archived tee |
| 2 | `/products/3-clives-tee` | 404 (archived) | URL redirect → `/collections/tees` | archived tee |
| 3 | `/products/broadcast-tee` | 404 (archived) | URL redirect → `/collections/tees` | archived tee |
| 4 | `/products/evil-clive-tee` (Money Clive Tee) | 404 (archived) | URL redirect → `/collections/tees` | archived tee |
| 5 | `/products/large-duffle-bag` (Ballistic Nylon Duffle) | 404 (archived) | URL redirect → `/collections/accessories` | not a tee; product type Accessories; `/collections/accessories` returns 200 with 4 products |
| 6 | `/collections/frontpage` | 200, self-canonical, no robots meta, in `sitemap_collections_1.xml`, title `PRODUCTS \| CROOKSLDN`, 37 products | set metafield `seo.hidden` = 1 (number_integer) | thin duplicate of `/collections/all`; not linked from home or menus. Same mechanism Sets already uses: drops it from the sitemap and adds noindex, with no unpublish or delete |
| 7 | `/products/cb1-wash-jorts`, `/products/cb2-wash-jorts` | redirect to blue / grey Yard Jorts respectively | edit redirect targets **after** George confirms the washes | crossed against the jeans redirects (see below) |

## Leave alone

| URL | Live now | Reason |
|---|---|---|
| `/collections/all` | 200, title `Shop CROOKSLDN Streetwear \| All Clothing` | main-menu SHOP and ALL target |
| `/collections/sweats-1`, `denim-1`, `tees-1`, `new-1` | each redirects to its clean handle; none in sitemap | already handled; never delete |
| `/collections/sets` | 200 but `noindex,nofollow`, not in sitemap | already hidden from search (see task G) |
| `/blogs/news/reactive-outerwear` | 404 | task E not published yet |

## CB1 / CB2 redirects (existing)

| Old path | Current target |
|---|---|
| `/products/cb1-wash-jeans` | `/products/grey-wash-yard-jeans` |
| `/products/cb2-wash-jeans` | `/products/blue-wash-yard-jeans` |
| `/products/cb1-wash-jorts` | `/products/blue-wash-yard-jorts` |
| `/products/cb2-wash-jorts` | `/products/grey-wash-yard-jorts` |

For jeans, CB1 = grey and CB2 = blue. For jorts it's the other way round. If CB1 and CB2 meant the same wash across both lines, one pair is wrong. The brief already flags `cb2-wash-jorts`. Needs George to say which wash CB1 and CB2 were.

## Collections in sitemap_collections_1.xml (18 Oct)

frontpage, tracksuits, tees, denim, sweats, accessories, new, all, outerwear.
