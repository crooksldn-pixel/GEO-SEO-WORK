# Findings

Evidence comes from Shopify Admin GraphQL reads on 16 Oct 2026, 20:31 BST and 18 Oct 2026, 16:30 BST, unless stated otherwise. Product IDs are `gid://shopify/Product/…`.

## Finding 1 — "Cotton" is claimed on tees, socks and the Cellblock Shorts

**Finding:**
George's confirmed rule (16 Oct) limits the cotton claim to hoodies and joggers. Six products break it:
- CROOKS EXPRESS TEE (10642177786199) says "cotton".
- CRX GARMS T-SHIRT (10837626683735) says "premium cotton".
- CRXST★RZ T-SHIRT (10837911503191) says "cotton".
- Both MotionTec socks (10787430367575, 10837189853527) say "cotton blend".
- CHARCOAL CELLBLOCK SHORTS (10967990010199) carries Cotton in `shopify.fabric`.

The claims sit across descriptions, SEO titles, SEO descriptions, alt text, `crooks.fabric` and `shopify.fabric`.

**Evidence:**
Product reads on both dates, with no change between them. The field-by-field list is in [artifacts/c-fabric-claim-fixes.md](artifacts/c-fabric-claim-fixes.md).

**Why it matters:**
`shopify.fabric` feeds Google's material attribute, and SEO titles and descriptions are what search snippets and AI answers quote. An unconfirmed composition claim can end up repeated as fact in Shopping listings and in generated answers about the brand.

**Confidence:**
High that the claims fall outside the confirmed facts. Unknown whether the products actually are cotton.

**Recommended action:**
Apply C1–C5 (word removal only, no new claims) on George's yes. If George later confirms a composition as a new fact, restore it in the same fields.

## Finding 2 — OG Jeans is the only denim product without 14oz

**Finding:**
OG JEANS (10837667086679) says "heavyweight denim". Both Yard jeans and both Yard jorts say 14oz, and OG Jeans counts as jeans.

**Evidence:**
`crooks.fabric` = "Heavyweight denim". Neither the description nor the SEO description mentions oz.

**Why it matters:**
It's an inconsistent spec across the denim line, and it misses a concrete fact that the other four products already carry in their snippets.

**Confidence:**
High.

**Recommended action:**
Apply C6–C8 on George's yes.

## Finding 3 — The three jeans size charts are a copy of the Convict Sweats chart

**Finding:**
`crooks.measurements` on BLUE WASH YARD JEANS (10890058203479), GREY WASH YARD JEANS (10890055680343) and OG JEANS (10837667086679) matches the Convict Sweats chart value for value:
- waist 76.2 / 81.3 / 86.4 / 91.4 / 96.5cm
- inseam 73.7–81.3cm
- leg opening 45.7–55.9cm

**Evidence:**
16 Oct read of `crooks.measurements` on all six products. The jorts have their own chart (hip, thigh and length columns) and aren't affected.

**Why it matters:**
Customers size from this chart. A sweatpant chart on structured 14oz denim is a likely cause of wrong-size orders and swaps, and it gives Google and AI answers bad fit data.

**Confidence:**
High that it's copied. Not known how far the real measurements differ.

**Recommended action:**
George supplies the real denim measurements; this workstream writes them. Leave the current values until then rather than blanking the chart.

## Finding 4 — The Cream Cap is live on Google with no images or copy

**Finding:**
MAJOR LEAGUE CROOKS CAP (CREAM) (11236081402199) is ACTIVE with 0 media, an empty description and no SEO fields. It's published to all seven channels, Google & YouTube included.

**Evidence:**
The 18 Oct read shows the same state as 16 Oct.

**Why it matters:**
Google disapproves items without an image. While no photo exists, there's nothing for search or AI to describe on the product page.

**Confidence:**
High.

**Recommended action:**
Item A (unpublish from Google & YouTube only) as soon as George says yes in chat. Then J: photo first, then description and alt text, then republish to Google.

## Finding 5 — 11 products ship at 0g, including every set

**Finding:**
Every variant on these products has 0 weight:
- BLACK, GREY, PINK and CELLBLOCK SETS (125 variants)
- CRX GARMS and CRXST★RZ tees
- BLUE and GREY WASH YARD JORTS
- DOUBLE-AGENT PUFFA
- the Cream Cap
- WHITE/RED MOTIONTEC SOCKS

Separately, BLACK/BLUE MOTIONTEC SOCKS shows 20g on the 1-, 3-, 6- and 12-packs alike.

**Evidence:**
`inventoryItem.measurement.weight` on every variant, read 18 Oct.

**Why it matters:**
Weight-based shipping rates and Click & Drop labels price these at nothing, and Merchant Center uses shipping weight where a weight-based rate applies. Sets are the heaviest orders in the catalogue.

**Confidence:**
High on the zeros. The set and tee weights in the proposal are derived from their components.

