# Merge register

This lists each workstream branch reviewed for the change log. Only work a branch's `CHANGES.md` marks LIVE becomes a change-log entry. PREPARED and STAGED work goes into the master queue as a status instead.

## Merged 18 Oct 2026, 20:30–20:50 BST, into `records/`

Re-read at 20:50: product-data (`462bc18`) logged 7 live changes, which are merged as PD-1 to PD-7. Outreach (`d5e942c`) created 2 Gmail drafts; they're prepared, not sent, and recorded in the queue as Q27. Theme-editor (`a32dcfa`) has still made no change, and notes the footer and tee wording are live through other sessions.

| Branch | Commit read | Live changes | Merged as |
|---|---|---|---|
| `cowork/international-markets-pricing` | `ab1ca33` | IMP-1, IMP-2, IMP-4, IMP-5, IMP-7, IMP-8 live; IMP-3 and IMP-6 in draft | change-log IMP-1 to IMP-8 |
| `cowork/trustpilot` | `d0d8536` | 12 replies posted; profile name, description and address | change-log TP-1, TP-2; queue Q23, Q24 |
| `cowork/geo-measurement` | `c0471b8` | None (measurement; branch rebased onto `main`) | queue Q35 (baseline measured) |
| `cowork/search-console` | `f7bd1f5` | None | queue Q30–Q33; password lock under Outside changes |
| `cowork/live-site-checks` | `29e9ca7` | None (policy edits prepared, not applied) | queue Q20, Q34, Q42 |
| `cowork/merchant-center` | `5e46a93` | None | queue Q2, Q8 |
| `cowork/product-data` | `fb8d2f0` | None | queue Q9b, Q15, Q16, Q21, Q37, Q41 |
| `cowork/collections` | `00ad6dd` | None | queue 2b, 4, Q6, Q7, Q32, Q40 |
| `cowork/outreach` | `d70b71e` | None | queue Q25, Q27 |
| `cowork/authority-research` | `c1e0fd9` | None | queue Q26 |
| `cowork/theme-editor` | `f4539f8` | None on the live theme by this workstream | queue Q14 |

**Also recorded under Outside changes observed in the change log,** from programme-records' own Admin reads and from other branches' findings:
- the live theme was replaced on 18 Oct (new MAIN theme at 18:36 UTC);
- the store was password-locked that evening;
- the T-shirt Week tees were made active.

None of these is logged in any workstream's CHANGES.md.

## Earlier reviews (before the files arrived)

## Reviewed 18 Oct 2026, 16:55 UK

| Branch | Commit reviewed | Cut from `main`? | Live changes | Change-log entries to add | Master-queue status to record |
|---|---|---|---|---|---|
| `cowork/geo-measurement` | `eca2845` (18 Oct 16:37) | No (pushed before `main` existed) | None. Research only. | None. Record the 16 Oct run as the programme's GEO baseline. | GEO baseline measured 16 Oct 2026. ChatGPT 63/63 runs, Gemini 63/63, Google UK 16/21 queries, Perplexity 5/63 (sign-up wall). Google UK gap-fill running. |
| `cowork/product-data` | `239cb27` (18 Oct 16:40) | Yes | None. One write (Cream Cap off Google & YouTube, 16 Oct 20:29) was refused by the connector before it reached Shopify. | None | Audit done (25 active products). Items A–K prepared with exact before/after values. Every write waits on George's yes in that chat. |
| `cowork/authority-research` | `7740cd5` (18 Oct 16:40) | No (orphan branch) | None. Nothing posted, submitted or contacted. | None | Second-pass research prepared: 47 scored targets, 8 journalist-request platforms, Trustpilot audit with 12 draft replies, and Trustpilot, LinkedIn and Crunchbase copy. External actions sit with George or the outreach workstream. |

## Reviewed 18 Oct 2026, 17:05 UK

| Branch | Commit reviewed | Cut from `main`? | Live changes | Change-log entries to add | Master-queue status to record |
|---|---|---|---|---|---|
| `cowork/collections` | `1de8481` (18 Oct 16:41) | Yes | None. The 16 Oct 20:40 Denim append was blocked before saving, and live Denim on 18 Oct matched the 16 Oct baseline. | None. This confirms C-003 is not live. | Baselines captured 16 Oct and re-checked 18 Oct. B, B2, C and D drafted, waiting on George's yes in chat. B2 removes "made in Portugal" from Denim. A and E are blocked on Project files. F waits on Search Console. G closed: leave `/collections/sets` alone, because it's noindexed. |
| `cowork/live-site-checks` | `5aef376` (18 Oct 16:42) | Yes | None. Research only. A test checkout went as far as shipping rates, with no submission. | None | Measured baseline 16 Oct (PSI, Rich Results, shipping promises, tee stock lines, mobile popup), re-checked 18 Oct. 10 findings, 2 at P1: tees show false stock and dispatch, and checkout pre-ticks marketing consent. |
| `cowork/search-console` | `3cacbd5` (18 Oct 16:42) | Yes | None. Only exports committed so far; no STATUS or CHANGES yet. | None | UK exports for 21 Jan – 22 Jul 2026 and 15–16 Oct 2026 committed. The property has no performance data for 23 Jul – 14 Oct 2026. |

