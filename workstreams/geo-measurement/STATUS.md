# Workstream: GEO measurement (UK GEO panel)

**Branch:** cowork/geo-measurement  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 21:00 BST  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Build a repeatable, evidence-backed UK GEO panel for crooksldn.com, and use it to set the programme's baseline:
- 21 queries, plus one labelled extra query.
- Google UK, plus ChatGPT and Gemini 3 times per query. Perplexity is parked.
- Every result recorded only from what is on screen, with screenshots.

This is research only. It changes nothing on the store or any account.

## Current state

**The baseline is measured.** Results by surface:

| Surface | Result | Run |
|---|---|---|
| Google UK | 21/21 queries | 16 on 16 Oct; the other 5 on 18 Oct as a dated gap-fill |
| ChatGPT | 63/63 runs | 16 Oct |
| Gemini | 63/63 runs | 16 Oct |
| Perplexity | 5/63 runs | 16 Oct; the rest hit a sign-up wall. A panel account is parked by George. |

**Headline:** Crooks appears only when the query contains "Crooks". It was named in 0 of 110 readable non-brand AI answers and on 0 of 18 non-brand Google UK pages (top 20 plus AI Overview). See `FINDINGS.md`.

**George's answers (18 Oct, 17:03 UTC) are applied.** The record is `ANSWERS.md`; how each answer was applied is in `artifacts/questions-for-george.md`.
- **Q2:** Crooks London Limited (16396366) is George's company, but not the public operator, which is Crooks Clothing Company Ltd (16606021). FINDINGS Finding 6 is rewritten to match.
- **Q3:** no IP address, network or location in committed files. This workstream removed:
  - the network detail from both run summaries;
  - the IP-based location footer from all 63 Gemini screenshots;
  - Google's local-store location pins (see `CHANGES.md`).
- **Q5:** "water reactive windbreaker" is added as a labelled extra query (`artifacts/panel-method.md`). Its baseline was captured on 18 Oct at 19:23–19:29 UTC (`artifacts/runs/2026-10-18-extra-query/`):
  - Crooks is named in 0 of 7 answers.
  - **Gemini run 2 cites the crooksldn.com HydroCuff page as a source.** This is the first crooksldn.com citation in any non-brand answer.
  - On Google, Mertra holds all of page 1.
- **Q6:**
  - The re-run stays on Fri 13 Nov.
  - T-shirt Week and every change that went LIVE around the baseline are logged in `artifacts/run-log.md`.
  - Changes C-001, C-002, C-006, C-007 and C-WS02-1 were all live 25 minutes to 4 hours before the baseline started. The baseline is the before-reading for them, and 13 Nov is the first after-reading.
- **Q1 (Perplexity) and Q6 (scheduling the run):** parked.

**What happens next:** the 13 Nov run of the core 8 plus the extra query (see `NEXT.md`).

**Overlaps with other workstreams.** These are coordinated through this repo, and none of their files was edited:
- **authority-research:** asked the panel to check its candidate domains. Answered in `artifacts/authority-candidate-citations.md`. Finding 6 supports its plan to use Crooks Clothing Company Ltd on Trustpilot, LinkedIn and Crunchbase.
- **outreach:** uses the streetwear.directory citation data, and asks for a re-run about a month after its listings go live.
- **product-data:** uses this run's Google Shopping-pack evidence.
- **search-console:** is the source of the extra query, and marks T-shirt Week too.
- **programme-records:** records the 16 Oct run as the programme's GEO baseline. Its merge register still lists this branch's old pre-rebase commit `eca2845`; the baseline commit is now `788cbb8`.

## Completed

- **Method written:** `artifacts/panel-method.md`, updated 18 Oct with the extra query, the country-only rule and Perplexity parked.
- **Measured, 16 Oct 2026 baseline:** `artifacts/runs/2026-10-16/`
  - `results.csv`: 210 rows.
  - `meta.json`, `summary.md`.
  - 223 screenshots.
- **Measured, 18 Oct 2026 Google UK gap-fill** for the 5 queries not run on 16 Oct: `artifacts/runs/2026-10-18/`
  - `results.csv`: 5 rows.
  - `meta.json`, `summary.md`.
  - 10 screenshots.
- **Measured, 18 Oct 2026 extra-query baseline**, "water reactive windbreaker": `artifacts/runs/2026-10-18-extra-query/`
  - `results.csv`: 7 rows (Google UK 1, ChatGPT 3, Gemini 3).
  - `meta.json`, `summary.md`.
  - 9 screenshots.
- **Researched:** 8 findings in `FINDINGS.md`. Finding 6 was updated with George's Q2 answer.
- **Researched:** authority-research's candidate domains checked against both runs: `artifacts/authority-candidate-citations.md`.
- **Logged:** runs and every event that can move the readings, including T-shirt Week: `artifacts/run-log.md`.
- **Applied owner decision #16** to this workstream's committed files: `CHANGES.md`.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Perplexity login wall (parked by George, 18 Oct)

**Blocking:** the Perplexity column of the panel (58 of 63 runs blocked on 16 Oct)  
**Needs:** One dedicated Perplexity account for the panel, with memory off. George signs in himself, using email, not Google.  
**From:** George. Parked, so it blocks nothing else.  
**Severity:** P3  
**Can work around it?:** Yes  
**Workaround:** Report Google UK, ChatGPT and Gemini only. Record Perplexity as not run, with the reason.

## Waiting on George

1. Switch the GitHub default branch to `main` (GitHub → Settings → default branch). It is still this branch. This was also raised by programme-records.

Parked by George, not blocking anything: the Perplexity panel account, and whether the 13 Nov run should be a scheduled task.

## Waiting on external systems

- Google and the AI engines re-crawling the changes that went live on 16 Oct (C-001, C-002, C-006, C-007, C-WS02-1), plus any later ones, before a re-measure can show movement.
- The Streetwear Directory and Disco listings going live (outreach). Once they do, the competitor queries stop being drift controls.

## Next actions

1. Before 13 Nov: add any new LIVE changes from the programme change log to `artifacts/run-log.md`.
2. Fri 13 Nov 2026: run the core 8 plus "water reactive windbreaker" on Google UK, ChatGPT and Gemini, into a new dated folder. Use the drift controls described in `run-log.md`.
3. About 4 weeks after the Streetwear Directory or Disco listing goes live: re-run all 21 queries and check whether those pages start carrying Crooks into AI answers.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** High  
**Confidence:** High

This workstream changes nothing by itself. It is the measurement every other workstream is judged against, and it shows which third-party pages the AI answers actually cite. That makes outreach and on-site copy decisions evidence-based instead of guesses.
