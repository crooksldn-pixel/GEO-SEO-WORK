# Findings

## Finding 1 — The Trustpilot score in circulation is stale

**Finding:**  
The live profile shows **TrustScore 4.2 "Great" from 80 reviews**: 57 five-star, 2 four-star, 1 three-star, 1 two-star, 19 one-star. The "3.3 Average from 50 reviews" figure used in the 16 Oct brief comes from a cached copy whose newest review is from 30 Jul 2026. That copy predates the 30+ five-star reviews posted since 15 Sep.

**Evidence:**  
- https://uk.trustpilot.com/review/crooksldn.com, read in Chrome from the page's embedded data on 16 Oct 2026 and again on 18 Oct 2026.
- A WebFetch on 16 Oct returned the stale 3.3/50 copy.

**Why it matters:**  
Any workstream quoting 3.3 is working from a cached page.
- **Commercial:** the live score is a selling point, not a liability.
- **GEO:** AI assistants may also be reading cached copies.

**Confidence:** High

**Recommended action:**  
Quote 4.2 / 80, dated. Read Trustpilot in a real browser, not through fetch tools.

## Finding 2 — Low reviews are about delivery and silence, not product

**Finding:**  
Across all 21 public reviews at 1–3★:

| Complaint | Reviews (of 21) |
|---|---|
| Late, missing or partial delivery | 20 |
| Unanswered or contradictory communication | 18 |
| Refund or chargeback | 2 |
| Sizing | 0 |
| Quality | 0 |

- The one 3★ review praises the quality.
- **Timing:** 16 of the 21 were posted between 14 Dec 2025 and 14 Mar 2026, the winter pre-order and Chinese New Year backlog period. Since 5 Sep 2026 every review has been 5★.
- **Unanswered:** 12 of the 21 have no reply.
- **"Scam":** 8 of the 21 use the word.

**Evidence:**  
Artifact §2.2–2.3. The source is the page data at https://uk.trustpilot.com/review/crooksldn.com?stars=1&stars=2&stars=3.

**Why it matters:**
- **Commercial:** unanswered "scam" reviews hurt conversion.
- **GEO:** AI summaries of Trustpilot can repeat "scam".
- The fix is replies plus delivery messaging, not product changes.

**Confidence:** High

**Recommended action:**  
George posts the 12 drafted replies (artifact §2.4). Nothing in them promises anything beyond the published policies.

## Finding 3 — Conflict-of-interest reviews on the profile

**Finding:**
- One 5★ review (8 Feb 2026) was checked as a possible staff review. George confirmed on 18 Oct that it is not from anyone at the business.
- Two 5★ reviews (16 Sep 2026) are from people who say they modelled for the brand.

Trustpilot doesn't allow reviews from "someone who is working for your business".

**Evidence:**
- Trustpilot profile page 1 (the two model reviews).
- Companies House officers: https://find-and-update.company-information.service.gov.uk/company/16606021/officers
- Trustpilot Guidelines for Businesses v7.3: https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses/sep-2026

**Why it matters:**  
Misuse can lead to a Consumer Warning on the profile and a hidden TrustScore. That would be a commercial hit and an entity-trust hit for GEO.

**Confidence:** Medium. The name match is exact, but I can't confirm identity.

**Recommended action:**
- Resolved 18 Oct: the 8 Feb review is not a staff review; no action.
- George decides whether to report the two model reviews.
- From now on, no reviews from staff, models, crew, friends or family.

## Finding 4 — The current review asks are selective, and one sits near an incentive

