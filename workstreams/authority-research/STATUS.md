# Workstream: Authority research, second pass (earned media, Trustpilot, entity profiles)

**Branch:** cowork/authority-research  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 16:45 UK  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

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

**This record is not yet deduped against 07-authority.md.** The project `seo/` folder (07 and any GEO panel runs) was not reachable from this session, and neither is in this repo yet.

**Repo state.** On 18 Oct this repo had no commits and no `main` branch. This branch was created as an orphan branch so that nothing was committed to `main`.

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

**Measured (proxy only)**
- Search-ranking pools for 10 GEO prompts, plus a summary of 2025–26 studies on AI citation sources.
- This is not observed AI citation data.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — 07-authority.md and GEO panel runs not available

**Blocking:**
- Deduping this list against the first pass's 222 opportunities.
- Reporting the domains AI assistants actually cite. Task 4 currently has a proxy instead.

**Needs:** `seo/workstreams/07-authority.md` and `seo/measurements/geo-panel/runs/` committed to this repo, or attached to this chat.  
**From:** George, the outreach workstream, or the geo-measurement workstream  
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

1. **Post the 12 Trustpilot replies** (artifact §2.4), or say which to skip. Before posting, confirm team@crooksldn.com is the inbox that gets answered.
2. **Check with Preston** whether the 5★ review from "kellan mullane" (8 Feb 2026) is his. If it is, he deletes it from his Trustpilot account.
3. **Approve two invitation changes:**
   - Install Trustpilot's own Shopify app (free plan, 50 automated invitations a month).
   - Remove the Trustpilot link from the shipped-today email.
4. **Create the profiles** from artifact §3: rename the Trustpilot profile to CROOKSLDN, then the LinkedIn company page and the Crunchbase entry. Confirm the line "CROOKSLDN is the trading name of Crooks Clothing Company Ltd".
5. **Decide whether to report** the two 5★ reviews from people who say they modelled for the brand.

## Waiting on external systems

None. Nothing has been submitted.

## Next actions

1. **Trustpilot compliance fixes:**
   - Remove the director-name review if it's Preston's.
   - Take the review link out of the shipped-today email.
   - Switch to Trustpilot's own invitations.

   Biased collection can trigger a Consumer Warning and hide the TrustScore.
2. **Post the 12 replies.** Eight of the 21 low reviews use the word "scam", and AI assistants that summarise Trustpilot can repeat it.
3. **Outreach workstream merges §1.1 into 07.** Dedupe by domain, then start with the top text-only pitches:
   - Mixtape Madness (320)
   - Complex UK "JP's UK Culture Picks" (300)
   - British GQ (250)
   - Trench, GUAP, Hunger (180 each)
   - backwardfashion.com (150)
4. **Entity copy fix on crooksldn.com/pages/contact.** Change "run out of London" to "independent British streetwear brand". This belongs to the entity/About or storefront workstream.
5. **Create the Trustpilot, LinkedIn and Crunchbase profiles** from the prepared copy.
6. **Follow-up research turn** for the national press rows that still have no evidence, and to verify GRM Daily.
7. **GEO panel run:** check whether the candidate listicle domains (§4) are actually cited.

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
