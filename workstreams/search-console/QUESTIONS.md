# Questions for George — search-console workstream

**Status: all answered or parked, 18 Oct 2026.** Answers below come from `ANSWERS.md` (George, 18 Oct 17:03 UTC).

**How to answer:** write each answer on its `Answer:` line in this file on branch `cowork/search-console` and commit, or put the answers in the chat message. Then send this session the word **answered**.

Things already requested elsewhere aren't repeated here. The programme change log (deploy dates for C-001, C-002, C-006, C-007, C-WS02-1) is in issue #1 for programme-records; this workstream reads it from the repo once it lands.

---

## Q1 — Is the Crooks Express tee the "Tesco tee"?

**Why I'm asking:** people search "crooks tesco shirt", "crooks tesco tee" and "crooks tesco": 238 UK impressions in Jan–Jul, rising from 52 to 186 half on half (FINDINGS 5). The two old pages, /products/white-tesco-tshirt and /products/black-tesco-tshirt, now return 404. The answer decides where the collections workstream redirects them.

**Options:**
- A. Yes, it's the same design → redirect both to /products/crooks-express-t-shirt
- B. No, the Tesco tee is no longer sold → redirect both to /collections/tees
- C. No, it's a different current product → name it, and both redirect there

**Answer:** A — yes, it's the Crooks Express tee. Redirect both old URLs to /products/crooks-express-t-shirt; collections owns the redirects. (George, 18 Oct 17:03 UTC; owner decision #21; `ANSWERS.md`.)

---

## Q2 — Does any other Google account have a Search Console property for crooksldn.com?

**Why I'm asking:** the property on team@crooksldn.com has no data for 23 Jul – 14 Oct 2026 (FINDINGS 1). The data before that gap means the site was verified somewhere until 22 Jul. If another account still holds a property, for example the account that set up the Shopify Google & YouTube channel or Merchant Center, or an older `https://crooksldn.com/` URL-prefix property, it may have the missing weeks. That would give a real pre-deploy baseline instead of two days.

**What to do:** in any other Google account used for the business, open search.google.com/search-console and check the property list for crooksldn.com.
- If one exists: add team@crooksldn.com as a user (Restricted is enough), and say which property it is.
- If none exists: say "none".

**Answer:** Parked. Not answered, and it blocks nothing. (`ANSWERS.md`.)

---

## Q3 — Drops, launches and password-gating between now and 14 Nov 2026

**Why I'm asking:** drops spike branded search; 14 Feb, 2 May and 4 Jul are the biggest days in the data. The store was also password-gated around the May and July drops, which sends brand searches to /password. The 7-day (16–22 Oct) and 28-day (16 Oct – 12 Nov) reads need those dates marked, or a drop will look like an SEO win or loss.

**Please give:**
- Date of any drop or product launch before 14 Nov (including T-shirt week going live, if planned)
- Whether the store will be password-gated, and for which dates
- Any paid or creator push that would lift brand searches, with dates

If nothing is planned, say "none planned".

**Answer:** T-shirt Week runs Monday to Sunday. Exact dates weren't given; the main chat says the 14 tees went live 18 Oct, so it's presumed to be Mon 19 – Sun 25 Oct. No other drops given. (Owner decision #24; `ANSWERS.md`.) Observed since: the whole store has been password-locked since the evening of 18 Oct (FINDINGS 13).

---

## Q4 — Should this workstream schedule its own follow-up checks?

**Why I'm asking:** the next Search Console reads depend on Google's data catching up (NEXT.md):
- 20 Oct: Indexing > Pages (still processing on 18 Oct)
- 24 Oct: first 7-day post-deploy read (16–22 Oct)
- 14 Nov: 28-day read

**Options:**
- A. Yes, set scheduled tasks in this session for those three dates. Each run is read-only and updates this branch.
- B. No, the main chat will tell this session when to run each check.

**Answer:** A — schedule them. Created on 18 Oct for 20 Oct 10:00 BST, 24 Oct 10:00 BST and 14 Nov 10:00 GMT (see NEXT.md). (`ANSWERS.md`.)
