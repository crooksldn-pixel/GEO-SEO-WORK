# Workstream: Authority research, second pass (earned media, Trustpilot, entity profiles)

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).

**Branch:** cowork/authority-research  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:15 UK  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Extend the first authority pass (`07-authority.md`, 222 opportunities, owned by the outreach workstream) into the segments where it hit search limits:
- UK national press style desks
- grime, rap and music titles
- youth culture and student outlets
- journalist-request platforms

Each target is scored on relevance × authority × likelihood × GEO value, with an evidence URL, pitch route and angle.

The workstream also:
- audits CROOKSLDN's public Trustpilot reviews and drafts honest replies for George to post;
- drafts Trustpilot, LinkedIn and Crunchbase profile copy for Crooks Clothing Company Ltd (16606021);
- reports which sources AI assistants cite for "best UK streetwear brands" and "brands like Corteiz".

This is a research-only workstream. It contacts no one, submits nothing and creates no profiles.

## Current state

The research is finished and the artefacts are prepared. **Nothing is live.** Every external action (posting replies, creating profiles, pitching) belongs to George or to the outreach workstream (07).

**Trustpilot** was re-checked on 18 Oct and is unchanged from 16 Oct:
- TrustScore 4.2 "Great" from 80 reviews.
- 21 reviews at 1–3★, 12 of them still unanswered.
- Display name still "Crooks ldn".

**This record is not yet deduped against 07-authority.md.** 07 isn't in this repo and the project `seo/` folder isn't reachable.

**The GEO panel is now available** on `cowork/geo-measurement`. Its 16 Oct cited sources are mapped against this target list in `artifacts/geo-cited-sources-vs-targets.md`.

**Repo state.** This branch was first pushed as an orphan, because the repo was empty at the time. It was then rebased onto `main` once the programme-records workstream created it.

## Completed

**Researched**
- 47 scored earned-media targets across national press, music titles, youth culture, student press, and ranking listicles/directories. All have evidence URLs.
- 8 journalist-request platforms with live status and cost. 13 paid tools and 3 dead or irrelevant ones are excluded, with reasons.
- Spot-checked the contact routes for Mixtape Madness, Clash, Trench, Hunger and Shift London.
- Verified the backwardfashion and discobrands submission criteria.

**Audited**
- All 21 public 1–3★ Trustpilot reviews, grouped by complaint: delivery 20, communication 18, refund/chargeback 2, sizing 0, quality 0.
- Read Trustpilot's Guidelines for Businesses (v7.3, Sept 2026). Identified 5 compliance risks.

**Prepared**
- 12 draft Trustpilot replies in George's voice, plus 2 suggested edits to earlier replies.
- Trustpilot, LinkedIn and Crunchbase copy, checked against Companies House and the 16 Oct brand rules.
- Ranked target CSV for the outreach merge.

**Measured**
- Mapped the 16 Oct GEO panel's cited sources (geo-measurement's measurement, not this workstream's) for "best UK streetwear brands", "brands like Corteiz" and related prompts against the target list. Two new domains were checked: Dripscan and Wings2Fashion.
- Checked Companies House for the entity AI assistants cite.
- Also kept: the 16 Oct search-ranking proxy (10 prompts) and a summary of 2025–26 studies on AI citation sources.

## Currently working on

Nothing currently running. Waiting for George's answers in `QUESTIONS.md`. The follow-up research turn runs once this session resumes.

## Blockers

### Blocker 1 — 07-authority.md not available

**Blocking:** deduping this list against the first pass's 222 opportunities. GEO panel runs are no longer a blocker: they're on `cowork/geo-measurement`.

