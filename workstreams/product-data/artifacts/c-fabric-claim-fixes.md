# C — fabric and weight claim fixes (exact strings)

Prepared 18 Oct 2026 from live Admin reads at 16:30 BST. Nothing here is live.

Rule applied (George, 16 Oct 2026): hoodies and joggers 550gsm, 100% cotton; crewnecks and shorts 450gsm; jeans and jorts 14oz; tees have no confirmed weight; the cotton claim applies to hoodies and joggers only and is not extended to any other category.

Fixes C1–C5 only remove the unconfirmed word. They add no new claims. If George confirms a composition for the tee blanks or the socks as a new fact, C2–C5 are dropped or rewritten to match.

`shopify.fabric` values are metaobject references. Cotton = `gid://shopify/Metaobject/599082402135`, Fleece = `gid://shopify/Metaobject/599082434903`.

---

## C1 — CHARCOAL CELLBLOCK SHORTS (`gid://shopify/Product/10967990010199`)

| Field | Before | After |
|---|---|---|
| shopify.fabric | Cotton, Fleece | Fleece |

This matches the Charcoal Cellblock Crewneck, which is already Fleece only.

## C2 — CROOKS EXPRESS TEE (`gid://shopify/Product/10642177786199`)

| Field | Before | After |
|---|---|---|
| Description | `<p>The Crooks Express tee in Black or White: a red CROOKS logo with a blue dashed-line graphic on the chest. Cotton. Each tee is printed to order.</p><p>Full measurements for every size are in the size chart.</p>` | `<p>The Crooks Express tee in Black or White: a red CROOKS logo with a blue dashed-line graphic on the chest. Each tee is printed to order.</p><p>Full measurements for every size are in the size chart.</p>` |
| SEO title | Crooks Express Tee — Cotton Logo T-Shirt \| CROOKSLDN | Crooks Express Tee — Graphic Logo T-Shirt \| CROOKSLDN |
| SEO description | Crooks Express tee in cotton, with the red CROOKS logo and blue dashed-line graphic across the chest. In black or white. | Crooks Express tee with the red CROOKS logo and blue dashed-line graphic across the chest. In black or white. |
| Image 1 alt | CROOKSLDN black cotton t-shirt featuring a red CROOKS logo with a blue dashed line graphic on the chest | CROOKSLDN black t-shirt featuring a red CROOKS logo with a blue dashed line graphic on the chest |
| Image 2 alt | CROOKSLDN white cotton t-shirt featuring a red CROOKS logo and blue dashed line graphic on the chest | CROOKSLDN white t-shirt featuring a red CROOKS logo and blue dashed line graphic on the chest |
| crooks.fabric | Cotton | cleared |

## C3 — CRX GARMS T-SHIRT (`gid://shopify/Product/10837626683735`)

| Field | Before | After |
|---|---|---|
| Description | `<p><span><strong>CRX Garms</strong> tee, built for everyday rotation.</span><span><br> </span><span>Premium cotton with a structured fit.</span></p>` | `<p><span><strong>CRX Garms</strong> tee, built for everyday rotation.</span><span><br> </span><span>Cut with a structured fit.</span></p>` |
| SEO title | CRX Garms T-Shirt — Premium Cotton Tee \| CROOKSLDN | CRX Garms T-Shirt — Graphic Logo Tee \| CROOKSLDN |
| SEO description | CRX Garms tee in premium cotton with a structured fit and the CRX Garms logo graphic across the chest. In black or white. | CRX Garms tee with a structured fit and the CRX Garms logo graphic across the chest. In black or white. |
| Image 1 alt | CROOKSLDN black premium cotton t-shirt featuring a bold CRX GARMS logo graphic on the chest. | CROOKSLDN black t-shirt featuring a bold CRX GARMS logo graphic on the chest. |
| Image 2 alt | CROOKSLDN white premium cotton t-shirt featuring a black and gold CRX GARMS logo graphic on the chest | CROOKSLDN white t-shirt featuring a black and gold CRX GARMS logo graphic on the chest |
| crooks.fabric | Premium cotton | cleared |
| shopify.fabric | Cotton | cleared |

