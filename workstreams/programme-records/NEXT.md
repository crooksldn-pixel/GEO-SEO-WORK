# Next

## Do next

1. **Merge new live changes.** Fetch every `cowork/*` branch, then for each new LIVE entry in a CHANGES.md add a change-log entry with:
   - baseline, change, reason, URLs and target queries;
   - deploy date, expected result, observed result and next action;
   - the Q36 fields: Metric, Baseline value, and review dates at 4 and 8 weeks.

   Use the branch's own ID if it suggests one (as IMP did). Otherwise use a short prefix (TP, PD), or `C-<slug>-n`. Expected soon:
   - the next live-theme publish;
   - collections' Sweats/Denim, redirects and contact page;
   - live-site-checks' policy edits;
   - Merchant Center's duplicate delete and seller name;
   - George's admin actions (store description, ReStock, checkout box).
2. **Update the master queue status** for every merged change. Then update `artifacts/merge-register.md` with the commit read for each branch.
3. **Store reopen.** When it's known, record the reopen date under Outside changes in the change log, and mark lock days as excluded in each review.
4. **4-week reviews:**
   - Fri 13 Nov: C-001, C-002 and C-007 (review these two together), C-006 and C-WS02-1;
   - Sun 15 Nov: C-009, IMP, TP and PD.

   For each one, fill an "Observed at 4 weeks" line from captured data only: Shopify M1, search-console's 14 Nov read, Merchant Center's 29 Oct export, and the GEO control re-run on 13 Nov. Label lock days and T-shirt Week.
5. **8-week reviews:** Fri 11 Dec and Sun 13 Dec, the same way.
6. **Each new George answer:** add a dated Update to the status report, and don't repeat answered questions.

## Do not do yet

- Don't record an improvement from a deploy alone, or from any period that includes lock days.
- Don't merge anything into `main`. That is the orchestrator's call.
- Don't edit another workstream's files.

## Decisions still required

- None for this workstream.

## Data still required

- The store reopen date.
- Who published the 18 Oct evening theme.

## Recommended follow-up date

19 Oct 2026, to pick up newly logged changes. Then 13 Nov 2026 for the first 4-week reviews.

## Rules in force

- Never record a ranking, traffic or GEO improvement without a captured measurement. A deploy is not proof.
- GEO 43/50/54 and SEO health 70/74 have no recorded method. Keep them only as labelled history.
- Re-read a file just before editing it, keep each edit small, and read it back after pushing.
- Public repo (decision #16): no revenue, exact order counts, private addresses, age or IP details.
- Owner decisions of 18 Oct are the source of truth (`project-files-import:project-files/seo/owner-decisions-2026-10-18.md`).
