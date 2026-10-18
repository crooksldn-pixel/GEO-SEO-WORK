# Findings

All evidence paths are relative to `workstreams/geo-measurement/artifacts/runs/`. The baseline is `2026-10-16/`. The Google UK gap-fill for the 5 queries not run on 16 Oct is `2026-10-18/`. Counts come from `results.csv`.

## Finding 1 — Crooks is invisible on every non-brand query

**Finding:**  
Crooks only appears when the searcher types "Crooks".
- **Non-brand queries:** 0 mentions across product, category, competitor and specialist:
  - ChatGPT: 0 of 54 runs.
  - Gemini: 0 of 54 runs.
  - Perplexity: 0 of 2 runs.
  - Google UK: 0 of 18 result pages (top 20 plus AI Overview). That count includes the 5 pages from the 18 Oct gap-fill.
- **Brand queries:** crooksldn.com ranks #1 on Google for "Crooks LDN" and "Crooks London", and #5 for "Crooks LDN reviews". The AI answers name Crooks on brand queries: ChatGPT 8/9, Gemini 9/9, Perplexity 3/3.

**Evidence:**  
- `2026-10-16/results.csv`: `crooks_mentioned` by `query_group`
- `2026-10-16/summary.md`: mention-rate table and Google table
- `2026-10-18/results.csv` and `summary.md`: the 5 Google UK queries not run on 16 Oct
- Google page-2 screenshots: `2026-10-16/shots/google_uk__*__1_p2.png` and `2026-10-18/shots/google_uk__*__1_p2.png`

