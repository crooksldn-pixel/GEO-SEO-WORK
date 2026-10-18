# Proposed changes — exact before / after

This file uses the per-change format the brief asks for in `cowork-results/02-collections.md`: baseline, exact change, approval and time, read-back, target query, metric. When the project folder is reachable, this is what goes there.

Nothing below is live. The approval and read-back fields are filled in only when a change is actually made, and the change is then logged in `../CHANGES.md`.

---

## A. /collections/sweats: SEO title, meta and description

- **Approval:** pre-approved 16 Oct 15:33 (C-003). Confirmed weights allowed since 18:26. George sees the final text before it goes in.
- **Blocked on:** the "Sweats" section of `workstreams/01-collections-internal-linking.md`, which isn't reachable from this session.
- **Baseline:** see `baselines-2026-10-18.md`. The current description contains "made in Portugal" (Finding 1), and the A rewrite removes it.
- **Build:** the 01 copy, plus "550gsm, 100% cotton" for the Convict pieces, "450gsm" for Cellblock, and the C fit-article sentence. The H1 stays "Sweats".
- **SEO title:** `Heavyweight Hoodies & Joggers | Baggy Fleece Sweats`. The theme appends ` | CROOKSLDN`, so it renders at 63 characters, and Google will probably cut off the brand suffix. That's acceptable, but flagged.
- **Target query:** heavyweight hoodies, heavyweight joggers, 550gsm hoodie, baggy fleece sweats.
- **Metric:** Search Console impressions, CTR and average position for `/collections/sweats` on those queries, comparing 28 days before and after.

## B. /collections/denim: append outfit links

- **Approval:** pre-approved (C-003), but the session's permission check needs George's yes in chat. The attempt on 16 Oct 20:40 was blocked before saving.
- **Baseline:** exact HTML in `baselines-2026-10-18.md`.
- **Change:** append a new paragraph after the existing one, leaving the existing paragraph byte-for-byte unchanged:

```html
<p>Wear them with the <a href="/collections/sweats">Convict Hoodie</a> or a <a href="/collections/tees">graphic tee</a>.</p>
```

- **Where:** Shopify admin UI (the API can't see Denim), collection 688184099159, in the description's HTML view.
- **Target query:** baggy jeans. Denim and `/products/og-jeans` own this; the link moves Denim visitors on to Sweats and Tees.
- **Metric:** clicks from `/collections/denim` to `/collections/sweats` and `/collections/tees`.

## B2. /collections/denim: remove the "made in Portugal" clause (not in the brief)

- **Approval:** needs George's explicit yes. It goes beyond "append only".
- **Before:** `… a white handcuff graphic on the back pockets. The Yard pieces are made in Portugal; wash cold, inside out, and hang dry. Sizes XS to XL, with measurements in each size guide.</p>`
- **After:** `… a white handcuff graphic on the back pockets. Wash the Yard pieces cold, inside out, and hang dry. Sizes XS to XL, with measurements in each size guide.</p>`
- **Why:** Finding 1. The care instruction is kept and only the origin claim is dropped.
- **Metric:** none. This is a factual correction.

## C. Fit-article link from Tracksuits (and Sweats via A)

- **Approval:** needs George's yes.
- **Baseline:** the Tracksuits HTML in `baselines-2026-10-18.md`.
- **Change:** append to Tracksuits (collection 687058518359, via the Admin API):

```html
<p>Not sure on size? See <a href="/blogs/news/convict-vs-cellblock-fit">how the Convict and Cellblock fits compare</a>.</p>
```

- **Target query:** sizing and fit, e.g. "convict hoodie size" or "550gsm hoodie fit".
- **Metric:** sessions on `/blogs/news/convict-vs-cellblock-fit` whose previous page was Tracksuits or Sweats.

## D. Fit article: answer "is 550gsm heavy?"

- **Approval:** needs George's OK on this draft.
- **Approach:** rewrite the existing gsm section rather than add a second one, so the article doesn't explain gsm twice.
- **Before:**

```html
<h2>What 550gsm and 450gsm mean</h2>
<p>gsm is grams per square metre of fabric. At 550gsm, the Convict fabric is about 22% heavier than the Cellblock's 450gsm. That extra weight is what gives the Convict hoodie and sweats their heavy, structured hang. The Cellblock is lighter, for layering or warmer days.</p>
```

- **After:**

```html
<h2>Is 550gsm heavy?</h2>
<p>Yes. gsm is grams per square metre of fabric, and the Convict Hoodie and Convict Sweats are 550gsm, 100% cotton fleece: a heavy fabric, which is what gives them their structured hang. The Cellblock Crewneck and Shorts are 450gsm, so the Convict fabric is about 22% heavier, and the Cellblock is the one for layering or warmer days.</p>
```

- **Facts used:** 550gsm and 100% cotton for the Convict hoodie and joggers only; 450gsm for Cellblock. 550/450 = 1.22.
- **Where:** article `gid://shopify/Article/676342530391`, via the Admin API.
- **Target query:** "is 550gsm heavy", "550gsm hoodie", "what does gsm mean hoodie".
- **Metric:** article impressions and average position on gsm queries.

## E. Reactive guide

- **Blocked on:** George's approval of `workstreams/05-reactive-drafts.md` sections 3 and 4, which this session can't reach.
- **When approved:** publish at `/blogs/news/reactive-outerwear` (currently 404), add the section 3 intro line and a guide link to `/collections/outerwear`, and link the guide to `/products/hydrocuff-windbreaker` and `/products/double-agent-puffa`.

## F. Index hygiene

See `index-hygiene-audit.md`.

## G. /collections/sets

Recommendation: no redirect. See Finding 2.
