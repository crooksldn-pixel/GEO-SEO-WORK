# Findings

## Finding 1 — Live baseline confirmed: 4.2 from 80, and 8 months without a reply to a negative review

**Finding:**
- TrustScore 4.2 "Great" from 80 reviews (5★ 57 · 4★ 2 · 3★ 1 · 2★ 1 · 1★ 19). Same as the authority-research reads on 16 and 18 Oct.
- Trustpilot's own reply figures shown to readers: 45% of negative reviews answered, 12.6 days average, **last reply to a negative review 12 Feb 2026**.
- 12 low-star reviews are unanswered: ten 1★, one 2★, one 3★.
- The public listing shows 79 reviews. One 1★ counted in the distribution is not in the listing.
- No 1–3★ review since 30 Jul 2026. Every review since then is 5★ (30 in Sep–Oct; newest 14 Oct).

**Evidence:** page data at https://uk.trustpilot.com/review/crooksldn.com, read in Chrome 18 Oct 2026 ~18:30 BST. `artifacts/review-audit.md`.

**Why it matters:** the reply stats are displayed on the profile and visible to anyone checking legitimacy. Replies fix the stat and the silence at the same time.

**Confidence:** High

**Recommended action:** post the 12 replies (`artifacts/reply-pack.md`).

## Finding 2 — The store was password-locked during the audit

**Finding:** at ~18:35 BST on 18 Oct 2026 every crooksldn.com URL, including the policy pages, redirected to `/password`. That is the destination of Trustpilot's "Visit website" link and of the links in Google's AI answers for "is crooks ldn legit" and "crooksldn scam".

**Evidence:** Chrome navigation to https://crooksldn.com/policies/shipping-policy landed on https://crooksldn.com/password. A WebFetch of the same URL got the same result.

**Why it matters:** a locked store next to unanswered "scam" reviews reads as a dead shop. Conversion and reputation.

**Confidence:** High that it was locked at that time. Unknown whether intentional (e.g. pre-drop).

**Recommended action:** storefront owner / George confirm. Not changed here.

## Finding 3 — Google's AI answers about CROOKSLDN's legitimacy are built from the Trustpilot page

**Finding** (Google, UK, signed-in Chrome, 18 Oct 2026):
- **"crooksldn reviews"** — AI Overview cites only Trustpilot. Quotes 4.2. Lists quality, fit and design as positives; shipping delays and slow email support as negatives; and "return handling" problems, which no visible review describes.
- **"is crooks ldn legit"** — AI Overview says it is legitimate, gives **4.1** (stale), says email support is poor and Instagram DMs work better. Organic results: CROOKSLDN Trustpilot #1, **Crooks & Castles' Trustpilot #2**, then TikTok, the homepage, unrelated "crooks" scam stories (a Facebook scam-ads warning, a Mirror article).
- **"crooksldn scam"** — AI Overview calls the reputation "mixed", names team@crooksldn.com as an address that ignores emails, cites Scamadviser, and offers the reader chargeback help. Organic: Trustpilot, Scamadviser, Trustpilot .com and .ca copies, TikTok, Gridinsoft (64/100).
- The Trustpilot snippet shows the display name **"Crooks ldn"** and the lowercase address "oairo offices, unit m, Bour…".
- The homepage's search title is **"Crooks London Streetwear | Fleece, Denim & Tees"**, which conflicts with the CROOKSLDN naming rule.

**Evidence:** Google results pages read in Chrome, 18 Oct 2026 ~18:40 BST. Observation only; no GEO score is derived from this.

**Why it matters:**
- **GEO:** the unanswered complaints and the name and address fields on Trustpilot are what assistants repeat. Visible replies routed to one inbox are the cheapest counterweight.
- The Crooks & Castles result confirms the name-confusion risk on reputation queries.

**Confidence:** High for what was shown on 18 Oct. AI Overviews vary run to run.

**Recommended action:**
- Replies and profile clean-up (this workstream).
- Homepage title: storefront workstream.
- geo-measurement: add "is crooksldn legit" and "crooksldn scam" to the brand-query panel and re-run at the 7- and 28-day checkpoints.

## Finding 4 — The profile description name-drops competitors, with a typo

**Finding:** the current Trustpilot description is "Streetwear Brand" followed by "Similiar to: Corteiz - Supreme - Ultralight - Poser - Upinflames - Protect".

