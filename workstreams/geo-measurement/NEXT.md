# Next

The baseline is measured: Google UK 21/21 queries, ChatGPT 63/63 runs, Gemini 63/63 runs. Perplexity is the only missing surface (5/63). Before running the panel again, read `artifacts/panel-method.md`. Write each new run to a new dated folder under `artifacts/runs/`. Never edit a past run.

## Do next

1. **Perplexity column, once George provides a panel account.**
   - Log in with the dedicated account. Turn memory off.
   - Run the 21 queries × 3 into a new folder `artifacts/runs/<date>/`, with type "perplexity gap-fill" in `meta.json`.
   - Same rules as before: new thread per run, no follow-ups, record only what is on screen.
2. **Control re-run of the core 8 on Fri 13 Nov 2026**, 4 weeks after the baseline, on all four surfaces.
   - This shows how much the answers drift on their own, so later changes aren't mistaken for drift.
   - Use the same browser profile and network (Claude desktop built-in browser on George's Mac, Three UK). Record the IP country.
3. **First real re-measure: the core 8, then all 21**, about 4 weeks after the first relevant change goes LIVE. Check `CHANGES.md` on these branches:
   - `cowork/product-data`: Merchant Center attributes, reactive-product wording.
   - `cowork/collections`.
   - `cowork/outreach` / `cowork/authority-research`: the Streetwear Directory and Disco listings.
   - The entity / About work.

   Compare against `runs/2026-10-16/` and `runs/2026-10-18/`. Report movement only where a captured measurement shows it.
4. **In every run, also record:**
   - the Trustpilot score and review count quoted in brand answers;
   - whether streetwear.directory and discobrands.co list Crooks, and whether those pages are cited (see `artifacts/authority-candidate-citations.md`).

## Do not do yet

- **Don't re-run the full panel before changes are live and indexed.** It would only re-measure the baseline. The dependency is: other workstreams' changes reach LIVE, then about 2–4 weeks for Google and the AI engines to pick them up.
- **Don't log into ChatGPT or Gemini.** The baseline is logged out, so logged-in runs aren't comparable. Perplexity is the exception because it can't be run logged out.
- **Don't add or rename queries in the 21.** Comparability depends on the exact query text. Extra queries can be recorded as a separate, labelled block (see Decisions).
- **Don't merge this branch into `main`.** The orchestrator decides.
- **Don't cite the old GEO 43→54 scores.**

## Decisions still required

All of these are in `artifacts/questions-for-george.md` (Q1–Q7), with options and answer slots. When the answers come back, apply each one as that file says, then update `STATUS.md`.

- **Q1:** a Perplexity panel account (signed in by George, with email not Google), or drop Perplexity.
- **Q2:** is Crooks London Limited (16396366) George's company? See FINDINGS Finding 6.
- **Q3:** keep or redact the measuring IP address in this public repo.
- **Q4:** switch the GitHub default branch to `main`. This was also raised by programme-records.
- **Q5:** add "water reactive windbreaker" as a labelled extra query? See `cowork/search-console` Finding 2.
- **Q6:** the 13 Nov control re-run date, and whether to schedule it.
- **Q7:** the GitHub branch alone, or the run zips in the Project folder too.

## Data still required

- Perplexity answers: 58 of 63 runs blocked on 16 Oct.
- The dates other workstreams' changes went LIVE, from their `CHANGES.md` or the programme change log, to time the re-measure.

## Recommended follow-up date

- **Fri 13 Nov 2026:** core-8 control re-run.
- **Then about 4 weeks after the first relevant LIVE change:** the full re-measure.
