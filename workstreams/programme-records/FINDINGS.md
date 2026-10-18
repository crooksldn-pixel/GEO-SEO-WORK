# Findings

## Finding 1 — The Project folder can't be reached from Cowork sessions

**Finding:**  
Briefs tell Cowork sessions to read from, and write results to, `/mnt/project-files/seo/`. That path exists only inside the claude.ai Project. This session can't see it, and on 16 Oct the theme-editor, collections, products and authority-research sessions also reported that they couldn't. They put their results in local files or chat instead.

**Evidence:**  
This session's checks on 16 and 18 Oct: the workspace mounts, George's linked Mac (no folder connected), Google Drive search and GitHub. The other sessions' reports come from their chat summaries of 16 Oct.

**Why it matters:**  
Results that were meant for `cowork-results/` may never have arrived there, so the change log may be missing work done on 16 Oct. Any "done" status in the master queue needs checking against the sessions that did the work.

**Confidence:**  
High for this session. Medium for the other sessions, because that comes from chat summaries rather than their files.

**Recommended action:**  
Treat this repo as the shared record. Have each workstream put its 16 Oct results in `CHANGES.md` on its own branch, so they can be merged into the change log with evidence attached. Issue #1 tracks the record files.

## Finding 2 — The default branch is not `main`

**Finding:**  
`cowork/geo-measurement` was pushed at 16:37 UK on 18 Oct, before `main` existed, and GitHub made it the default branch. This session created `main` at 16:39 (README only). Neither `cowork/geo-measurement` nor `cowork/authority-research` (an orphan branch) shares history with `main`. `cowork/product-data` has rebased onto `main`.

**Evidence:**  
`git ls-remote --symref origin` shows `HEAD -> refs/heads/cowork/geo-measurement`. Changing the default through this session's proxy was refused ("Repository settings writes are not permitted").

**Why it matters:**  
A new session that clones without naming a branch starts on `cowork/geo-measurement` and could build on that workstream's files. Merging either unrelated branch into `main` later needs `--allow-unrelated-histories`, or that workstream has to rebase onto `main`.

**Confidence:**  
High.

**Recommended action:**  
George switches the default branch to `main` in GitHub settings. The geo-measurement and authority-research workstreams rebase onto `main` when convenient.

## Finding 3 — The repo is public

**Finding:**  
GEO-SEO-WORK is public. George decided on 18 Oct to keep it that way.

**Evidence:**  
The GitHub repository listing shows `"private": false`, and anonymous `git clone` works.

**Why it matters:**  
Anything committed here can be read by anyone. That includes the Shopify 90-day baselines once `10-measurement.md` is committed, plus the change log, George's action list and any outreach targets.

**Confidence:**  
High.

**Recommended action:**  
Nothing further. It is recorded so that no workstream commits credentials, customer data or order data here.

## Finding 4 — The first captured GEO measurement exists

**Finding:**  
`cowork/geo-measurement` holds a dated UK GEO panel run from 16 Oct 2026: 21 queries across Google UK, ChatGPT, Gemini and Perplexity, with `results.csv` (210 rows), the method, and 223 screenshots. Crooks is named only on brand queries, and in none of the 110 readable non-brand AI answers. Gaps: Perplexity is 5 of 63 runs (sign-up wall), and Google UK is 16 of 21 queries (gap-fill under way).

**Evidence:**  
`cowork/geo-measurement`: `workstreams/geo-measurement/artifacts/runs/2026-10-16/summary.md`, `results.csv`, `meta.json`, `panel-method.md`.

**Why it matters:**  
This is the baseline any GEO claim in the change log has to be checked against. It replaces GEO 43/50/54, which had no recorded method.

**Confidence:**  
High. These are counts from the committed CSV.

**Recommended action:**  
When merging into the change log, use this run as the GEO baseline for every live change that targets AI answers. Keep Perplexity out of any comparison until a full run exists. Authority-research's §4 is a search-ranking proxy written because this run wasn't available to it. The run's observed citation table should replace that proxy (see artifacts/merge-register.md, note 1).
