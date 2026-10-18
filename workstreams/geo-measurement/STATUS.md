# Workstream: GEO measurement (UK GEO panel)

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).

**Branch:** cowork/geo-measurement  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:15 BST  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Build a repeatable, evidence-backed UK GEO panel for crooksldn.com, and use it to set the programme's baseline:
- 21 queries.
- Google UK, plus ChatGPT, Gemini and Perplexity, each AI surface run 3 times per query.
- Every result recorded only from what is on screen, with screenshots.

This is research only. It changes nothing on the store or any account.

## Current state

**The baseline is measured.** Results by surface:

| Surface | Result | Run |
|---|---|---|
| Google UK | 21/21 queries | 16 on 16 Oct; the other 5 on 18 Oct as a dated gap-fill |
| ChatGPT | 63/63 runs | 16 Oct |
| Gemini | 63/63 runs | 16 Oct |
| Perplexity | 5/63 runs | 16 Oct; the rest hit a sign-up wall |

**Headline:** Crooks appears only when the query contains "Crooks". It was named in 0 of 110 readable non-brand AI answers and on 0 of 18 non-brand Google UK pages (top 20 plus AI Overview). See `FINDINGS.md`.

**What happens next:** the next measurement waits on other workstreams' changes going live and being indexed. A control re-run is set for 13 Nov (see `NEXT.md`).

**Branch rebased.** At 16:50 this branch was rebased onto `main`. The old orphan commit `eca2845` is now `788cbb8`, with the same workstream files; the gap-fill is `b2260e2`. programme-records' merge register still lists `eca2845`.

**Overlaps with other workstreams.** These are coordinated through this repo, and none of their files was edited:
- **authority-research:** asked the panel to check its candidate domains. Answered in `artifacts/authority-candidate-citations.md`.
- **product-data:** uses this run's Google Shopping-pack evidence.
- **search-console:** tracks the same reactive query family.
- **programme-records:** records the 16 Oct run as the programme's GEO baseline.

## Completed

- **Method written:** `artifacts/panel-method.md`.
- **Measured, 16 Oct 2026 baseline:** `artifacts/runs/2026-10-16/`
  - `results.csv`: 210 rows.
  - `meta.json`, `summary.md`.
  - 223 screenshots.
- **Measured, 18 Oct 2026 Google UK gap-fill** for the 5 queries not run on 16 Oct: `artifacts/runs/2026-10-18/`
  - `results.csv`: 5 rows.
  - `meta.json`, `summary.md`.
  - 10 screenshots.
- **Researched:** 8 findings in `FINDINGS.md`, covering:
  - non-brand invisibility;
  - which list pages AI answers cite;
  - small brands' own list pages getting them named;
  - the reactive-product gap;
  - wrong entity and wrong descriptor;
  - the Companies House mismatch;
  - Trustpilot as the only reputation source;
  - measurement limits.
- **Researched:** authority-research's candidate domains checked against both runs: `artifacts/authority-candidate-citations.md`.

## Currently working on

Nothing currently running. Waiting for George's answers in `artifacts/questions-for-george.md`.

## Blockers

### Blocker 1 — Perplexity login wall

**Blocking:** the Perplexity column of the panel (58 of 63 runs blocked on 16 Oct)  
**Needs:** One dedicated Perplexity account for the panel, with memory off  
**From:** George  
**Severity:** P2  
**Can work around it?:** Yes  
**Workaround:** Report Google UK, ChatGPT and Gemini only. The Perplexity rows stay blank, with the reason in `notes`.

## Waiting on George

Each question has options and an answer slot in **`artifacts/questions-for-george.md`**. Answer there, then tell this session "answered".

1. Perplexity: sign in a panel account in the built-in browser (with email, not Google), or drop Perplexity.
2. Is Crooks London Limited (Companies House 16396366) your company?
3. The repo is public: keep the measuring network's IP address in the run files, or redact it?
4. Switch the GitHub default branch to `main`. This was also raised by programme-records.
5. Add "water reactive windbreaker" as an extra tracked query?
6. Is Fri 13 Nov OK for the control re-run, with the Mac on? Should it be a scheduled task?
7. Is the GitHub branch enough as the record, or should the run zips also go in the Project folder?

## Waiting on external systems

- Other workstreams' changes going LIVE, then Google and the AI engines re-crawling them, before a re-measure can show movement.

## Next actions

1. Hand the cited-source shortlist to outreach and authority-research. streetwear.directory goes first; add wings2fashion.com and rosenberries.co.uk. It is already in `FINDINGS.md` Finding 2 and `artifacts/authority-candidate-citations.md`.
2. Fri 13 Nov 2026: control re-run of the core 8 on all four surfaces.
3. Run the Perplexity column once the panel account exists.
4. Re-measure the core 8 and then all 21, about 4 weeks after the first relevant LIVE change.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** High  
**Confidence:** High

This workstream changes nothing by itself. It is the measurement every other workstream is judged against, and it shows which third-party pages the AI answers actually cite. That makes outreach and on-site copy decisions evidence-based instead of guesses.
