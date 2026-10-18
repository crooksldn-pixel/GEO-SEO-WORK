# Authority-research candidates: are they cited in the GEO panel?

This answers the authority-research workstream's request (`cowork/authority-research`, NEXT.md item 7, STATUS Blocker 1): record whether its candidate listicle and directory domains are actually cited.

It uses no new searches. Everything is counted from the two panel runs on this branch:
- `runs/2026-10-16/results.csv`: the baseline.
- `runs/2026-10-18/results.csv`: the Google UK gap-fill.

That gives 131 readable AI answers (ChatGPT 63, Gemini 63, Perplexity 5) and 21 Google UK result pages (pages 1–2 plus the AI Overview).

**How the counts were made:**
- **AI answers:** the `sources_cited` column. Gemini shows source labels, not URLs, so its labels are matched by name.
- **Google AI Overview:** the `sources_cited` column of the `google_uk` rows.
- **Google top 20:** the `competitors` column (first 5 domains) plus the domains listed in `notes`. The 16 Oct notes for the five product queries and "brands like Corteiz" do not list every page-2 domain, so the Google top-20 column is a minimum.

## The authority-research candidates

| Domain | AI answers citing it (of 131) | Google AI Overview source (of 21 queries) | Google top 20 (of 21 queries) |
|---|---|---|---|
| streetwear.directory | **9** (ChatGPT 8, Gemini 1) | **1**: Corteiz alternatives (first source card) | **2**: Corteiz alternatives #1; brands like Corteiz #6 |
| backwardfashion.com | 0 | 0 | **8**: brands like Corteiz (p1), emerging UK streetwear brands (p1), Corteiz alternatives (#9), best UK streetwear brands (p2), British streetwear brands (p2), London streetwear brands (p2), brands like Carsicko (p2), brands like Broken Planet (p2) |
| discobrands.co | 0 | 0 | **1**: brands like Broken Planet #4, "30 Brands like Broken Planet for Streetwear" |
| retailboss.co | 0 | 0 | 0 for the domain. Its Facebook post "Top 10 Corteiz Competitors and Alternatives" (Facebook · RETAILBOSS) is #5 for Corteiz alternatives |
| apartstyle.com | 0 | 0 | 0 |
| fastfashionnews.co.uk | 0 | 0 | 0 |
| graziadaily.co.uk | 0 | 0 | 0 |
| fashionbeans.com | 0 | 0 | 0 |

The rest of authority-research's §4 table:

| Domain | AI answers | Google AI Overview | Google top 20 |
|---|---|---|---|
| complex.com | 0 | 0 | 1 (brands like Broken Planet, p2) |
| wearop.com | 0 | 0 | 1 (Corteiz alternatives, p2) |
| guap.co, highsnobiety.com, spocket.co | 0 | 0 | 0 |
| ldnfashion.com (excluded by authority-research for London framing) | 1 (Gemini) | 1 (London streetwear brands) | 1 (London streetwear brands, #2) |

**Screenshots:**
- `runs/2026-10-18/shots/google_uk__corteiz-alternatives__1.png`: streetwear.directory #1, the AI Overview's Streetwear Directory mention, and Facebook · RETAILBOSS.
- `runs/2026-10-18/shots/google_uk__brands-like-broken-planet__1.png`: the AI Overview.
- The discobrands.co result for "brands like Broken Planet" is below that screenshot. It is recorded in that row's `notes` and `competitors`.

## Sources the AI answers cite most that are not on the authority-research list

These come from Finding 2, with the 18 Oct Google pages added. Neither wings2fashion.com nor rosenberries.co.uk appears anywhere in authority-research's CSV or report.

| Source | AI answers citing it | Google AI Overview source (of 21) | Note |
|---|---|---|---|
| phrasestudios.com | 25 (ChatGPT 20, Gemini 5) | 5 | Authority-research marks it "No" (a brand blog that ranks itself). It is still the most-cited page in the panel. |
| calistudios.co.uk | 11 (Gemini) | 2 | Same: a brand blog |
| wings2fashion.com | 8 (Gemini) | 6 | Not on the authority-research list |
| rosenberries.co.uk | 8 (Gemini) | 0 | Not on the authority-research list |
| flowlikezen.com | 4 (Gemini) | 4 | Brand blog |
| CUOTTI | 4 (Gemini) | 1 | Brand blog |
| Trustpilot | 9 (ChatGPT 4, Perplexity 3, Gemini 2) | 1 | Crooks' own review page |

## Reddit

Authority-research could not check Reddit rankings. The panel did not run the "… reddit" queries it asks for. Even so, Reddit threads rank in Google UK's top 20 for 11 of the 21 panel queries, for example:
- r/ukdrill: Corteiz alternatives, brands like Carsicko and brands like Broken Planet;
- r/streetwearstartup: independent British streetwear (#3) and emerging UK streetwear brands;
- r/mensfashionadvice: heavyweight hoodie UK (#2).

Only one AI answer (Gemini) and one AI Overview cite reddit.com. This is a ranking observation only. The programme has Reddit seeding switched off.

## What this means

- **streetwear.directory** is the only candidate that the panel's AI answers already cite. George approved the free submission on 16 Oct.
- **backwardfashion.com** ranks widely on Google, but no AI answer or AI Overview cited it in these runs.
- **discobrands.co** ranks on one competitor query and is not cited.
- The other five new candidates did not appear anywhere in the panel. They may still matter for queries the panel doesn't cover, so this is not a reason to drop them. It is a reason not to rank them above the sources that are cited.
