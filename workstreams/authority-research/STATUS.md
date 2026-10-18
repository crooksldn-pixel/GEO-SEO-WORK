# Workstream: Authority research, second pass (earned media, Trustpilot, entity profiles)

**Branch:** cowork/authority-research  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 21:45 UK  
**Priority:** P2  
**Overall status:** READY TO IMPLEMENT

## Objective

Extend the first authority pass (07-authority, 222 opportunities, owned by `cowork/outreach`) into the segments it couldn't cover:
- UK national press;
- grime, rap and music titles;
- youth culture and student outlets;
- journalist-request platforms;
- since 18 Oct, outlets that cover water- and heat-reactive outerwear.

Each target is scored on relevance × authority × likelihood × GEO value, with evidence, pitch route and angle.

The workstream also:
- audited the public Trustpilot reviews and drafted replies;
- prepared the LinkedIn and Crunchbase copy;
- mapped which sources AI assistants cite against the target list.

This is a research-only workstream. It contacts no one, submits nothing and creates no profiles.

## Current state

Research is finished, George's 18 Oct answers are applied ([ANSWERS.md](ANSWERS.md)), and the outputs are ready for the people who act on them. **Nothing in this workstream is live.**

| Area | Status |
|---|---|
| Earned-media targets | **63 scored rows**: 33 new vs 07, 30 overlapping with 07 IDs, 6 parked (need samples or seeding). CSV ready for the outreach merge. |
| Trustpilot | **Done by `cowork/trustpilot`** on 18 Oct: 12 replies posted, profile renamed CROOKSLDN, description and address replaced. The model-review reports are owned there (route blocked in-app; support report pending George's go there). The invitation change is parked (decision #6). |
| LinkedIn and Crunchbase | **Final copy ready**: `artifacts/profile-pack-linkedin-crunchbase.md`. George creates both. |
| GEO citations | Mapped from the 16 Oct panel: Streetwear Directory is ChatGPT's only cited source for "brands like Corteiz". |

Live conditions that affect timing (FINDINGS 12–14):
- The storefront redirected to `/password` at ~20:15 BST on 18 Oct.
- The Black Convict hoodie has stock in XS only.
- GRM Daily's site is a holding page.

## Completed

**Researched**
- 63 targets with evidence URLs, including 16 added by the 18 Oct follow-up: 11 reactive-outerwear outlets and 5 national press.
- 8 journalist-request platforms. 13 paid and 3 dead or irrelevant ones excluded.

**Audited**
- 21 Trustpilot reviews at 1–3★, grouped by complaint.
- Trustpilot's business guidelines.
- Black Convict stock (Shopify, read-only).
- Storefront access.

**Prepared**
- Profile pack: LinkedIn and Crunchbase.
- Ranked CSV with an `in_07` merge key.
- Dedupe note for 07 (`artifacts/dedupe-vs-07.md`).
- GEO citation mapping.

**Measured (read only, not this workstream's measurement):** the 16 Oct GEO panel citations, mapped to targets.

**Handed over:** the 12 Trustpilot reply texts went to `cowork/trustpilot`, which posted them.

## Currently working on

Nothing currently running.

## Blockers

None. Everything left belongs to George or to another workstream (below and in NEXT.md).

## Waiting on George

1. **Create the LinkedIn company page and the Crunchbase entry** from `artifacts/profile-pack-linkedin-crunchbase.md`, once the storefront is public again. LinkedIn's organisation-size field is required; the pack assumes 2–10 employees, so change it if that's wrong.

All other decisions were answered on 18 Oct. The parked ones (review-invitation change, Dripscan, samples and seeding, edits to the 12 Feb and 10 Feb replies) block nothing.

## Waiting on external systems

- Crunchbase's review of the new entry, after George submits it.
- The new GRM Daily website.

## Next actions

1. **Outreach (`cowork/outreach`):** prioritise the Streetwear Directory listing (ChatGPT's only cited source for "brands like Corteiz"), then Disco.
2. **Outreach:** merge `artifacts/authority-targets-second-pass.csv` into 07 using `in_07`.
   - Draft text-only pitches in score order, starting with Mixtape Madness, Complex UK's culture column, Man of Many, GQ and Yanko Design.
   - Leave ⏸ rows alone.
   - Hold IndyBest and FashionBeans until the Black Convict hoodie is back in S–XL.
3. **George:** create the LinkedIn and Crunchbase profiles once the store is public.
4. **Entity/collections workstreams:** the contact-page "run out of London" fix (approved, owned by collections). After the profiles go live, George decides whether they join `sameAs`.
5. **Content workstream:** the reactive-outerwear niche is open. Almost no editorial covers water-reactive jackets, and AI panels name no brand. The approved reactive guide plus TikTok captions using the exact phrases "water reactive jacket" and "heat reactive puffer" are the cheapest way in.
6. **GEO measurement:** re-run after the directory listings go live. Baseline: CROOKSLDN named in 0 of 60 category and competitor answers.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** High  
**Confidence:** Medium

- **GEO:** the Streetwear Directory and Disco listings target the exact sources AI assistants cite for competitor prompts. LinkedIn and Crunchbase add authoritative entity records.
- **Reactive outerwear:** a niche where no brand is named yet.
- **Commercial:** the Trustpilot clean-up (done in its own workstream) protects conversion.
- **Confidence:** medium, because likelihood scores for a small label are judgement calls and the GEO effect needs a re-measure.

Key artefacts:
- `artifacts/09-authority-research.md`: full research.
- `artifacts/authority-targets-second-pass.csv`: ranked targets with the `in_07` key.
- `artifacts/dedupe-vs-07.md`
- `artifacts/geo-cited-sources-vs-targets.md`
- `artifacts/profile-pack-linkedin-crunchbase.md`
- `QUESTIONS.md` / `ANSWERS.md`
