# Changes

**No live changes.** This workstream has not posted, submitted, contacted, created or edited anything outside this repository.

It has not touched:
- Shopify
- Trustpilot
- crooksldn.com
- LinkedIn
- Crunchbase
- any outlet

Access was read-only throughout:
- public Trustpilot pages
- Shopify fulfilment analytics
- Companies House
- the crooksldn.com policy pages
- public outlet pages

## 16 Oct 2026 (evening) — Second-pass authority research prepared

**State:** PREPARED

**Affected:**
- `09-authority-research.md`, a session output file sent to George.
- It was not written to `seo/cowork-results/`, because the project folder wasn't reachable from the session.

**Before:**  
Only the first pass existed (07-authority, 222 opportunities). There were no Trustpilot replies, no profile copy and no GEO source list.

**After:**  
The second pass contains:
- 47 scored targets and 8 journalist-request platforms;
- the Trustpilot audit, with 12 draft replies;
- Trustpilot, LinkedIn and Crunchbase copy;
- the GEO search-ranking proxy.

**Reason:**  
Fill the segments where the first pass hit search limits. Prepare the reputation and entity work George asked for.

**Target:** UK streetwear authority and mentions; the "best UK streetwear brands" and "brands like Corteiz" GEO answers; Trustpilot conversion.

**Validation:**
- Spot-checked the top contact routes and submission terms myself.
- Re-ran the score arithmetic (55 rows, 0 errors).
- Grepped for banned descriptors and for the excluded company name and number.

**Expected metric:** editorial mentions and links once outreach runs; Trustpilot response rate to negative reviews (currently 45%); citation share in the GEO panel.

## 18 Oct 2026, 16:40 — Research aligned with the 16 Oct brand rules; CSV export added

**State:** PREPARED

**Affected:**
- `workstreams/authority-research/artifacts/09-authority-research.md`
- `workstreams/authority-research/artifacts/authority-targets-second-pass.csv`

**Before:**
- Some angles relied on sending samples or seeding creators.
- The profile copy stated manufacturing origin.
- Disco and Streetwear Directory were listed as new targets.

**After:**
- **Text-only rescoring:** IndyBest, FashionBeans, Ape to Gentleman and Clash are re-scored for text-only pitches.
- **Parked rows (⏸):** 7 rows that depend on seeding or loans are marked parked.
- **Profile copy:** manufacturing origin removed. Free UK shipping over £30 and free size swaps added.
- **Disco and Streetwear Directory:** marked as approved 16 Oct and owned by the outreach workstream.
- **Reddit:** the note now reflects that Reddit seeding is off.
- **Trustpilot:** the 18 Oct re-check is recorded.
- **CSV:** the ranked list is exported for the merge.

**Reason:**  
George confirmed on 16 Oct, in the outreach and programme sessions:
- Pitches are text-only.
- Sample offers are declined and creator seeding is paused.
- Manufacturing origin stays out of consumer copy.
- No Reddit or poll seeding.

**Target:** same as above.

**Validation:**
- Score arithmetic re-run: 55 rows, 0 errors.
- Ranking re-sorted, and the section 4 cross-references updated to the new row numbers.
- Trustpilot re-read in Chrome on 18 Oct. It's unchanged: 80 reviews, 4.2, the same 21 low reviews, no new replies.

**Expected metric:** same as above.

## 18 Oct 2026, 16:45 — Workstream record created in GEO-SEO-WORK

**State:** PREPARED

**Affected:** branch `cowork/authority-research`, folder `workstreams/authority-research/`

**Before:**  
The repository was empty: no commits and no `main` branch.

**After:**  
The branch was created as an orphan, so nothing was committed to `main`. It holds STATUS, FINDINGS, CHANGES, NEXT and the artefacts. Once programme-records created `main` (README only), the branch was rebased onto it.

**Reason:** the programme protocol requires a durable record per workstream.

**Target:** programme coordination.

**Validation:** branch pushed and checked with `git ls-remote`. After the rebase, `git merge-base` confirms the branch now descends from `origin/main`.

**Expected metric:** n/a

## 18 Oct 2026, 17:20 — GEO panel citations mapped to targets

**State:** PREPARED

**Affected:**
- `workstreams/authority-research/artifacts/geo-cited-sources-vs-targets.md` (new)
- `artifacts/09-authority-research.md` §4
- `STATUS.md`, `FINDINGS.md` (Findings 10 and 11) and `NEXT.md`

**Before:**  
Task 4 had only a search-ranking proxy, because the GEO panel wasn't reachable.

**After:**  
The geo-measurement workstream's 16 Oct observed citations are mapped against this target list and 07's approved items. Two new domains were checked (Dripscan, Wings2Fashion) and an entity divergence was recorded (Crooks London Limited vs Crooks Clothing Company Ltd). The `cowork/geo-measurement` files were read only, not edited.

**Reason:** answer Task 4 with measured data instead of the proxy.

**Target:** GEO answers for "best UK streetwear brands" and "brands like Corteiz".

**Validation:**
- Counts were taken directly from `results.csv` (210 rows).
- The new domains were opened in Chrome: Dripscan's magazine and seller pages, the Wings2Fashion post, and Rosenberries.
- The Companies House officers page for 16396366 was read.

**Expected metric:** citation share and the CROOKSLDN mention rate for these prompts in the next GEO panel run, after the Streetwear Directory and Disco listings go live.


## 18 Oct 2026, 20:40 — George's answers applied; profile pack finalised; dedupe against 07

**State:** PREPARED

**Affected:**
- `artifacts/profile-pack-linkedin-crunchbase.md` (new)
- `artifacts/dedupe-vs-07.md` (new)
- `artifacts/09-authority-research.md` (§0, §1.1, §2, §3, §4 cross-references)
- `artifacts/authority-targets-second-pass.csv` (new `in_07` column)
- `QUESTIONS.md` (answers filled in)
- `ANSWERS.md` (two reviewer first names replaced with reply dates)
- `FINDINGS.md` (resolution notes; Findings 12–14)

**Before:**
- Profile copy named a company still to be decided, with no founding date.
- The Trustpilot section held drafts and named reviewers.
- Targets were marked "check 07".

**After:**
- **Profile pack:** ready-to-paste LinkedIn and Crunchbase copy. It names Crooks Clothing Company Ltd only where a company is needed, has George as founder, trading since March 2024, the approved description verbatim, Black Convict as the core colourway, and no other people or details.
- **Trustpilot section:** marked as done by `cowork/trustpilot` (replies posted, profile renamed), with every reviewer name removed.
- **Dedupe:** every target carries its 07 ID or "new" (21 new, 26 overlap).
- **GRM Daily:** rescored (G 5→2) after its site was found offline.
- **The Tab:** tips route verified.

**Reason:** George's answers of 18 Oct 2026 (`ANSWERS.md`), and owner decision #16 (no names tied to reviews, no exact order counts in the public repo).

**Target:** entity consistency (LinkedIn, Crunchbase); a clean merge into 07.

**Validation:**
- Shopify read-only check of Black Convict stock.
- Companies House re-read.
- crooksldn.com fetched (password page).
- GRM Daily and The Tab checked in Chrome.
- Grepped every file in this folder for reviewer names (none left) and exact order counts (none).
- Score arithmetic re-run by `table_tool.py`.

**Expected metric:** n/a until the profiles are live. Then: whether AI brand answers name Crooks Clothing Company Ltd and stop citing other entities (next GEO panel run).