## Reviewed 18 Oct 2026, 17:15 UK

| Branch | Commit reviewed | Cut from `main`? | Live changes | Change-log entries to add | Master-queue status to record |
|---|---|---|---|---|---|
| `cowork/merchant-center` | `4fcc18f` (18 Oct 17:00) | Yes | None. Two exports were downloaded, and the UK shipping wizard was opened and cancelled without saving. | None | Audit done. All 25 Shopify products are approved for the UK. The only UK disapproval is the Cream Cap, which waits on product-data item A. Other disapprovals come from 10 hand-added `CROOKSRELEASESEPT` duplicates and from five minor markets. GTIN task B can't be done as briefed. Re-check booked for 29 Oct, ahead of the 1 Nov opt-out decision. |
| `cowork/outreach` | `65abd3c` (18 Oct 16:47) | Yes | None. Nothing submitted, no profile created, no draft made. | None | Both directory forms inspected (both free). Pitch routes verified for 8 outlets: 3 usable, 2 weak, 3 to skip. Blocked on `07-directory-submission-pack.md` and `07-authority.md`. |

**Result so far:** none of the eight branches reports a live change. When `change-log.md` arrives, they add no change-log entries. Their status goes into the master queue only.

## Cross-workstream notes

1. **The GEO panel exists, but authority-research hasn't used it.** Authority-research §4 and its Blocker 1 say no panel runs were available, so it reported a search-ranking proxy. The real 16 Oct run is on `cowork/geo-measurement` at `workstreams/geo-measurement/artifacts/runs/2026-10-16/`. Its "Sources the AI answers cite most" table is observed citation data. For example, phrasestudios.com was cited in 25 AI runs and streetwear.directory in 9. That table can replace the proxy.
2. **Several workstreams are missing files from the same Project folder:**
   - this workstream: `change-log.md`, `master-queue.md`, the status report and `10-measurement.md`;
   - product-data: `05-reactive-drafts.md`, `assets/README.md` and the photo inbox;
   - authority-research: `07-authority.md`;
   - collections: `01-collections-internal-linking.md`, `05-reactive-drafts.md`, `05-query-map.md` and `p1-collection-audit-2026-10-16.md`;
   - outreach: `07-directory-submission-pack.md` and `07-authority.md`.

   All of these are listed in `WAITING-ON-GEORGE.md`, along with the suggestion to import the whole `seo/` folder in one go.
3. **No owner for the contact-page copy.** Authority-research found "run out of London" on crooksldn.com/pages/contact. It should read "independent British streetwear brand". No workstream branch owns site page copy yet.
4. **Two branches don't share history with `main`:** `cowork/geo-measurement` and `cowork/authority-research`. Whoever merges them will need `--allow-unrelated-histories`, or the workstream rebases onto `main` first. `cowork/product-data`, `cowork/collections`, `cowork/live-site-checks` and `cowork/search-console` are all cut from `main`.
5. **Search Console has no data for 23 Jul – 14 Oct 2026. This affects Q36.** Any live entry deployed in that window, or just after it, has no Search Console window immediately before the deploy. The nearest data is 21 Jan – 22 Jul 2026 (pre-gap, so a different season and not like-for-like) and 15–16 Oct 2026 (two days). Q36 is still applied as briefed: the Shopify 90-day baseline where it exists, otherwise "no baseline: Search Console pending". An entry's Search Console baseline should be labelled with the window it actually comes from.
6. **The held "Claude P1 fixes" theme would undo later live edits.** Live-site-checks found it is a full copy of the live theme as of 16 Oct. It differs only in the popup snippet and the Organization schema snippet. If it is published after any live theme-editor change, that change is lost. P1 theme copy stays on hold, and any live theme change logged after 16 Oct needs this risk noted against it.
7. **The tee stock fix crosses two workstreams.** Live-site-checks' tee fix (`made-to-order` tag, untracked inventory, including the 14 draft tees) builds on product-data item D2. Both branches already record this, so there is one change for the queue, owned by product-data.
8. **Collections is waiting on `cowork-results/05-search-console.md`.** That file will never exist in the old location. The Search Console exports are now on `cowork/search-console`, and its findings file is still to come.
9. **"Made in Portugal" is live on two collections.** Collections found it in the Sweats and Denim descriptions. That contradicts the facts in force (all products are made in China, and manufacturing origin stays out of consumer copy). B2 and A remove it, and both are waiting on George.
