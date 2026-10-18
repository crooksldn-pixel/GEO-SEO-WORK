# Merge register

This lists each workstream branch reviewed for the change log. Only work a branch's `CHANGES.md` marks LIVE becomes a change-log entry. PREPARED and STAGED work goes into the master queue as a status instead.

`change-log.md` and `master-queue.md` aren't reachable yet (issue #1), so nothing below has been written into them. This register is what will be applied when they arrive.

## Reviewed 18 Oct 2026, 16:55 UK

| Branch | Commit reviewed | Cut from `main`? | Live changes | Change-log entries to add | Master-queue status to record |
|---|---|---|---|---|---|
| `cowork/geo-measurement` | `eca2845` (18 Oct 16:37) | No (pushed before `main` existed) | None. Research only. | None. Record the 16 Oct run as the programme's GEO baseline. | GEO baseline measured 16 Oct 2026. ChatGPT 63/63 runs, Gemini 63/63, Google UK 16/21 queries, Perplexity 5/63 (sign-up wall). Google UK gap-fill running. |
| `cowork/product-data` | `239cb27` (18 Oct 16:40) | Yes | None. One write (Cream Cap off Google & YouTube, 16 Oct 20:29) was refused by the connector before it reached Shopify. | None | Audit done (25 active products). Items A–K prepared with exact before/after values. Every write waits on George's yes in that chat. |
| `cowork/authority-research` | `7740cd5` (18 Oct 16:40) | No (orphan branch) | None. Nothing posted, submitted or contacted. | None | Second-pass research prepared: 47 scored targets, 8 journalist-request platforms, Trustpilot audit with 12 draft replies, and Trustpilot, LinkedIn and Crunchbase copy. External actions sit with George or the outreach workstream. |

**Result so far:** no workstream has reported a live change on its branch. When `change-log.md` arrives, these three branches add no change-log entries. Their status goes into the master queue only.

## Cross-workstream notes

1. **The GEO panel exists, but authority-research hasn't used it.** Authority-research §4 and its Blocker 1 say no panel runs were available, so it reported a search-ranking proxy. The real 16 Oct run is on `cowork/geo-measurement` at `workstreams/geo-measurement/artifacts/runs/2026-10-16/`. Its "Sources the AI answers cite most" table is observed citation data. For example, phrasestudios.com was cited in 25 AI runs and streetwear.directory in 9. That table can replace the proxy.
2. **Several workstreams are missing files from the same Project folder:**
   - this workstream: `change-log.md`, `master-queue.md`, the status report and `10-measurement.md`;
   - product-data: `05-reactive-drafts.md`, `assets/README.md` and the photo inbox;
   - authority-research: `07-authority.md`.

   All are listed in issue #1, so George has one place to answer.
3. **No owner for the contact-page copy.** Authority-research found "run out of London" on crooksldn.com/pages/contact. It should read "independent British streetwear brand". No workstream branch owns site page copy yet.
4. **Two branches don't share history with `main`:** `cowork/geo-measurement` and `cowork/authority-research`. Whoever merges them will need `--allow-unrelated-histories`, or the workstream rebases onto `main` first. `cowork/product-data` has already rebased.