## C4 — CRXST★RZ T-SHIRT (`gid://shopify/Product/10837911503191`)

| Field | Before | After |
|---|---|---|
| SEO title | CRXSTARZ T-Shirt — CROOKS Logo Cotton Tee \| CROOKSLDN | CRXSTARZ T-Shirt — CROOKS Logo Tee \| CROOKSLDN |
| SEO description | CRXST★RZ tee in cotton, with the outlined CROOKS wordmark and red star across the chest. In black or white. | CRXST★RZ tee with the outlined CROOKS wordmark and red star across the chest. In black or white. |
| crooks.fabric | Cotton | cleared |

The description ("CRXST★RZ tee — Wokstar energy only.") and both alt texts make no fabric claim, so they are unchanged.

## C5a — BLACK/BLUE MOTIONTEC™️ SOCKS (`gid://shopify/Product/10787430367575`)

| Field | Before | After |
|---|---|---|
| Description, para 1 | MotionTec™ socks in black and blue — cotton blend, reinforced heel, made for constant movement. | MotionTec™ socks in black and blue — reinforced heel, made for constant movement. |
| SEO description | MotionTec socks in black and blue. Cotton blend with a reinforced heel, made for constant movement. Single pairs or packs of 3, 6 or 12. | MotionTec socks in black and blue, with a reinforced heel, made for constant movement. Single pairs or packs of 3, 6 or 12. |
| crooks.fabric | Cotton blend, reinforced heel | cleared |
| shopify.fabric | Cotton | cleared |

## C5b — WHITE/RED MOTIONTEC™️ SOCKS (`gid://shopify/Product/10837189853527`)

| Field | Before | After |
|---|---|---|
| Description, para 1 | MotionTec™ socks in white and red — cotton blend, reinforced heel, made for constant movement. | MotionTec™ socks in white and red — reinforced heel, made for constant movement. |
| SEO description | MotionTec socks in white and red. Cotton blend with a reinforced heel, made for constant movement. Single pairs or packs of 3, 6 or 12. | MotionTec socks in white and red, with a reinforced heel, made for constant movement. Single pairs or packs of 3, 6 or 12. |
| crooks.fabric | Cotton blend, reinforced heel | cleared |
| shopify.fabric | Cotton | cleared |

## C6–C8 — OG JEANS 14oz (`gid://shopify/Product/10837667086679`)

Every other denim product already states 14oz. OG Jeans counts as jeans.

| # | Field | Before | After |
|---|---|---|---|
| C6 | crooks.fabric | Heavyweight denim | 14oz denim |
| C7 | Description | `<p><span><strong>OG jeans</strong>, built for structure and everyday wear.</span><span><br></span><span>Heavyweight denim with a baggy, stacked fit.</span></p>` | `<p><span><strong>OG jeans</strong>, built for structure and everyday wear.</span><span><br></span><span>Heavyweight 14oz denim with a baggy, stacked fit.</span></p>` |
| C8 | SEO description | OG Jeans in heavyweight denim with a baggy, stacked fit that holds its structure. White handcuff graphic on the back pockets. | OG Jeans in heavyweight 14oz denim with a baggy, stacked fit that holds its structure. White handcuff graphic on the back pockets. |

The SEO title "OG Jeans — Heavyweight Baggy Stacked Denim | CROOKSLDN" and the alt texts are unchanged; adding 14oz there would read as stuffing.

---

## After writing

- Re-read each product in Admin and confirm every field matches the "After" column.
- Open each product page on crooksldn.com and check how the theme handles a cleared crooks.fabric: the row should hide, not show an empty label. The theme belongs to the theme session, so report it there if the row shows empty; don't fix it from here.