**Recommended action:**
Approve the derived weights:
- Black and Grey Sets 1,700g, Pink Set 1,600g, Cellblock Set 1,450g
- both tees 250g

George supplies weights for the jorts, Puffa, cap and each sock pack.

## Finding 6 — Variant weights were changed outside this session on 17 Oct

**Finding:**
CHARCOAL CELLBLOCK CREWNECK went from 0 to 800g on 17 Oct at 20:42 BST, and PINK CONVICT SWEATS from 0 to 700g at 20:43 BST. This session made neither change. The Black and Grey Convict Sweats are 800g.

**Evidence:**
The 16 Oct variant read showed 0 on both. The 18 Oct read shows the new values. Product `updatedAt` is 17 Oct, 20:42 and 20:43 BST.

**Why it matters:**
The brief makes this session the only writer for products, variants and inventory items. A second writer risks overwriting this workstream's changes or the other way round. 700g on one colour of the same garment may also be a typo.

**Confidence:**
High that the change happened outside this session. Unknown who made it (George in admin, an app, or another session).

**Recommended action:**
The orchestrator confirms who made the change. George confirms whether Pink Convict Sweats should be 700g or 800g. The Pink Set's proposed weight depends on the answer.

## Finding 7 — Tee stock is tracked and negative, and two preorder plans sit on one product

**Finding:**
All 30 tee variants track inventory while selling at zero (policy CONTINUE):
- CROOKS EXPRESS TEE: White XS −4, White M −4
- CRXST★RZ: Black S −2

The ReStock "preorder" selling plan is on all three tees and on PINK CONVICT SWEATS. That product also has the clive-preorders plan "Pre-order: expected to dispatch by 31 October", so it carries two preorder plans.

**Evidence:**
Variant `inventoryQuantity`, `inventoryPolicy` and `inventoryItem.tracked`, plus product `sellingPlanGroups`, read on both dates.

**Why it matters:**
Print-on-demand tees should never show negative stock or read as preorder. Brief item D says the theme marks them PreOrder in product schema. The ReStock plan triggers a "recurring/deferred purchase" notice at checkout.

**Confidence:**
High on the data. Medium on the checkout notice, which comes from the brief and hasn't been re-tested here.

**Recommended action:**
D2: switch tracking off on all 30 tee variants. I: remove the ReStock plan in the app (not by uninstalling), with George deciding whether the Pink Sweats are included.

## Finding 8 — No product has gender or age group, and the Puffa has no colour

**Finding:**
No active product has a target gender or age group, and neither `shopify.target-gender` nor `shopify.age-group` has a metafield definition in the store. Every product except DOUBLE-AGENT PUFFA (11236140417367) has `shopify.color-pattern`.

**Evidence:**
The product metafield definitions list (shopify namespace) and the 18 Oct product metafield reads.

**Why it matters:**
For apparel in the UK, Google Shopping requires gender, age group and colour. Missing them limits or blocks the items in Shopping.

**Confidence:**
High on the data.

**Recommended action:**
- D1: age group "adult" on all 25.
- E: per-product gender, once George has corrected the suggested list in [artifacts/01-product-data.md](artifacts/01-product-data.md).
- F: the Puffa colour once George names it.

The two category metafield definitions may need enabling first.

## Finding 9 — The store description is empty

**Finding:**
`shop.description` is "".

**Evidence:**
Shop reads on 16 and 18 Oct.

**Why it matters:**
Per the brief, this field feeds the Organization schema description. It's also used as the homepage meta description, so today the homepage has no brand description in schema and no controlled snippet. That last point is from Shopify's theme conventions and hasn't been verified on the live theme.

**Confidence:**
High that it's empty. Medium on the meta-description effect.

**Recommended action:**
Item B on George's yes, entered in Shopify admin via the browser. There's no API route.

## Finding 10 — Smaller metadata gaps

**Finding:**
- CHARCOAL CELLBLOCK CREWNECK (10967989944663) is the only product with copy that has no SEO title.
- BLACK/BLUE MOTIONTEC SOCKS has alt text that just repeats the product name in capitals ("BLACK/BLUE MOTIONTEC SOCKS").
- The DOUBLE-AGENT PUFFA description has a stray `<meta charset="utf-8">` inside its paragraph.
- HYDROCUFF WINDBREAKER has one image only, with no wet or reacted view.

**Evidence:**
18 Oct product reads.

**Why it matters:**
Small snippet-quality and accessibility losses. The HydroCuff gap means its main selling point isn't shown.

**Confidence:**
High.

**Recommended action:**
- Crewneck SEO title in the style of the other products, for example "Charcoal Cellblock Crewneck — 450gsm Fleece | CROOKSLDN", on George's yes.
- Socks alt: rewrite from the actual image.
- Puffa: clean up the HTML in the G rewrite.
- HydroCuff: covered by J.