**Evidence:** profile page data (`infoBusinessUnitBox.descriptionText`), 18 Oct 2026.

**Why it matters:** it ties the entity to six other brands in exactly the field assistants and search snippets read, and it misspells "similar". Trustpilot's Guidelines for Businesses (v7.3) say profile information must be accurate and not misleading.

**Confidence:** High

**Recommended action:** replace it with the approved brand line (`artifacts/action-pack.md` §1).

## Finding 5 — Pre-delivery invitations produced a share of the low-star reviews

**Finding:**
- 9 visible reviews came through Trustpilot's Shopify integration (15 Feb – 14 Mar 2026). **6 of the 9 are 1–2★**, all verified, all about orders not arriving.
- One of them complains about being asked for a review when the order never arrived.
- 12 visible reviews came through a Trustpilot basic link (5 Sep – 14 Oct 2026). All 12 are 4–5★. That link is the one in the shipped-today email, which skips orders tagged out for problems (authority-research Finding 4).

**Evidence:** `labels.verification.reviewSourceName` in the profile page data, 18 Oct 2026.

**Why it matters:** invitations sent before delivery generate complaints; invitations that skip problem orders are the screening Trustpilot bans. Both are invitation-setup risks.

**Confidence:** High on the source labels. The mechanism behind the February invites is inferred.

**Recommended action:** none now. George: review-request changes **NOT NOW** (18 Oct). Recorded for when that decision is revisited.

## Finding 6 — Complaints are delivery and silence; nothing on product

**Finding** (visible reviews, 18 Oct):
- All 20 visible 1–3★ reviews are about late, missing or partial delivery and/or unanswered or contradictory communication.
- Sizing: 0 low-star mentions, 9 positive mentions. Quality: 1 low-star mention (positive), 35 positive mentions.
- "Scam" appears in 7 reviews, all 1★, 5 already answered.
- Refund or chargeback: 2 (both answered).
- Returns: 0. Tracking: 1.

**Evidence:** keyword and manual read of the page data. `artifacts/review-audit.md` §3.

**Confidence:** High

**Recommended action:** replies route everyone to one inbox and promise only what the published policies say.

## Finding 7 — Older public replies send customers to three different addresses

**Finding:** of the 8 answered low-star reviews, 5 replies point to support@crooksldn.com and 1 to crooksldn@gmail.com. The profile, site and policies say team@crooksldn.com.

**Evidence:** reply texts in the page data, 18 Oct 2026.

**Why it matters:** customers write to the wrong inbox, and the "no reply" pattern continues. Google's AI answer already says email support ignores people.

**Confidence:** High

**Recommended action:** George decides whether to edit those replies to team@crooksldn.com (address-only correction). Not in the approved scope; the earlier question about editing two older replies is parked.

## Finding 8 — The two model reviews are self-declared working relationships

**Finding:**
- Both 5★, both posted 16 Sep 2026, both the reviewer's only Trustpilot review, both organic (not invited).
- Both reviewers say in the review that they modelled for CROOKSLDN, and both review the shoot (catering, the team, how models were treated), not a purchase.
- No name matching was used.
- Trustpilot v7.3: people "working for your business" may not review it. The published flag reasons (harmful or illegal, personal information, advertising or promotional, not based on a genuine experience, about a different business) have no separate conflict-of-interest category.

**Evidence:** review text in the page data; https://corporate.trustpilot.com/legal/for-businesses/guidelines-for-businesses/sep-2026

**Confidence:** High on the relationship. Medium on whether a flag removes them, because the "not genuine" route runs through Trustpilot's detection software.

**Recommended action:** flag both, with the note in `artifacts/action-pack.md` §2. If the flag form rejects or keeps them, escalate to Trustpilot's Content Integrity team with the same evidence.

## Finding 9 — Reviewer names are still on the public authority-research branch

**Finding:** `workstreams/authority-research/artifacts/09-authority-research.md` on `cowork/authority-research` still lists reviewer display names next to each low-star review (§2.2), in the draft replies (§2.4), and names the two model reviewers (§2.5). Decision #16 was applied to that branch's FINDINGS 3–4 only.

**Evidence:** file at commit aeaa30e on `cowork/authority-research`, read 18 Oct 2026.

**Why it matters:** the repo is public. It conflicts with decision #16.

**Confidence:** High

**Recommended action:** authority-research or programme-records redacts §2.2, §2.4 and §2.5. Not edited from this branch.