**Why it matters:**  
All discovery traffic (people who don't already know the brand) goes to Corteiz, Trapstar, Represent, Broken Planet, Palace and others. This is the zero point every other workstream should be measured against.

**Confidence:** High for ChatGPT, Gemini and Google UK. Low for Perplexity: only 5 runs answered (see Finding 8).

**Recommended action:**  
Re-run the core 8 queries after other workstreams' changes are indexed (see `NEXT.md`). The first realistic target is any non-brand mention on the category and specialist queries.

## Finding 2 — AI category and competitor answers come from a small set of list articles

**Finding:**  
On category and competitor queries, ChatGPT and Gemini draw on the same few third-party list pages. Google's AI Overviews use the same pages.

| Source | AI runs citing it (of 131) | Google AI Overviews citing it (of 21) | Page seen |
|---|---|---|---|
| phrasestudios.com (Phrase Studios) | 25 (ChatGPT 20, Gemini 5) | 5 | "Best London Streetwear Brands (2026 Guide)", Journal |
| calistudios.co.uk (Cali Studios) | 11 (Gemini) | 2 | UK streetwear brands guide |
| streetwear.directory (Streetwear Directory) | 9 (ChatGPT 8, Gemini 1) | 1 | "Brands Like Corteiz: 9 Alternatives (UK and Global)" |
| wings2fashion.com | 8 (Gemini) | 6 | "Top 15 Best UK Streetwear Brands Dominating Men's…" |
| rosenberries.co.uk | 8 (Gemini) | 0 | "Best UK Streetwear Brands 2026", Chronicles |
| flowlikezen.com (Flow Like Zen) | 4 (Gemini) | 4 | "Top UK Streetwear Brands to Know in 2026" |
| CUOTTI | 4 (Gemini) | 1 (lead AIO source on "brands like Corteiz") | Its own "brands like Corteiz" blog |

The 18 Oct gap-fill adds two "brands like X" observations:
- **Corteiz alternatives:** streetwear.directory ranks #1 organically and is the AI Overview's first source card. The Overview also tells readers to "explore style breakdowns and community recommendations on the Streetwear Directory".
- **Brands like Broken Planet:** discobrands.co (Disco) ranks #4 with "30 Brands like Broken Planet for Streetwear".
- **AI Overview chips:** Phrase Studios is the inline source on 4 of 6 brands for "brands like Carsicko" and 3 of 6 for "brands like Broken Planet". Wings2Fashion is the source on the other 3 Broken Planet brands.

Other list pages ranking on Google pages 1–2 for the category and competitor queries:
- backwardfashion.com, on 8 of 21 queries
- British GQ, "The 20 most advanced streetwear brands"
- Ape to Gentleman, "Top 40 Streetwear Brands"
- freshersfestival.com
- makeitbritish.co.uk

**Evidence:**  
- `sources_cited` in `2026-10-16/results.csv` (rows where `query_group` is category or competitor) and in `2026-10-18/results.csv`
- `2026-10-16/shots/chatgpt__british-streetwear-brands__1.png` (citation chip "Phrase Studios +2")
- `2026-10-16/shots/google_uk__british-streetwear-brands__1_p2.png`
- `2026-10-16/shots/google_uk__emerging-uk-streetwear-brands__1_p2.png`
- `2026-10-18/shots/google_uk__corteiz-alternatives__1.png`
- `2026-10-18/shots/google_uk__brands-like-carsicko__1.png`
- `2026-10-18/shots/google_uk__brands-like-broken-planet__1.png`
- `../authority-candidate-citations.md`: every authority-research candidate checked against both runs

**Why it matters:**  
- Being added to these pages is the most direct route into category-level AI answers. ChatGPT's "Phrase Studios +2" citation appears on almost every category and competitor answer.
- Streetwear Directory is the only directory or listicle candidate that is both cited by AI answers and ranking #1 on a competitor query. George approved a free submission to it on 16 Oct.
- None of the five new authority-research candidates (retailboss.co, apartstyle.com, fastfashionnews.co.uk, graziadaily.co.uk, fashionbeans.com) appears anywhere in the panel.

**Confidence:** Medium. The citation counts are exact. Gemini shows source labels, not URLs, so its labels are merged with their domains by name.

**Recommended action:**  
For the outreach and authority-research workstreams:
- Put streetwear.directory first. Then put wings2fashion.com and rosenberries.co.uk on the list: both are cited and neither is on authority-research's list.
- Rank sources the panel shows being cited above candidates found only by search ranking. See `artifacts/authority-candidate-citations.md`.
- The free directory submissions to Streetwear Directory and Disco were approved on 16 Oct. Every pitch to a list publisher still needs George's OK, under the programme's outreach rule.

## Finding 3 — Small brands get named by publishing their own list pages

**Finding:**  
Several small labels appear in AI answers because their own article or site is the cited source:
- **Google AI Overview, "emerging UK streetwear brands":** lists Flow Like Zen and Cali Studios as emerging brands, while citing Flow Like Zen's and Cali Studios' own list posts.
- **Gemini, "Corteiz alternatives" run 1:** recommends Cuotti as "an emerging European alternative", citing CUOTTI's own blog. On Google UK (18 Oct), CUOTTI's own "brands like Corteiz" posts rank #2 and on page 2 for the same query.
- **ChatGPT, independent and emerging queries:** names V-98, Nobody Apparel, Kushems and Rude Dept, citing each brand's own site.

**Evidence:**  
- `2026-10-16/shots/google_uk__emerging-uk-streetwear-brands__1.png`
- `2026-10-16/shots/gemini__corteiz-alternatives__1.png`
- `2026-10-16/shots/chatgpt__emerging-uk-streetwear-brands__1.png`, `2026-10-16/shots/chatgpt__emerging-uk-streetwear-brands__2.png`
- `2026-10-16/shots/chatgpt__independent-british-streetwear__1.png`

**Why it matters:**  
An owned, well-structured guide or brand page on crooksldn.com can get cited directly. This needs no third-party approval.

**Confidence:** Medium. The pattern is clear in this run but the sample is small.

**Recommended action:**  
For the blog/collections workstream: decide whether a crooksldn.com guide page fits the programme rule of one URL per search intent and no new landing pages. If it does, it should state "independent British streetwear brand", the fabric weights and the product types in plain text.

## Finding 4 — Reactive outerwear is an open lane, but nothing ties Crooks to it

**Finding:**  
- **Water-reactive:** ChatGPT and Gemini name no brand.
  - ChatGPT asked clarifying questions in 6 of 6 runs (water reactive jacket and water reactive clothing).
  - Gemini gave generic hydrochromic explainers citing textile makers (INVIDIA Textile, AKCN). One run refused: "I cannot fulfill this request."
  - **Google's AI Overviews do name brands:**
    - "Water reactive jacket" (16 Oct): Buchan Cheetah Rain Jacket, Lyle & Scott Reactive Shell, Pretty Green Resonance, Mertra Shell. Buchan owns this results page: organic results, the AI Overview, Instagram, Facebook and ads.
    - "Water reactive clothing" (18 Oct): Vilebrequin, HERA Clothing, Sports Direct, Pretty Green (Resonance jacket), Lyle & Scott (Reactive Series), SAYSKY.
    - Buchan is the first Sponsored Product.
- **Heat-reactive:**
  - "Heat reactive puffer": ChatGPT and Gemini name Remyx London (£115), Mertra, PESO, Trapstar Hyperdrive and Pretty Boy Ugly World.
  - Google's AI Overview for "heat reactive clothing" (18 Oct) names Stone Island and Lyle & Scott. Lyle & Scott's "Reactive Series" page ranks #1 for "heat reactive clothing" and #2 for "water reactive clothing".
- **Crooks' own products:** Crooks sells both categories. Google's own AI Overview for "Crooks London" lists the HydroCuff Windbreaker (£85) and the Double-Agent Puffa (£140). Neither product is tied to "water-reactive" or "heat-reactive" in any non-brand answer.

**Evidence:**  
- `2026-10-16/shots/chatgpt__water-reactive-jacket__{1,2,3}.png`, `2026-10-16/shots/chatgpt__water-reactive-clothing__{1,2,3}.png`
- `2026-10-16/shots/gemini__water-reactive-clothing__2.png` (the refusal)
- `2026-10-16/shots/google_uk__water-reactive-jacket__1.png`
- `2026-10-16/shots/chatgpt__heat-reactive-puffer__{1,2,3}.png`, `2026-10-16/shots/gemini__heat-reactive-puffer__{1,2,3}.png`
- `2026-10-16/shots/google_uk__crooks-london__1.png` (AI Overview product list)
- `2026-10-18/shots/google_uk__water-reactive-clothing__1.png`, `2026-10-18/shots/google_uk__heat-reactive-clothing__1.png`

**Why it matters:**  
- **Water-reactive:** ChatGPT and Gemini name no brand at all, so a clear product page could become their default answer. Google's AI Overviews already draw on Buchan, Lyle & Scott and Pretty Green product and collection pages. A product page is therefore the kind of page Google picks up for this query.
- **Heat-reactive:** Remyx London and Mertra hold the AI answers for puffers. Stone Island and Lyle & Scott hold Google's AI Overview for clothing.

**Confidence:** High for what the answers show. Medium for how quickly a product page would be picked up.

**Recommended action:**  
For the reactive-products / product-data workstream: the HydroCuff and Double-Agent product pages should say "water-reactive (hydrochromic)" and "heat-reactive (thermochromic)" in their titles, descriptions and Product data. Re-measure "water reactive jacket" and "heat reactive puffer" after indexing.

## Finding 5 — Wrong entity and wrong descriptor on brand queries

**Finding:**  
- **ChatGPT, "Crooks London":**
  - Run 1 answered about *Crooks 1926*, a theatre show.
  - Run 2 led with *Crooks' Corner* pub, then mentioned "Crooks London Limited" on Companies House.
- **Perplexity, "Crooks LDN":** sources included a fr.trustpilot.com *Crooks & Castles* page and an unrelated LinkedIn profile (seen in runs 2–3).
- **Gemini:** added a Crooks & Castles disambiguation note once.
- **Google UK, "Crooks LDN reviews":** crooksandcandy.com (*Crooks and Candy*) also ranks.
- **Descriptor:**
  - ChatGPT calls it "CROOKSLDN, the London streetwear brand" (Crooks LDN runs 1 and 3, Crooks London run 3).
  - Perplexity calls it a "London-based" or "London streetwear label" (3 of 3).
  - Only Gemini uses the approved descriptor, "independent British streetwear brand".

**Evidence:**  
- `2026-10-16/shots/chatgpt__crooks-london__{1,2,3}.png`
- `2026-10-16/shots/chatgpt__crooks-ldn__{1,3}.png`
- `2026-10-16/shots/perplexity__crooks-ldn__{1,2,3}.png`
- `2026-10-16/shots/gemini__crooks-london__1.png`
- `2026-10-16/shots/google_uk__crooks-ldn-reviews__1.png`, plus that row's `notes`

**Why it matters:**  
Answers that pick the wrong entity lose the searcher. The "London" descriptor breaks the programme's copy rule: "independent British streetwear brand", never "London-based".

**Confidence:** High.

**Recommended action:**  
For the entity / About workstream:
- Use the name "CROOKSLDN (Crooks LDN)" and "independent British streetwear brand" consistently across the site and profiles.
- Add Organization structured data with `sameAs` pointing to the official Instagram and TikTok (@crooksldn) and with `legalName` set (see Finding 6).

## Finding 6 — AI engines connect the brand to a different Companies House record

**Finding:**  
- Perplexity (3 of 3 runs) cites Companies House "Crooks London Limited, 16396366, incorporated 19 Apr 2025, registered office Englefield Green" as the brand's company.
- ChatGPT ("Crooks London" run 2) also points to "Crooks London Limited" on Companies House.
- The legal entity George uses for profiles and listings is Crooks Clothing Company Ltd (16606021).

**Evidence:**  
- `notes` and `sources_cited` (find-and-update.company-information.service.gov.uk) on the Perplexity "Crooks LDN" rows
- `2026-10-16/shots/perplexity__crooks-ldn__1.png`
- `2026-10-16/shots/chatgpt__crooks-london__2.png`

**Why it matters:**  
AI answers present an unconfirmed company record as the brand's legal identity.

**Confidence:** High that the citation happens. Unknown whether 16396366 is connected to George.

**Recommended action:**  
- George: confirm whether Crooks London Limited (16396366) is his.
- Entity workstream: show the legal entity (Crooks Clothing Company Ltd, 16606021) in the site footer and legal pages, and set it as `legalName` in Organization structured data.

## Finding 7 — Every reputation answer comes from Trustpilot, and delivery is the main complaint

**Finding:**  
Every review or rating claim cites Trustpilot:
- ChatGPT: 4.2/5 from 80 reviews, "~71% five-star and 24% one-star".
- Perplexity and Google's AI Overview: 4.1/5 from 79 reviews.

Quality, fit and the V2 joggers are praised. Delivery delays and slow email replies are the main negative in all engines.

**Evidence:**  
- `2026-10-16/results.csv`: "Crooks LDN reviews" rows and "Crooks LDN" Perplexity rows
- `2026-10-16/shots/google_uk__crooks-ldn-reviews__1.png`

**Why it matters:**  
The delivery-delay theme is repeated to anyone who asks AI about the brand.

**Confidence:** High.

**Recommended action:**  
Owner or operations: reply on Trustpilot to delivery complaints, and keep new reviews coming in. Track the Trustpilot score and review count in each panel run.

## Finding 8 — Measurement limits to fix before the next run

**Finding:**  
- **Perplexity:** logged out, it allows about 5 answers and then shows "Sign up and repeat your request." So 58 of 63 runs were blocked.
- **Gemini:** logged out it runs on Flash-Lite. 5 of 63 answers were ungrounded (no sources) and 1 was a refusal.
- **ChatGPT:** logged out it shows "You're using our basic model."

**Evidence:**  
- `2026-10-16/meta.json` (`problems`)
- `BLOCKED:` and `UNGROUNDED` entries in `notes`

**Why it matters:**  
Without a fix, Perplexity is missing from the panel, and logged-out results reflect free-tier models.

**Confidence:** High.

**Recommended action:**  
- George: create one dedicated Perplexity account for the panel with memory off. The protocol allows this.
- Keep ChatGPT and Gemini logged out so runs stay comparable with this baseline.
