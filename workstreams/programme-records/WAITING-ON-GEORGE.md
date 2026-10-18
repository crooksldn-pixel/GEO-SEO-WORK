# Waiting on George: programme records

**Last updated:** 18 Oct 2026, 17:20 UK

This is everything the records session needs from you. Answer it, then send **answered** in the records chat.

You can answer in any of these ways:
- Commit the files under `records/` on `cowork/programme-records`, and the answers in `workstreams/programme-records/ANSWERS.md`.
- Comment on issue #1.
- Paste the answers into the records chat.

Already answered, so not asked again: the repo stays public (18 Oct), and the records session set up `main` with your OK (18 Oct).

## A. Files (these block Q36, the queue tidy-up, the merge and the status update)

Commit them exactly as they are now in the Project folder `seo/`, without tidying first. I need the current text.

| # | File in the Project | Put it at |
|---|---|---|
| 1 | `change-log.md` | `records/change-log.md` |
| 2 | `master-queue.md` | `records/master-queue.md` |
| 3 | `status-report-2026-10-16.md` | `records/status-report-2026-10-16.md` |
| 4 | `workstreams/10-measurement.md` | `records/workstreams/10-measurement.md` |
| 5 | everything in `cowork-results/` | `records/cowork-results/` (if the folder is empty, say so) |

Easier option: commit the whole `seo/` folder as it is to a new branch, `cowork/project-files-import`, cut from `main`. I'll read my files from there. The same import also unblocks other workstreams that need files from that folder:
- product-data needs `05-reactive-drafts.md`, `assets/README.md` and the photos;
- collections needs `01-collections-internal-linking.md`, `05-reactive-drafts.md`, `05-query-map.md` and `p1-collection-audit-2026-10-16.md`;
- authority-research and outreach need `07-authority.md` and `07-directory-submission-pack.md`.

## B. Decisions (if you don't answer, I'll use the default shown)

**6. Q36 metric.** Suppose `change-log.md` and `10-measurement.md` don't name a metric for a live entry. Can I set one from the entry's own target, for example "UK organic clicks to /collections/sweats (Search Console)", and label it "metric set by records"?  
*Default:* yes.

**7. Search Console baseline.** Search Console has no data for 23 Jul – 14 Oct 2026 (see `cowork/search-console`). For entries with no Shopify 90-day baseline, there are two options:
- write only your 16 Oct wording, "no baseline: Search Console pending";
- also add the nearest Search Console figure (21 Jan – 22 Jul 2026), labelled "pre-gap, not like-for-like".

*Default:* your wording only.

**8. Parked rows.** Which master-queue rows become "Parked (George)"?  
*Default:* rows the queue already marks parked or on hold, plus P1 theme copy (on hold) and the About page (not approved). Rows for things you have already decided (reviews hidden, samples declined, Orderify kept) are marked with the decision, not parked.

**9. Where the edited records live.**  
*Default:* on `cowork/programme-records` under `records/`. The main chat copies them back to the Project folder or merges them when it chooses. Nothing goes to `main` from me.

**10. Questions already answered since 16 Oct.** The status-report Update must not repeat questions you've answered. If the main chat holds answers given after the 16 Oct report that aren't written in any of the files above, list them in `ANSWERS.md`.  
*Default:* I treat a question as answered only where the four files or a workstream branch show it as answered.

**11. Owner for site page copy.** crooksldn.com/pages/contact says "run out of London" (from `cowork/authority-research`), and no workstream owns page copy.  
*Default:* recorded in the queue as "owner unassigned".

## C. Physical action (no default)

**12.** In GitHub, go to Settings > General > Default branch and change it to `main`. It is still `cowork/geo-measurement` because that branch was pushed first, and this session can't change repo settings.
