# Next

## Do next

1. When issue #1 is answered, read the four record files: `change-log.md`, `master-queue.md`, `status-report-2026-10-16.md` and `workstreams/10-measurement.md`.
2. Q36 in `change-log.md`. For each live entry (C-001, C-002, C-006, C-007, C-WS02-1), add:
   - Metric
   - Baseline value: the Shopify 90-day baseline from `10-measurement.md`, or "no baseline: Search Console pending"
   - Review at 4 weeks: deploy date + 28 days
   - Review at 8 weeks: deploy date + 56 days

   Mark C-003, C-004, C-005 and C-008 not live.
3. In `master-queue.md`:
   - mark done whatever the change log shows as done
   - mark parked items "Parked (George)"
   - change the Orderify row to "keep; customers use it for order edits"
4. For each `cowork/*` branch, merge `CHANGES.md` into `change-log.md` as new entries. Each entry gets baseline, change, reason, URLs, target queries, deploy date, expected result, observed result and next action. Then update queue status. Leave the branches' own files unchanged.
   - `cowork/geo-measurement` has no `CHANGES.md`, because it is research only. Record its 16 Oct run as the GEO baseline, not as a change.
5. Add a dated Update section at the top of `status-report-2026-10-16.md`: what went live, what was measured, and George's remaining actions. Don't repeat questions he has already answered.

## Do not do yet

- Don't edit any record file from memory or from chat summaries. The dates and baselines have to come from the files.
- Don't merge anything into `main`. That is the orchestrator's call.
- Don't edit another workstream's files.

## Decisions still required

- Listed with defaults in [WAITING-ON-GEORGE.md](WAITING-ON-GEORGE.md). When George says "answered", read `ANSWERS.md`, the `records/` folder (or `cowork/project-files-import`) and issue #1, then start at step 1. Use the stated default for anything left unanswered.

## Data still required

- Deploy dates for C-001, C-002, C-006, C-007 and C-WS02-1 (in `change-log.md`).
- Shopify 90-day baselines (in `workstreams/10-measurement.md`).

## Recommended follow-up date

19 Oct 2026: check issue #1 and any new `cowork/*` branches. The 4-week and 8-week review dates follow from the deploy dates once they're in hand.

## Rules in force

These come from George's brief to the records session, 16 Oct 2026.

- Never record a ranking, traffic or GEO improvement without a captured measurement. A deploy is not proof.
- GEO 43/50/54 and SEO health 70/74 have no recorded method. Keep them only as labelled historical figures and never cite them as evidence.
- Facts in force: all products made in China; hoodies and joggers 550gsm 100% cotton; crewnecks and shorts 450gsm; jeans and jorts 14oz; tees print on demand; barcodes stay in Shopify; P1 theme copy on hold; About not approved; reviews hidden; samples declined; Orderify kept (customers use it for order edits); sameAs = site, Instagram and TikTok only.
