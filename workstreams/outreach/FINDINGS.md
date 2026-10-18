# Findings

## Finding 1 — Both approved directories are free and reviewed by hand

**Finding:**
**Disco**
- Free: "Free to apply", "No payment required", "Approved listings are always free".
- Every application is reviewed by hand, usually within 5–7 days.
- 20 fields, 11 required. The first field, "Company (leave this empty)", is a spam trap.

**Streetwear Directory**
- A 6-field Tally form (`vGXPdQ`): no uploads, no account, no payment.
- New brands are reviewed monthly.
- The only free-text field is "Anything Else?".

Field-by-field maps, with the source for each value, are in [`artifacts/directory-form-fields.md`](artifacts/directory-form-fields.md).

**Evidence:**
- https://discobrands.co/submit
- https://streetwear.directory/join, which embeds https://tally.so/r/vGXPdQ. The form schema was read in the browser on 16 Oct 2026.

**Why it matters:**
- Both are free, editorially reviewed listings carrying brand-controlled copy and the official links.
- The brief's stop condition is "if payment is requested, don't submit". Neither form triggers it.
- `cowork/authority-research` lists "whether streetwear.directory charges" as an open gap. The answer is no.

**Confidence:** High

**Recommended action:**
- Submit both with the values from `07-directory-submission-pack.md`.
- On Disco, leave the spam trap, City and Year founded blank.
- Leave Disco's marketing opt-in unticked unless George wants it.

## Finding 2 — Streetwear Directory is a source AI answers already cite

**Finding:** The 16 Oct GEO panel recorded streetwear.directory as a cited source in 9 AI runs (ChatGPT 8, Gemini 1). ChatGPT cited it for a small label "listed in streetwear directories". Crooks was named in none of the 110 readable non-brand AI answers.

**Evidence:** `cowork/geo-measurement`, `workstreams/geo-measurement/artifacts/runs/2026-10-16/summary.md`, table "Sources the AI answers cite most".

**Why it matters:**
- This is the only observed AI citation source this workstream can enter for free and without samples.
- A listing does not guarantee being cited. The cited pages are list pages such as "Brands Like Corteiz".
- Still, the listing is the precondition for appearing there.

**Confidence:** Medium. The citation data is observed. The effect of a listing is not.

**Recommended action:**
- Submit Streetwear Directory first: it needs no images.
- Re-run the panel query set about a month after approval.

## Finding 3 — Only three of the eight Task B outlets have a usable free pitch route

**Finding:**
- **Usable free route:**
  - PAUSE: editorial email.
  - GUAP: free editorial form.
  - Menswear Style Podcast: guest email, given on air.
- **Weak:** FashionBeans and Ape to Gentleman have only general contact forms.
  - FashionBeans's heavyweight hoodie guide is a 18 Sep 2026 freelance piece on established brands.
  - Ape to Gentleman's guide was last modified in Mar 2023.
- **Advertising routes only:** The Sole Supplier and OPUMO.
- **No public route:** WMTV LDN. It looks dormant, with the last episode on 16 Jul 2025.

**Evidence:** Each outlet's own page, linked per row in [`artifacts/pitch-routes.md`](artifacts/pitch-routes.md).

**Why it matters:**
- Pitching through advertising inboxes invites a media kit and fee quote, which breaks the no-paid-placement rule.
- The draft list should shrink to the routes that can produce free editorial.

**Confidence:**
- High for PAUSE, GUAP, The Sole Supplier, FashionBeans and Ape to Gentleman. Each was re-checked directly.
- Medium for the rest:
  - Menswear Style: the address is spoken on air.
  - OPUMO: the address was decoded from the page's obfuscated link.
  - WMTV LDN: this rests on finding no route.

**Recommended action:**
- Draft PAUSE and Menswear Style as Gmail drafts.
- Prepare the GUAP form.
- Offer FashionBeans and Ape to Gentleman as optional.
- Drop The Sole Supplier, OPUMO and WMTV LDN from this round.

## Finding 4 — Menswear Style's podcast interviews also sit in a paid offer

**Finding:** The host invites future guests to email info@menswearstyle.co.uk. The site's Work With Us page offers "paid editorials, paid features, paid links and paid advertising boxes", and its body lists "podcast interviews" among the exposure options.

**Evidence:**
- https://www.menswearstyle.co.uk/workwithus (meta description and body)
- Episode transcript at https://www.buzzsprout.com/1068124/episodes/19240854-guray-kesman-founder-of-kesman-male-grooming-men-s-hair-styling

**Why it matters:** A guest pitch could come back as a sales reply.

**Confidence:** Medium

**Recommended action:**
- The pitch states plainly that it's an editorial guest pitch, not a request for paid placement.
- George declines any fee.

## Finding 5 — Drafts may not default to team@crooksldn.com

**Finding:** The connected mailbox is the brand inbox. Its replies sent on 16 Oct show a gmail.com sender address rather than team@crooksldn.com. The confirmed public contact is team@crooksldn.com.

**Evidence:** Sent folder of the connected Gmail account, 16 Oct 2026 (metadata only). `cowork/authority-research` raises the same question: "Which support inbox is actually monitored (team@, support@ or the Gmail address)".

**Why it matters:** A pitch from a gmail.com address reads less credibly. It also splits replies from the published contact.

**Confidence:** Medium. This rests on the sender metadata. Gmail's From setting was not inspected.

**Recommended action:**
- Check the From address on the first draft before any others are created.
- George confirms which address pitches go out from.
