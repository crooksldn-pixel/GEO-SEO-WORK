# Workstream: GEO measurement (UK GEO panel)

**Branch:** cowork/geo-measurement  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 16:40 BST  
**Priority:** P1  
**Overall status:** IMPLEMENTING

## Objective

Build a repeatable, evidence-backed UK GEO panel for crooksldn.com, and use it to set the baseline for the programme:
- 21 queries.
- Google UK plus ChatGPT, Gemini and Perplexity, each AI surface run 3 times per query.
- Every result recorded only from what is on screen, with screenshots.

This is research only. It changes nothing on the store or any account.

## Current state

The 16 Oct 2026 baseline run is committed to this branch:

| Surface | Runs recorded |
|---|---|
| ChatGPT | 63/63 |
| Gemini | 63/63 |
| Google UK | 16/21 |
| Perplexity | 5/63 (the other 58 hit a sign-up wall) |

The measuring Mac went offline before 5 Google UK queries could run. It is back online, so those 5 queries are now being run as a dated gap-fill.

## Completed

- Method written: `artifacts/panel-method.md`.
- Baseline run on 16 Oct 2026, measured: `artifacts/runs/2026-10-16/`
  - `results.csv`: 210 rows.
  - `meta.json`, `summary.md`.
  - 223 screenshots.

## Currently working on

- Google UK gap-fill for Corteiz alternatives, brands like Carsicko, brands like Broken Planet, water reactive clothing and heat reactive clothing.
- Findings write-up.

## Blockers

### Blocker 1 — Perplexity login wall

**Blocking:** Perplexity column of the panel (58 of 63 runs blocked on 16 Oct)  
**Needs:** One dedicated Perplexity account for the panel, with memory off  
**From:** George  
**Severity:** P2  
**Can work around it?:** Yes  
**Workaround:** Report Google UK, ChatGPT and Gemini only. The Perplexity rows stay blank with the reason given.

## Waiting on George

1. Create a Perplexity account for the GEO panel and share the login method.

## Waiting on external systems

- Nothing yet.

## Next actions

1. Finish the Google UK gap-fill and commit it.
2. Write up findings: outreach source list, reactive-product gap, entity confusion.
3. Set the re-measure schedule.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** High  
**Confidence:** High

This workstream changes nothing by itself. It is the measurement every other workstream is judged against, and it shows which third-party pages the AI answers actually cite.
