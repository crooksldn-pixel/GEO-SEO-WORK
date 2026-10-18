# Changes

This workstream changes the record files in `records/` and this repo only. It hasn't changed Shopify, any theme, Merchant Center or any external site. Its Shopify access was read-only: theme list and tee products, 18 Oct, 19:17–19:22 UTC.

## 18 Oct 2026, 20:17–20:40 BST — Records brought up to date from George's answers

**State:** LIVE (on this branch)

**Affected:**
- `records/change-log.md`
- `records/master-queue.md`
- `records/status-report-2026-10-16.md`
- `records/README.md`
- `artifacts/merge-register.md`

**Before:**  
The three files existed only in the Project folder, last updated 18 Oct 17:20 UTC (C-009). No live entry had a metric, baseline or review date. The queue still showed resolved items as blocked. The status report's last update was 16 Oct 18:35 UTC.

**After (one commit each):**
- `2ce51cc`: verbatim copy from `cowork/project-files-import` `1c98fb3`.
- `ea3b529`: Q36. Metric, Baseline value and review dates at 4 and 8 weeks on C-001, C-002, C-006, C-007, C-WS02-1 and C-009. C-003, C-004, C-005 and C-008 marked not live. Old scores labelled historical.
- `b8c31bc`: queue done and parked rows, and Orderify "keep; customers use it for order edits".
- `fd93547`: IMP-1 to IMP-8, TP-1 and TP-2 merged; 18 Oct outside changes recorded; queue statuses updated from all eleven branches.
- `a0ec9b3`: dated 18 Oct Update at the top of the status report. Also recorded what the 18 Oct evening live theme shipped (from `cowork/live-site-checks` FINDINGS 12).
- Next commit: PD-1 to PD-7 merged (product-data logged them at 20:28 BST). Cream Cap, footer and outreach-draft statuses updated, and George's action list corrected: the Cream Cap item is dropped; the store description, ReStock, sending the drafts and a theme backup are added.

**Reason:**  
George's brief to this session (16 Oct, tasks 1–4) and his answers of 18 Oct.

**Target:**  
A measurable record for every live change.

**Validation:**
- Review dates computed in code (deploy date + 28 and + 56 days).
- Every queue row checked for 11 cells.
- The remote branch was checked as unchanged before each push, and read back about 10 s after.
- An independent agent check of the records diff (`2ce51cc`..`a0ec9b3`) against its sources was started at 20:40 BST. Its result will be recorded here.

**Expected metric:**  
None directly.

**Deviation from my default 8:** Q19 (review display) and Q28 (samples/seeding) are marked Parked (George), as well as showing the decision, because `owner-decisions-2026-10-18.md` lists them as parked. That file is the source of truth.

## 18 Oct 2026, 16:39 UK — Created `main` with a README

**State:** LIVE

**Affected:**
- GEO-SEO-WORK: new branch `main`, with `README.md` only

**Before:**  
The repo had no `main`. Its only branch was `cowork/geo-measurement`, which became the default.

**After:**  
`main` exists with a README setting out the branch rules, the records workstream and the evidence rule.

**Reason:**  
The protocol has every workstream branch from `main`. George approved this session setting it up (18 Oct).

**Target:**  
Repo setup.

**Validation:**  
`git push` succeeded and `git ls-remote` lists `refs/heads/main`. The default branch is still `cowork/geo-measurement`; this session couldn't change it.

**Expected metric:**  
None.

## 18 Oct 2026, 16:40 UK — Opened issue #1

**State:** LIVE

**Affected:**
- GEO-SEO-WORK issue #1: the four record files the records session needs

**Before:**  
No issue existed.

**After:**  
Issue #1 is assigned to `crooksldn-pixel`.

**Reason:**  
George asked for the missing files to be logged as an issue (18 Oct).

**Target:**  
Unblock Q36 and the records work.

**Validation:**  
The issue URL was returned by the GitHub API.

**Expected metric:**  
None.

At 16:58 a comment was added to issue #1 listing the files product-data and authority-research also need from the Project folder.
