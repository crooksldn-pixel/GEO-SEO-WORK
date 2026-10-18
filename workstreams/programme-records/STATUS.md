# Workstream: Programme records (change log, master queue, status report)

**Branch:** cowork/programme-records  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 20:45 BST  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Keep the programme's single record. That means `change-log.md` (every live change with a metric, a baseline, and review dates at 4 and 8 weeks), `master-queue.md` (the status of every queued item) and `status-report-2026-10-16.md` (dated updates for George). This is the only session that edits those three files. Other workstreams log their changes on their own `cowork/*` branches, and this session merges them into the record.

## Current state

The records are in [`records/`](../../records/) on this branch, and they're current to 20:50 BST on 18 Oct. George answered on 18 Oct ([ANSWERS.md](ANSWERS.md)). The files came from `cowork/project-files-import` (`1c98fb3`), were committed verbatim first (`2ce51cc`), and every edit since is its own commit.

All four briefed tasks are done. What's next depends on other workstreams logging live changes, and on the review dates (13 and 15 Nov, then 11 and 13 Dec).

## Completed

- **Q36:** Metric, Baseline value and review dates at 4 and 8 weeks on every live entry. That's C-001, C-002, C-006, C-007 and C-WS02-1, plus C-009, which went live on 18 Oct. C-003, C-004, C-005 and C-008 are marked not live. The old scores are labelled as historical, not evidence.
- **Master queue:**
  - done rows marked from the change log;
  - parked rows set to "Parked (George)", per `owner-decisions-2026-10-18.md`;
  - the Orderify row reads "keep; customers use it for order edits";
  - every status brought up to date from the eleven workstream branches.
- **Merge:**
  - IMP-1 to IMP-8 (international markets, shipping, HS codes), TP-1 and TP-2 (Trustpilot), and PD-1 to PD-7 (product data) added to the change log;
  - the other eight branches record no live change;
  - three 18 Oct changes nobody logged are recorded under Outside changes, from this session's Admin reads and other branches' findings: the new live theme, the password lock and the T-shirt Week tees.

  Branch commits read are in [artifacts/merge-register.md](artifacts/merge-register.md).
- **Status report:** a dated 18 Oct Update at the top, covering what went live, what was measured, and George's 10 remaining actions. Questions answered in owner-decisions aren't repeated.
- Earlier: created `main` with a README, and opened issue #1.

## Currently working on

`Nothing currently running.`

## Blockers

None.

## Waiting on George

1. Set the GitHub default branch to `main` (Settings > General > Default branch).

The programme's other George actions are listed once, in the status report's 18 Oct Update.

## Waiting on external systems

- Workstreams logging the changes they make next. Expected entries: the next live-theme publish, the collections Sweats/Denim changes, redirects and contact page, the live-site-checks policies, the Merchant Center duplicate delete and seller name, and George's own admin actions.
- The store reopening after the 18 Oct password lock (date not recorded).
- The 14 Nov Search Console read (`cowork/search-console`), which feeds the 4-week reviews.

## Next actions

1. Merge each newly logged live change into the change log, with its Q36 fields.
2. Record the reopen date when it's known, and keep lock days out of every review.
3. 4-week reviews: Fri 13 Nov (the 16 Oct entries) and Sun 15 Nov (the 18 Oct entries), using search-console's 14 Nov read and Shopify.
4. 8-week reviews: Fri 11 Dec and Sun 13 Dec.

## Expected impact

**Commercial:** Low  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** High

No change here moves rankings by itself. A metric, a baseline and a review date on every live change is what will show which changes worked, and it stops deploys being reported as results.
