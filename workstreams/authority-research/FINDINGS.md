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
- A 5★ review from "kellan mullane" (8 Feb 2026) has the same name as a company director, Preston Kellan Mullane.
- Two 5★ reviews (16 Sep 2026) are from people who say they modelled for the brand.

Trustpilot doesn't allow reviews from "someone who is working for your business".

**Evidence:**
- Trustpilot profile page 4 (kellan mullane) and page 1 (Tee Wizza, georgia).
- Companies House officers: https://find-and-update.company-information.service.gov.uk/company/16606021/officers
- Trustpilot Guidelines for Businesses v7.3: https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses/sep-2026

**Why it matters:**  
Misuse can lead to a Consumer Warning on the profile and a hidden TrustScore. That would be a commercial hit and an entity-trust hit for GEO.

**Confidence:** Medium. The name match is exact, but I can't confirm identity.

**Recommended action:**
- If the "kellan mullane" review is Preston's, he deletes it.
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
- With 166–265 orders fulfilled a month (Jul–Sep 2026, Shopify analytics), the free cap covers about a fifth to a third of orders. Let it run out; don't hand-pick who gets it.

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

**Evidence:** https://crooksldn.com/pages/contact, read 16 Oct 2026.

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
