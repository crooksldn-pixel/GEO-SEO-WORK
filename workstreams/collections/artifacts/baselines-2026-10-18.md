# Live baselines — collections and fit article

Read from the live storefront (crooksldn.com) and Shopify admin. First captured 16 Oct 2026 20:30–20:45 BST, re-checked 18 Oct 2026 16:40 BST: **all unchanged** between the two reads.

The theme renders collection `<title>` as `{SEO title} | CROOKSLDN`.

The Admin API returns `null` for Sweats, Denim and Tees, by handle and by ID. Read and edit those three in the Shopify admin UI.

| Collection | ID | Type | Products | Read via |
|---|---|---|---|---|
| Sweats | 688184131927 | smart, Type = Sweats | 8 | admin UI + storefront |
| Denim | 688184099159 | smart, Type = Denim | 5 | admin UI + storefront |
| Tees | 688184066391 | — | — | storefront |
| Tracksuits | 687058518359 | custom | 9 | Admin API |
| Sets | 691325337943 | custom | 4 | Admin API |
| Outerwear | 698784121175 | smart, Type = Outerwear | 2 | Admin API |
| frontpage | 678766281047 | — | 37 | Admin API |

---

## /collections/sweats

- **H1:** `Sweats`
- **SEO title:** `Hoodies, Sweatshirts & Joggers` → renders `Hoodies, Sweatshirts & Joggers | CROOKSLDN`
- **Meta:** `Convict hoodies and sweats in 550gsm brushed fleece, plus the 450gsm Cellblock crewneck and shorts. Sizes XS to XL. Free UK shipping over £30.`
- **Description** (one paragraph, no links):

> Heavyweight fleece from CROOKSLDN. The Convict Hoodie and Convict Sweats are 550gsm brushed fleece in a baggy fit, with the sweats cuffed at the hem; each hoodie pairs with the sweats in the same colour as the Black, Grey or Pink Set, £60 a piece. The Cellblock Crewneck (£50) and Cellblock Shorts (£45) are 450gsm brushed fleece in a relaxed cut with 3D embroidery, made in Portugal; the shorts finish above the knee. Sizes XS to XL.

- **Products:** Pink, Black and Grey Convict Hoodie; Pink, Black and Grey Convict Sweats; Charcoal Cellblock Crewneck; Charcoal Cellblock Shorts. The Cellblock Set is **not** in this collection.

## /collections/denim

- **H1:** `Denim`
- **SEO title:** `Denim Jeans & Jorts` → renders `Denim Jeans & Jorts | CROOKSLDN`
- **Meta:** `Yard Jeans, Yard Jorts and OG Jeans from CROOKSLDN: 14oz and heavyweight denim in straight and baggy cuts, blue and grey washes. Free UK shipping over £30.`
- **Description HTML** (exact, from the admin HTML editor; rewritten outside the project on 16 Oct):

```html
<p>CROOKSLDN denim comes in three cuts. Yard Jeans are 14oz denim in an OG straight cut with a mid rise: structured, not baggy, in blue or grey wash, with an embroidered handcuff graphic on the back pockets. Yard Jorts are baggy 14oz denim shorts that finish below the knee, with the Convict embroidery on the back pockets, also in blue or grey wash. OG Jeans are heavyweight denim with a baggy, stacked fit and a white handcuff graphic on the back pockets. The Yard pieces are made in Portugal; wash cold, inside out, and hang dry. Sizes XS to XL, with measurements in each size guide.</p>
```

- **Products:** Grey Wash and Blue Wash Yard Jorts, Blue Wash and Grey Wash Yard Jeans, OG Jeans.

## /collections/tracksuits

- **H1:** `TRACKSUITS`
- **SEO title:** `Heavyweight Tracksuits: Matching Fleece Sets` · **Meta:** none set
- **updatedAt:** 2026-10-18T11:25:15Z. The description and SEO fields are identical to 16 Oct.
- **Description HTML:**

```html
<p>A CROOKSLDN tracksuit is the Convict Hoodie with the matching Convict Sweats: 550gsm, 100% cotton brushed fleece, baggy fit, sweats cuffed at the hem. Three colours: Black, with white contrast piping; Grey, with the embroidered handcuff logo; and Pink, with white piping and handcuff embroidery.</p><p>Buy the full tracksuit as a set for £110 (<a href="/products/grey-set">Grey Set</a>, <a href="/products/black-set">Black Set</a>, <a href="/products/pink-set">Pink Set</a>) and choose a size for each piece, or buy each piece separately for £60 in <a href="/collections/sweats">Sweats</a>. Sizes run XS to XL, and measurements for every size are on each product page.</p>
```

## /collections/sets

- **H1:** `Sets` · **Title:** `Sets | CROOKSLDN`. No description, SEO title or meta.
- **Metafield** `seo.hidden` = `1`, so the live page carries `<meta name="robots" content="noindex,nofollow">` and the collection is absent from `sitemap_collections_1.xml`.
- **Products:** Black Set, Pink Set, Grey Set, Cellblock Set (all product type "Sets").
- Not in any menu and not linked from the homepage.

## /collections/outerwear (already live, not to be redone)

- **SEO title:** `Water-Reactive & Heat-Reactive Jackets`
- **Meta:** `The HydroCuff windbreaker shows a cuff pattern in the rain. The Double-Agent Puffa changes appearance with temperature. Free UK shipping over £30.`
- **Description:** links `/products/hydrocuff-windbreaker` and `/products/double-agent-puffa`.

## /blogs/news/convict-vs-cellblock-fit

- Article `gid://shopify/Article/676342530391`, published 2026-10-16T13:10:18Z, unedited since.
- The section that D would replace:

```html
<h2>What 550gsm and 450gsm mean</h2>
<p>gsm is grams per square metre of fabric. At 550gsm, the Convict fabric is about 22% heavier than the Cellblock's 450gsm. That extra weight is what gives the Convict hoodie and sweats their heavy, structured hang. The Cellblock is lighter, for layering or warmer days.</p>
```

## Main menu (SHOP dropdown)

ALL `/collections/all` · NEW `/collections/new` · TEES · DENIM · SWEATS · TRACKSUITS · OUTERWEAR · ACCESSORIES. Sets and frontpage are not in any menu.
