# Workstream: Programme records (change log, master queue, status report)

**Branch:** cowork/programme-records  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:20 UK  
**Priority:** P1  
**Overall status:** BLOCKED

## Objective

Keep the programme's single record. That means `change-log.md` (every live change with a metric, a baseline, and review dates at 4 and 8 weeks), `master-queue.md` (the status of every queued item) and `status-report-2026-10-16.md` (dated updates for George). This is the only session that edits those three files. Other workstreams report on their own `cowork/*` branches, and this session merges their results into the record.

## Current state

No record file has been edited. The three record files and `workstreams/10-measurement.md` are in the Project folder (`/mnt/project-files/seo/`). This session can't reach that folder, and nor can the other Cowork sessions. Issue #1 asks for the files.

The repo now has `main` (README only) and nine workstream branches: `cowork/geo-measurement`, `cowork/product-data`, `cowork/authority-research`, `cowork/collections`, `cowork/live-site-checks`, `cowork/search-console`, `cowork/merchant-center`, `cowork/outreach` and this one. The GitHub default branch is still `cowork/geo-measurement`, because that branch was pushed before `main` existed.

All eight other branches were reviewed by 17:15. None reports a live change, so none adds a change-log entry. Their status for the master queue, and nine cross-workstream notes, are in [artifacts/merge-register.md](artifacts/merge-register.md). Note 5 matters for Q36: Search Console has no data for 23 Jul – 14 Oct 2026.

## Completed

- Audited: searched for the record files in this session's workspace, on George's linked Mac (no folder connected), in Google Drive and in every `crooksldn-pixel` GitHub repo. They weren't found anywhere this session can reach.
- Set up the repo: created `main` with a README describing the branch rules (George approved this on 18 Oct).
- Opened issue #1 for the missing record files. Added a comment that gathers the other workstreams' missing Project files into the same issue.
- Read `cowork/geo-measurement`: it holds the 16 Oct 2026 UK GEO panel baseline. This is the first captured GEO measurement in the programme (see FINDINGS, Finding 4).
- Reviewed `cowork/geo-measurement`, `cowork/product-data`, `cowork/authority-research`, `cowork/collections`, `cowork/live-site-checks`, `cowork/search-console`, `cowork/merchant-center` and `cowork/outreach` for change-log entries. None has a live change. Recorded the commits reviewed, the master-queue status for each, and the cross-workstream notes in `artifacts/merge-register.md`.

## Currently working on

`Nothing currently running.`

## Blockers

### Blocker 1 — Record files not reachable (issue #1)

**Blocking:** Q36 (adding metric, baseline and review dates to C-001, C-002, C-006, C-007 and C-WS02-1, and marking C-003, C-004, C-005 and C-008 not live), the master-queue tidy-up, merging workstream changes, and the status-report update  
**Needs:** `change-log.md`, `master-queue.md`, `status-report-2026-10-16.md` and `workstreams/10-measurement.md`, committed to this branch under `records/` or attached to the records chat  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** None. Editing from memory or chat summaries would put unverified deploy dates and baselines into the record.

## Waiting on George

All of it is in [WAITING-ON-GEORGE.md](WAITING-ON-GEORGE.md), with a default for every decision. In short:

1. The four record files, plus anything in `cowork-results/` (issue #1).
2. Six decisions (Q36 metric, Search Console baseline wording, parked rows, where records live, answers given since 16 Oct, page-copy owner). Each has a default.
3. Switch the repo's default branch to `main`.

## Waiting on external systems

- More workstreams pushing their branches. There's no theme branch yet, and search-console hasn't pushed its STATUS or FINDINGS.

## Next actions

1. Q36 in `change-log.md`. For C-001, C-002, C-006, C-007 and C-WS02-1, add Metric, Baseline value (the Shopify 90-day baseline from `10-measurement.md`, or "no baseline: Search Console pending"), and Review at 4 weeks and Review at 8 weeks counted from each deploy date. Mark C-003, C-004, C-005 and C-008 not live.
2. `master-queue.md`: mark done whatever the change log shows as done, mark parked items "Parked (George)", and change the Orderify row to "keep; customers use it for order edits".
3. Merge each `cowork/*` branch's `CHANGES.md` into `change-log.md` as new entries, and update queue status to match. Record the 16 Oct GEO panel as the GEO baseline.
4. Add a dated Update section at the top of the status report: what went live, what was measured, and George's remaining actions.

## Expected impact

**Commercial:** Low  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** High

No change here moves rankings by itself. A metric, a baseline and a review date on every live change is what will show which changes worked, and it stops deploys being reported as results.
