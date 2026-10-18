# Questions for George — collections workstream

**How to answer:** fill in each **Answer:** line and put any source text into `workstreams/collections/inputs/` under the filename given. Commit to `cowork/collections`, then tell the collections chat "answered".

**This repo is public.** Only paste text that is fine to be public: no manufacturing origin and no internal-only notes.

**Live edits need a typed "go".** Q1–Q6 and Q9 all change the live store. Once the collections session has read the answers, it will post the exact list of approved edits in its own chat and wait for George to type "go" there before saving anything. The session's permission check only accepts an approval typed in that chat, so a "yes" in this file isn't enough on its own.

The exact before and after for each edit is in `artifacts/proposed-changes.md`.

---

## Approvals

### Q1 — Task B: add an outfit line to /collections/denim

Add this as a new paragraph after the existing copy. The existing copy stays untouched.

```html
<p>Wear them with the <a href="/collections/sweats">Convict Hoodie</a> or a <a href="/collections/tees">graphic tee</a>.</p>
```

Yes / No

**Answer:**

### Q2 — Task B2: remove "made in Portugal" from /collections/denim

- Before: `The Yard pieces are made in Portugal; wash cold, inside out, and hang dry.`
- After: `Wash the Yard pieces cold, inside out, and hang dry.`

The brief says only to append to Denim, so changing existing text needs its own yes.

Yes / No

**Answer:**

### Q3 — Task C: link the fit guide from /collections/tracksuits

Add as the last paragraph:

```html
<p>Not sure on size? See <a href="/blogs/news/convict-vs-cellblock-fit">how the Convict and Cellblock fits compare</a>.</p>
```

The same sentence also goes into the Sweats copy as part of task A.

Yes / No

**Answer:**

### Q4 — Task D: answer "Is 550gsm heavy?" in the fit article

Replace the article's existing section "What 550gsm and 450gsm mean" with:

> **Is 550gsm heavy?**
> Yes. gsm is grams per square metre of fabric, and the Convict Hoodie and Convict Sweats are 550gsm, 100% cotton fleece: a heavy fabric, which is what gives them their structured hang. The Cellblock Crewneck and Shorts are 450gsm, so the Convict fabric is about 22% heavier, and the Cellblock is the one for layering or warmer days.

Yes / No / Yes with these edits: …

**Answer:**

### Q5 — Task E: reactive guide

Are sections 3 and 4 of `05-reactive-drafts.md` approved to publish?

- Section 3 is the Outerwear intro line.
- Section 4 is the guide, which would go live at `/blogs/news/reactive-outerwear`.

The text itself goes in via Q11.

Yes / No / Yes with these edits: …

**Answer:**

### Q6 — Task F: clean up the index

Each change is described in `artifacts/index-hygiene-audit.md`. Before creating any of them, the session will check the Search Console data from Q12 and flag any URL that still gets real clicks.

- a) Redirect 4 archived tees to `/collections/tees`: `og-crook-tee`, `3-clives-tee`, `broadcast-tee`, `evil-clive-tee`. Yes / No
- b) Redirect `/products/large-duffle-bag` to `/collections/accessories`. Yes / No
- c) Hide `/collections/frontpage` from search with `seo.hidden = 1`. It stays published and isn't deleted; this is the same setting Sets already uses. Yes / No

**Answer:**

---

## Facts

### Q7 — Which wash were the old CB1 and CB2?

The existing redirects disagree:

- Jeans: CB1 goes to grey, CB2 goes to blue.
- Jorts: CB1 goes to blue, CB2 goes to grey.

Pick one:

- A) CB1 = grey and CB2 = blue. The two jorts redirects are wrong.
- B) CB1 = blue and CB2 = grey. The two jeans redirects are wrong.
- C) CB1 and CB2 didn't mean the same wash for jeans and jorts, so the current redirects are right.

**Answer:**

---

## Decisions

### Q8 — Leave /collections/sets as it is?

The recommendation is yes: no redirect and no change. Sets is already set to noindex and isn't in the sitemap, so it can't compete with Tracksuits. The reasoning is in FINDINGS, Finding 2.

Yes (leave it) / No (redirect anyway)

**Answer:**

### Q9 — Optional: also show the Cellblock Set in Sweats?

This isn't in the brief. It would change the Sweats rule to "Type = Sweats OR Title = CELLBLOCK SET". Today the Cellblock Set can only be found through Sets and ALL.

Yes / No

**Answer:**

---

## Files — put these in `workstreams/collections/inputs/`

### Q10 — Sweats copy for task A

Copy the "Sweats" section of `workstreams/01-collections-internal-linking.md` word for word, including the SEO title, meta and description, into `inputs/01-sweats-section.md`.

**Answer:** (committed? yes / no)

### Q11 — Reactive drafts for task E

Copy sections 3 and 4 of `workstreams/05-reactive-drafts.md` word for word into `inputs/05-reactive-drafts-s3-s4.md`.

**Answer:** (committed? yes / no)

### Q12 — Search Console data for task F

For each URL below, give clicks and impressions for the last 28 days and the last 3 months, with the date range used. Put them in `inputs/05-search-console-collections.md`. If the search-console workstream has already published `05-search-console.md`, give its branch and path instead.

- `/products/og-crook-tee`, `/products/3-clives-tee`, `/products/broadcast-tee`, `/products/evil-clive-tee`, `/products/large-duffle-bag`
- `/collections/frontpage`, `/collections/all`, `/collections/sets`
- `/products/cb1-wash-jeans`, `/products/cb2-wash-jeans`, `/products/cb1-wash-jorts`, `/products/cb2-wash-jorts`
- Also, if available: the top queries for `/collections/sweats`, so the session can judge whether to change the H1 to "Heavyweight Sweats".

**Answer:**