**Finding:**
- The shipped-today email carries the Trustpilot review link (https://uk.trustpilot.com/evaluate/crooksldn.com). It goes out before delivery.
- Orders with problems are tagged `ship-email-sent` so they are left out of that email. Unhappy customers therefore never get the review ask, which is the screening Trustpilot bans.
- The post-delivery "Hope it turned up alright" email carries a per-customer discount code. A review ask in that email would read as an incentive.
- 23 five-star reviews landed on 6–10 Feb 2026, straight after a run of 1★ reviews. Another 13 landed on 15–16 Sep 2026.

**Evidence:**
- Shipped-email setup, as recorded by George: daily Resend send with the `ship-email-sent` dedupe tag, including excluded problem orders.
- The guidelines linked above: "Invite consistently and fairly"; no screening; "We don't allow incentivized reviews on Trustpilot".
- The review dates on the profile.

**Why it matters:**  
This is the same Consumer Warning risk as Finding 3. Selective collection also makes the 4.2 easy to dispute, and one reviewer has already publicly called the February burst "suspect".

**Confidence:** High on the rule. Medium on how the reviews were actually collected, because I can only see the outside.

**Recommended action:**
- Move every review ask to Trustpilot's own Shopify app ("Trustpilot Reviews", free plan, 50 automated invitations a month: https://apps.shopify.com/trustpilot-reviews).
- Send invites automatically, in order, a few days after delivery.
- Remove the link from the shipped-today email.
- Never put a review ask next to a discount code.
- With a few hundred orders fulfilled a month (Jul–Sep 2026, Shopify analytics), the free cap covers about a fifth to a third of orders. Let it run out; don't hand-pick who gets it.

## Finding 5 — Three different support addresses in public replies

**Finding:**  
Earlier Trustpilot replies sent customers to crooksldn@gmail.com, support@crooksldn.com and team@crooksldn.com. The site, the policies and the Trustpilot profile list only team@crooksldn.com.

**Evidence:**
- The reply texts on the Trustpilot profile.
- https://crooksldn.com/pages/contact
- https://crooksldn.com/policies/shipping-policy

**Why it matters:**  
Customers email the wrong inbox, the "no reply" complaints keep coming, and the entity contact data is inconsistent.

**Confidence:** High

**Recommended action:**  
Use team@crooksldn.com everywhere. All the drafts do. George should confirm it's monitored.

## Finding 6 — The contact page breaks the "independent British" descriptor

**Finding:**  
crooksldn.com/pages/contact calls the brand "an independent streetwear label run out of London". That conflicts with the confirmed descriptor ("independent British streetwear brand", never described as being from London) and with the Bourne End address on the same page.

**Evidence:**
- https://crooksldn.com/pages/contact, read 16 Oct 2026.
- The 16 Oct GEO panel (`cowork/geo-measurement`, `results.csv`, brand queries): ChatGPT asked "Are you looking for CROOKSLDN, the London streetwear brand?" in 3 runs, and Perplexity described it as a London label in all 3 of its brand runs.

**Why it matters:**  
**GEO:** inconsistent location signals across the site, Trustpilot and Companies House blur the entity, and AI assistants may describe the brand as being from London.

**Confidence:** High

**Recommended action:**  
Replace the phrase with "an independent British streetwear brand". Owned by the entity/About or storefront workstream. Flagged here, not changed.

## Finding 7 — The best new earned-media routes are music titles with live drop desks

**Finding:**  
Music and culture titles cover UK streetwear peers routinely, and their contact routes are published and verified:

| Outlet | Score | Pitch route |
|---|---|---|
| Mixtape Madness | 320 | info@ |
| Complex UK, "JP's UK Culture Picks" (monthly, June 2026 issue led on Trapstar) | 300 | general contact page |
| Trench | 180 | editorial@ |
| GUAP | 180 | contact@ |
| Hunger | 180 | editorial@rankin.co.uk, for pitches |

Mixtape Madness alone has run about 15 Broken Planet drop stories.

**Already gone (avoid):**
- The Face: dormant since C86 bought it on 26 May 2026.
- Vice UK: no UK style section.
- RWD: dead.
- SBTV: dormant.

**Evidence:** artifact §1.1, rows 1, 2, 7, 8 and 9, each with evidence and contact URLs.

**Why it matters:**
- **SEO:** these are editorial links and brand mentions from titles that already cover the peer set.
- **GEO:** Complex, GUAP and the listicles below appear in the source pools for "best UK streetwear brands".

**Confidence:** Medium. The likelihood scores are judgement calls.

**Recommended action:**  
The outreach workstream merges §1.1 into 07 and drafts text-only pitches for the top rows first. Rows marked ⏸ need samples or seeding, both paused since 16 Oct, so leave them.

## Finding 8 — GEO source pool: one independent listicle dominates, and the Corteiz queries are full of spam

**Update, 18 Oct:** Finding 10 now covers this with observed citations from the 16 Oct panel. The panel confirms the self-ranking-blog pattern and Streetwear Directory's weight.

**Finding:**  
This is a proxy from search ranking (10 prompts, 2 search modes), not observed AI citations.
- **backwardfashion.com** appeared for 6 of 10 queries. It has an "Up and Coming" section for brands under 100k Instagram followers.
- **Self-ranking brand blogs** dominate the fresh 2026 results.
- **"Brands like Corteiz" and "Corteiz alternatives"** are flooded with fake-Corteiz-store spam.
- **Ranking listicles with an editorial route:** retailboss.co, apartstyle.com and fastfashionnews.co.uk.
- **Measmerize (May 2026):** only 38% of AI Overview citations rank in the organic top 10, which limits how far this proxy can be trusted.
- **Gradial (Apr 2026):** brand product pages are rarely cited, while buying guides and FAQs are.

**Evidence:**
- Artifact §4.
- https://backwardfashion.com/streetwear/top-10-uk-brands/
- https://www.measmerize.com/whitepapers/aeo-geo-fashion
- https://www.gradial.com/blog/retail-ai-search-visibility-study

**Why it matters:**
- **GEO:** a few mid-authority listicles shape the "brands like Corteiz" answer pool.
- An on-site buying guide (e.g. on what 550gsm means) is more likely to be cited than product pages.

**Confidence:** Medium

**Recommended action:**
- Pitch backwardfashion's Up and Coming slot.
- Make sure the geo-measurement workstream's panel records whether these domains are actually cited.
- Hand the buying-guide idea to the content/collections workstream.

## Finding 9 — The free journalist-request routes are enough; the UK-focused paid tools aren't needed

**Finding:**
- **#journorequest on X:** about 76 posts a day, 78.5% from UK accounts.
- **#journorequest on Bluesky:** best read through Dot Star Media's free feed.
- **The Source Radar's free tier:** launched Sept 2026, and fashion and retail are among its top categories.

These three cover the UK fashion requests. ResponseSource, JournoLink, Press Plugs, Editorielle and Dot Star alerts are paid and excluded. Christmas print gift guides closed at the end of October; online gift-guide call-outs run to mid or late November.

**Evidence:**  
Artifact §1.2. Key sources: https://www.buzzstream.com/blog/journorequests/ and https://www.thesourceradar.com/

**Why it matters:**  
Gift-guide placements on free-to-read UK titles carry the most AI-visibility value per hour spent.

**Confidence:** Medium

**Recommended action:**  
Outreach sets up saved searches for: gift guide, menswear, streetwear, hoodie, tracksuit, founder.

## Finding 10 — Streetwear Directory is ChatGPT's only cited source for "brands like Corteiz"

**Finding:**  
In the 16 Oct GEO panel, these were the cited sources for the two prompts:

| Prompt | Surface | Sources cited |
|---|---|---|
| "brands like Corteiz" | ChatGPT | **Streetwear Directory, and nothing else, in 3/3 runs** |
| "brands like Corteiz" | Gemini | Streetwear Directory in 1/3 runs |
| "brands like Corteiz" | Google | streetwear.directory organic #6; GQ UK organic #1 and in the AI Overview |
| "best UK streetwear brands" | ChatGPT | Phrase Studios in 3/3 runs |
| "best UK streetwear brands" | Gemini | Wings2Fashion, Rosenberries, Cali Studios, Parlez |

- Disco is cited by Gemini for "brands like Broken Planet".
- **Two genuinely new domains:**
  - **Dripscan:** a magazine attached to a commission-based marketplace. No free editorial route.
  - **Wings2Fashion:** a manufacturer's blog with no featuring route.
- Everything else cited is either already a target or not one: competitor or self-ranking brand blogs, retailers, brand sites, polls.
- CROOKSLDN was named in 0 of the 60 readable category and competitor answers.

**Evidence:**
- `cowork/geo-measurement`: `workstreams/geo-measurement/artifacts/runs/2026-10-16/results.csv` and `summary.md`.
- The mapping is in `artifacts/geo-cited-sources-vs-targets.md`.
- Dripscan pages read 18 Oct: https://www.dripscan.com/magazine/corteiz-sold-out-in-minutes-here-is-what-to-wear-instead and https://www.dripscan.com/the-creators-manifesto
- Wings2Fashion: https://www.wings2fashion.com/blogs/top-15-uk-streetwear-brands/

**Why it matters:**  
**GEO:** for the competitor prompts, ChatGPT's answer pool is effectively one directory. A listing there is the shortest path to being named. The outreach workstream already has approval for it.

**Confidence:** Medium. It's one baseline run with 3 runs per surface, and Perplexity was blocked.

**Recommended action:**
- Outreach prioritises the Streetwear Directory and Disco listings.
- George decides on Dripscan, since it's a channel decision.
- Wings2Fashion only as an optional zero-cost ask.
- The geo-measurement workstream re-measures after the listings go live.

## Finding 11 — AI assistants tie the brand to a different company than the prepared profiles

**Finding:**
- **What AI cites:** Perplexity (3/3 "Crooks LDN" runs) and ChatGPT (1 "Crooks London" run) cite the Companies House record for **Crooks London Limited (16396366)**. It was incorporated 19 Apr 2025 with an Englefield Green registered office, and George is its sole active director.
- **What the profiles name:** the prepared LinkedIn and Crunchbase copy names **Crooks Clothing Company Ltd (16606021)**, as George instructed for profiles.
- **Other confusion:** Perplexity's sources also include a Crooks & Castles Trustpilot page and an unrelated LinkedIn profile.

**Evidence:**
- GEO panel `results.csv`, the Perplexity "Crooks LDN" notes and the ChatGPT "Crooks London" run 2.
- https://find-and-update.company-information.service.gov.uk/company/16396366/officers (read 18 Oct 2026)
- https://find-and-update.company-information.service.gov.uk/company/16606021

**Why it matters:**  
**GEO:** consistent entity data (Companies House, Crunchbase, LinkedIn, site footer and policies) is how assistants resolve "which company is CROOKSLDN". Two different companies across those sources weakens the entity and can surface the wrong registered office.

**Confidence:** High on what is cited. The right choice is George's.

**Recommended action:**
- George confirms which company operates the brand publicly.
- The profiles, the site's legal or footer text and any schema `legalName` then name that company consistently.
- Hold creating the LinkedIn and Crunchbase entries until this is decided.
