# Findings

## Finding 1 — Live Sweats and Denim copy says "made in Portugal"

**Finding:**
The Sweats description says the Cellblock pieces are "450gsm brushed fleece in a relaxed cut with 3D embroidery, made in Portugal". The Denim description says "The Yard pieces are made in Portugal". Both break George's confirmed rule: consumer copy never states where the pieces are made, and never names Portugal. The Portugal claim is also factually wrong.

**Evidence:**
Live `/collections/sweats` and `/collections/denim`, read 16 Oct and again 18 Oct 16:40 BST. Admin collections 688184131927 and 688184099159. Exact text in `artifacts/baselines-2026-10-18.md`.

**Why it matters:**
It's a false origin claim on two indexed category pages. AI answers and shopping surfaces can quote it back as fact, and it contradicts the brand facts the other workstreams are publishing.

**Confidence:** High

**Recommended action:**
Sweats: task A replaces the whole description, which removes the claim. Denim: remove the clause, as drafted in `artifacts/proposed-changes.md`. This needs George's explicit yes, because the brief says to keep the Denim copy and only append.

## Finding 2 — /collections/sets is already noindex and out of the sitemap (answers task G)

**Finding:**
Sets can't compete with Tracksuits in search: it already carries `seo.hidden = 1`. Redirecting it would cost more than it gains.

**Evidence:**
- Collection 691325337943 has metafield `seo.hidden` = `1`.
- The live page outputs `<meta name="robots" content="noindex,nofollow">` and is absent from `sitemap_collections_1.xml`.
- It is in no menu and not linked from the homepage.
- The Cellblock Set (product type "Sets") sits only in Sets, one hidden internal collection and `/collections/all`. Sweats is a smart collection on Type = Sweats, so it would not pick the Cellblock Set up.

**Why it matters:**
The duplicate-intent concern in G doesn't apply to a noindexed page. A redirect only fires once `/collections/sets` stops resolving, which means unpublishing it from Online Store. That would take away the only themed collection the Cellblock Set lives in.

**Confidence:** High

**Recommended action:** Leave Sets as it is. No redirect.

## Finding 3 — Old CB1/CB2 redirects are crossed between jeans and jorts

**Finding:**
`cb1-wash-jeans` goes to grey and `cb2-wash-jeans` goes to blue. `cb1-wash-jorts` goes to blue and `cb2-wash-jorts` goes to grey.

**Evidence:** Admin API `urlRedirects`, 18 Oct. All four paths resolve with a 200 after the redirect.

**Why it matters:**
If CB1 and CB2 named the same wash across both lines, one pair sends old links, and whatever ranking they carry, to the wrong colourway.

**Confidence:**
High that the two pairs disagree. Unknown which pair is wrong. The brief already flags `cb2-wash-jorts`.

**Recommended action:**
George confirms which wash CB1 and CB2 were. Then edit the two wrong redirect targets; nothing needs deleting.

## Finding 4 — Five archived products 404, and one of them isn't a tee

**Finding:**
OG Crook Tee, 3 Clives Tee, Broadcast Tee, Money Clive Tee (`evil-clive-tee`) and Ballistic Nylon Duffle (`large-duffle-bag`, type Accessories) are archived. All five `/products/` URLs return 404.

**Evidence:**
Admin API products with `status:archived`, plus live URL checks on 18 Oct. `/collections/accessories` returns 200 with 4 products.

**Why it matters:**
The brief sends archived tees to `/collections/tees`. The duffle needs `/collections/accessories` instead.

**Confidence:** High

**Recommended action:**
Once the Search Console evidence lands, create five URL redirects: four to `/collections/tees` and the duffle to `/collections/accessories`. The full list is in `artifacts/index-hygiene-audit.md`.

## Finding 5 — /collections/frontpage is indexable and duplicates /collections/all

**Finding:**
`/collections/frontpage` returns 200, is self-canonical, has no robots meta, is listed in the sitemap and is titled `PRODUCTS | CROOKSLDN`. It holds 37 products and nothing on the site links to it.

**Evidence:**
Live storefront and `sitemap_collections_1.xml`, 18 Oct. Collection 678766281047. By contrast, `/collections/all` is the main-menu target, titled `Shop CROOKSLDN Streetwear | All Clothing`.

**Why it matters:**
It's a thin, generically titled page competing with the real all-products listing.

**Confidence:** Medium. Search Console will show whether it earns any clicks.

**Recommended action:**
Set `seo.hidden = 1` on frontpage, the same mechanism Sets already uses. That removes it from the sitemap and adds noindex without unpublishing or deleting it. Do it after the Search Console evidence, with George's yes.

## Finding 6 — Admin API can't see Sweats, Denim or Tees, by handle or by ID

**Finding:**
`collectionByHandle` and `collection(id:)` both return `null` for Sweats (688184131927), Denim (688184099159) and Tees (688184066391). The API only returns the stale `sweats-1` and `denim-1` duplicates.

**Evidence:** Admin API queries on 16 and 18 Oct. The IDs come from the storefront `/collections.json`.

**Why it matters:**
Any session editing these three has to use the Shopify admin UI, and should use these IDs to find them.

**Confidence:** High

**Recommended action:** None. This confirms the known quirk and records the IDs for other sessions.

## Finding 7 — Another session touched collections on 18 Oct

**Finding:**
Tracksuits, Outerwear and frontpage all show `updatedAt 2026-10-18T11:25:15Z`. Their descriptions and SEO fields are unchanged from 16 Oct.

**Evidence:** Admin API, 18 Oct 16:35 BST.

**Why it matters:**
A shared timestamp across three collections points to product-side activity, since editing a product bumps the collections it belongs to. There's no copy conflict. This workstream re-reads every value before it writes.

**Confidence:** Medium

**Recommended action:** The orchestrator can confirm which session ran at 12:25 BST on 18 Oct.