**Needs:** `seo/workstreams/07-authority.md` committed to this repo, or attached to this chat (see issue #1, raised by programme-records for the Project files).  
**From:** George or the outreach workstream  
**Severity:** P2  
**Can work around it?:** Yes  
**Workaround:** The outreach session dedupes by domain when it merges. Rows likely to duplicate 07 are marked "check 07".

### Blocker 2 — search budget and blocked sites

**Blocking:** evidence rows for The Times/Sunday Times Style, Telegraph, the i, Metro, Mail, Sun, Mirror, Star, Sky, ITV, Esquire UK and Men's Health UK; the GRM Daily contact route; a Reddit ranking check.  
**Needs:** a follow-up research turn. Reddit and some national sites need a normal browser.  
**From:** other (tooling limits)  
**Severity:** P3  
**Can work around it?:** Yes  
**Workaround:** The top-ranked targets are already evidenced, so outreach can start with them.

## Waiting on George

**All open questions are in [`QUESTIONS.md`](QUESTIONS.md): 14 numbered questions, each with options, a recommendation and an answer line.** Reply "answered" to this session once they're filled in.

1. Q1–Q2: which company is the public operator, and the trading-name line. These block the LinkedIn and Crunchbase copy.
2. Q3–Q7: support inbox, approval of the 12 Trustpilot replies, the the 8 Feb 2026 review, the two model reviews, and the change to how reviews are requested. These block the Trustpilot work.
3. Q8: the contact-page "run out of London" copy.
4. Q9–Q14: smaller calls (Crunchbase team, Dripscan, IndyBest samples, core colourway, public-repo detail, the 07 file). Each has a stated default if left unanswered.

## Waiting on external systems

None. Nothing has been submitted.

## Next actions

1. **Trustpilot compliance fixes:**
   - Remove the director-name review if it's Preston's.
   - Take the review link out of the shipped-today email.
   - Switch to Trustpilot's own invitations.

   Biased collection can trigger a Consumer Warning and hide the TrustScore.
2. **Post the 12 replies.** Eight of the 21 low reviews use the word "scam", and AI assistants that summarise Trustpilot can repeat it.
3. **Outreach workstream: prioritise the Streetwear Directory listing** (already approved 16 Oct). It's ChatGPT's only cited source for "brands like Corteiz" (3/3 runs).
4. **Outreach workstream merges §1.1 into 07.** Dedupe by domain, then start with the top text-only pitches:
   - Mixtape Madness (320)
   - Complex UK "JP's UK Culture Picks" (300)
   - British GQ (250)
   - Trench, GUAP, Hunger (180 each)
   - backwardfashion.com (150)
5. **Entity copy fix on crooksldn.com/pages/contact.** Change "run out of London" to "independent British streetwear brand". This belongs to the entity/About or storefront workstream.
6. **Create the Trustpilot, LinkedIn and Crunchbase profiles** from the prepared copy, once the entity decision (Waiting on George #6) is made.
7. **Follow-up research turn** for the national press rows that still have no evidence, and to verify GRM Daily.
8. **Content/collections workstream:** consider an honest, ownership-disclosed CROOKSLDN guide. Brand-owned guides are among the most-cited sources (see `artifacts/geo-cited-sources-vs-targets.md`, note A).

## Expected impact

**Commercial:** High  
**SEO:** Medium  
**GEO:** High  
**Confidence:** Medium

- **Commercial:** Trustpilot sits on the purchase path. Unanswered "scam" reviews and a possible Consumer Warning are a direct conversion risk.
- **GEO:** Trustpilot, LinkedIn and Crunchbase are entity sources AI assistants draw on. Studies put LinkedIn among the most-cited domains, and the ranking listicles are the pool for "brands like Corteiz" answers.
- **SEO:** the earned editorial links are mostly from mid-authority titles.
- **Confidence:** medium, because likelihood scores for a small label are judgement calls and the GEO evidence is a proxy.

Key artefacts:
- [`artifacts/09-authority-research.md`](artifacts/09-authority-research.md): full research, replies and profile copy.
- [`artifacts/authority-targets-second-pass.csv`](artifacts/authority-targets-second-pass.csv): ranked targets for the merge.
- [`artifacts/geo-cited-sources-vs-targets.md`](artifacts/geo-cited-sources-vs-targets.md): GEO panel citations mapped to targets.
