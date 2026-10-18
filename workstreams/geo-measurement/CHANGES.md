# Changes

This workstream is measurement only. It has changed nothing on crooksldn.com, Shopify, product data, feeds, Merchant Center, external profiles or any account. Panel runs are measurements, so they are recorded in `STATUS.md` and `artifacts/runs/`, not here.

The only changes it has made are to this repository, below. Newest entries are first.

## 18 Oct 2026, about 20:30 UK — removed IP-based location and network detail from committed run files (owner decision #16)

**State:** LIVE

**Affected:**
- `artifacts/runs/2026-10-16/shots/gemini__*.png` (63 files)
- `artifacts/runs/2026-10-16/shots/google_uk__baggy-hoodie-uk__1_p2.png`
- `artifacts/runs/2026-10-16/shots/google_uk__heat-reactive-puffer__1.png`
- `artifacts/runs/2026-10-16/summary.md` and `artifacts/runs/2026-10-18/summary.md`
- The new `artifacts/runs/2026-10-18-extra-query/shots/gemini__*.png` (4 files), redacted before their first commit

**Before:**
- Every Gemini screenshot showed the location Gemini takes from the IP address, in the bottom-left sidebar, labelled "From your IP address".
- Two Google screenshots showed local-store pins naming nearby towns: an H&M result on the "baggy hoodie UK" page 2, and a Sponsored Products tile on "heat reactive puffer".
- Both run summaries named the mobile network.
- The project thread had already redacted the two `meta.json` files on 18 Oct (commit `c9eec84`). Those are not this workstream's change.

**After:**
- **Gemini:** the sidebar location box (x 0–178, y 1432–1468 of the 800×1500 image) is filled with the sidebar colour and labelled "location removed (#16)".
- **Google:** the two pins are filled with the surrounding colour: boxes (62,706)–(210,725) and (149,187)–(219,204).
- **Summaries:** they now say "UK (GB) connection".
- **Unchanged:** nothing that belongs to an answer or a result was changed.
  - Businesses' own published addresses quoted in answers are left as captured, such as the Bourne End returns office in the brand-query AI Overviews.
  - Answer text is left as captured.

**Reason:**
- Owner decision #16 (18 Oct): no IP or network details in the public repo; record the country only.
- ANSWERS.md, "Do now" 2: keep IP and location out of committed run files.

**Target:** Privacy of the measuring location in a public repository.

**Validation:**
- OCR (tesseract) of all 233 screenshots on this branch at the time found the location footer in 62 of 63 Gemini shots and the two Google pins. No other IP-derived or network text was found. The only other place names found are addresses quoted inside answers, which are left as captured. All 63 Gemini shots were redacted, including the one where OCR did not read the footer.
- A contact sheet of the 63 redacted footers was checked by eye.
- OCR of the 9 extra-query screenshots after redaction finds no location text.

**Expected metric:** None. Git history still holds the earlier versions. ANSWERS.md Q3 records the history as unchanged, and rewriting it would need a force-push and George's say-so.

## 18 Oct 2026, 16:50 UK — rebased `cowork/geo-measurement` onto `main`

**State:** LIVE

**Affected:**
- Branch `cowork/geo-measurement` on GitHub (force-pushed with lease)
- The commit hash recorded for this branch in `cowork/programme-records` → `artifacts/merge-register.md`

**Before:**  
An orphan branch at `eca2845`. It was pushed at 16:37 before `main` existed, so it shared no history with `main`.

**After:**
- `788cbb8`: the same baseline commit, now on top of `main` (`3905e37`).
- `b2260e2`: the 18 Oct gap-fill.

The workstream files are identical: `git diff eca2845 788cbb8 -- workstreams` is empty. The only new file is `main`'s README.md.

**Reason:**
- The workstream protocol says a branch must be cut from `main`.
- programme-records Finding 2 asked this workstream to rebase so that merging doesn't need `--allow-unrelated-histories`.

**Target:** Repository hygiene. The branch can now be merged into `main` normally.

**Validation:**
- `git merge-base origin/main cowork/geo-measurement` returns `3905e37`.
- `git diff eca2845 788cbb8 -- workstreams` is empty.

**Expected metric:** None. This changes no site, ranking or GEO metric.
