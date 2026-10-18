# Changes

This workstream is measurement only. It has changed nothing on crooksldn.com, Shopify, product data, feeds, Merchant Center, external profiles or any account. Panel runs are measurements, so they are recorded in `STATUS.md` and `artifacts/runs/`, not here.

The only change it has made is to this repository, below.

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
