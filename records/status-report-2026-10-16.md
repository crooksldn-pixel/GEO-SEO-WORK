<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# CROOKSLDN GEO + SEO programme: status report

**As of:** 16 Oct 2026, 18:00 UTC. Updated at 18:30 and 18:35 UTC with George's confirmed facts and decisions, and on 18 Oct 2026 at 20:50 BST by programme-records (see the Update sections; the newest is first). This is a read-only consolidation: nothing was changed to produce it.
**Sources:** all 10 workstream threads (latest replies 15:34–15:45 UTC), the project chat (including George's 25 answers at 15:33), `master-queue.md`, `change-log.md`, `workstreams/01–10`, `p1-collection-audit`, `measurements/geo-panel`.

**How "live" was checked.** At ~17:55 UTC I read the store back through the Shopify Admin API (collections, products, themes, shop settings). I could not load crooksldn.com itself from this container (network blocked), so anything described as "visible on the live page" comes from the programme thread's own live fetch at 15:36 UTC unless marked **[verified now]**.

**State words used throughout:**
- **Audited:** investigated and written up. Nothing changed.
- **Staged:** built on the unpublished theme copy. Not visible to anyone.
- **Live:** changed in the store or on the published theme, so customers and crawlers can see it.
- **Indexed/ranking:** confirmed in Google data. Nothing has reached this state yet because there is no Search Console data in the project.

No thread is running right now. All ten finished their turn and are waiting on George or on an external event.

---

## Update 18 Oct 2026, 20:50 BST: what went live, what was measured, what's left for you

**Sources:**
- the change log and master queue in `records/` on `cowork/programme-records`;
- `owner-decisions-2026-10-18.md`;
- all eleven `cowork/*` workstream branches as they stood at 20:50 BST;
- Shopify Admin reads at 19:17 and 19:22 UTC.

Nothing was changed on the site to write this. Section C below and its superseded lists are out of date; the list at the end of this update replaces them.

### Live since 16 Oct

| Entry | What | When |
|---|---|---|
| C-009 | Stock tracking off on the 3 tees that were live (90 variants) | 18 Oct ~17:20 UTC |
| IMP-1, IMP-2, IMP-5 | Markets restructured: the US and the Eurozone are now their own markets, and "all world" is rest-of-world only. Test prices unchanged | 18 Oct 18:10 to ~19:05 BST |
| IMP-4 | Channel Islands get free Tracked 48 from £30 | 18 Oct 18:37 BST |
| IMP-7 | International shipping zones rebuilt on real costs | 18 Oct ~19:15 BST |
| IMP-8 | HS codes on 176 variants. Data only: US duty collection isn't switched on | 18 Oct ~19:20 BST |
| TP-1 | 12 Trustpilot replies posted. No visible 1–3★ review is left without a reply | 18 Oct ~18:40–18:55 BST |
| TP-2 | Trustpilot name changed to CROOKSLDN, with the approved brand line as the description | 18 Oct ~19:00–19:10 BST |
| PD-1 to PD-7 | Product data:<br>• stock tracking off on all 21 tees<br>• unconfirmed cotton claims removed, and OG Jeans 14oz<br>• Crewneck and Puffa SEO titles<br>• HydroCuff and Puffa reactive copy<br>• Unisex and Adults on all 45 active products<br>• Puffa colour Black<br>• weights on the sets and 2 tees | 18 Oct 20:10–20:20 BST |

- **Still live from 16 Oct:** C-001, C-002, C-006, C-007 and C-WS02-1.
- **Not live:**
  - C-003: re-approved as decision #13 and routed to collections.
  - C-004, C-005 and C-008: on the held theme copy, parked. Most of their content is live anyway, through the evening theme below.
  - IMP-3 and IMP-6: the USD and EUR catalogs, still in draft.

Each live entry now has a metric, a baseline, and review dates at 4 and 8 weeks (Q36):
- 4-week review: 13 Nov for the 16 Oct changes, 15 Nov for the 18 Oct ones.
- 8-week review: 11 Dec and 13 Dec respectively.

### Changed on 18 Oct with no workstream record

- **New live theme.** "CROOKSLDN — live 18 Oct + evening fixes" became the live theme (created 18:36 UTC, last saved 18:58 UTC). No workstream logged it as its own change. `cowork/live-site-checks` read its files and found three things now live:
  - the Organization schema, with founder, Companies House number, sameAs limited to Instagram and TikTok, and "Crooks LDN";
  - the tee line "Printed to order. Dispatched within 2–3 working days.";
  - a rebuilt popup (teaser bar, with the game opening on press).

  Still open: the tee "IN STOCK" label, the tee schema handling time, and the policies, FAQ and Terms.
- **Store password-locked.** Every storefront URL redirected to /password at 18:35, 20:09 and 20:11 BST. The same URLs were open at 16:30–17:05 BST.
- **T-shirt Week tees active.** 21 tee products are ACTIVE, and 4 of the new ones are on the Online Store. Product-data has since turned stock tracking off on all of them (PD-1).
- **Cream Cap.** It now has 4 photos, a description and an SEO title, so it stays on Google.
- **Footer.** The OUTERWEAR link is now live.

All of this falls inside the first measurement window. The lock days and T-shirt Week are kept out of every before/after comparison.

### Measured (baselines; no improvement is claimed)

- **GEO panel:** run 16 Oct, with an 18 Oct Google UK gap-fill. Google UK 21/21 queries, ChatGPT 63/63 runs, Gemini 63/63, Perplexity 5/63. Crooks is named only when the query contains "Crooks": 0 of 110 readable non-brand AI answers.
- **Search Console:** UK exports for 21 Jan – 22 Jul 2026 and 15–16 Oct 2026. There is no data for 23 Jul – 14 Oct.
- **Merchant Center:** exports from 16 and 18 Oct. All 25 Shopify products are approved for the UK; the only UK disapproval is the Cream Cap. Since then the cap has been given photos and a description, and 20 more products have gone active, which makes 45. The 29 Oct re-export is the next reading.
- **Core Web Vitals:** PageSpeed measured on 16 Oct, mobile and desktop, on 5 URLs. The homepage fails mobile INP.
- **Trustpilot:** 4.2 from 80 reviews on 18 Oct. The 3.3 from 50 used earlier was out of date.

The old GEO 43/50/54 and SEO health 70/74 scores have no recorded method. They're kept only as labelled history.

### Your remaining actions

Everything in `owner-decisions-2026-10-18.md` is treated as answered and isn't asked again. Parked items aren't listed.

1. **The 18 Oct evening launch.** Is the password lock intentional, and when does the store reopen? Which chat or person published the new live theme? This is needed to log it properly and to set the measurement windows.
2. **Themes: one copy at a time.** The current live theme has no backup; the 18 Oct backup is of the old live. Before the next publish:
   - back up the live theme;
   - publish only a copy cut from the current live theme, "live 18 Oct + evening fixes".

   Theme-editor's "approved fixes" copy is stale, and publishing it would undo T-shirt Week and the evening work. The "colour photos" copy edits the same product files as the tee fix (`cowork/theme-editor` FINDINGS 7).
3. **Shopify admin:**
   - untick the pre-ticked marketing box at checkout;
   - paste the approved store description (decision #14) into Online Store preferences, because product-data couldn't type into that field;
   - remove the obsolete ReStock plan from the 3 original tees and Pink Convict Sweats, keeping the CLIVE pre-order on Pink Sweats. The connector lacks the scope for this.
4. **Outreach emails:** read and send the PAUSE and Menswear Style Podcast drafts in team@crooksldn.com.
5. **International pricing (`cowork/international-markets-pricing`):**
   - load the USD and EUR fixed prices and activate both catalogs, by CSV import or by an explicit instruction in that chat;
   - click "Agree and activate" for US duties;
   - read one Gildan label per tee style (for the tee HS codes and origin);
   - treat GG, JE and IM as domestic in CROOKS Shipping.
6. **Trustpilot:**
   - give your go on reporting the two model reviews through Trustpilot support;
   - keep team@crooksldn.com answered, because 11 public replies promise a reply within 1–2 working days.
7. **LinkedIn and Crunchbase:** create both profiles from the ready copy on `cowork/authority-research`.
8. **Directories and GUAP:** give your go on the final Disco and Streetwear Directory listings, and on the GUAP pitch once it's drafted.
9. **Merchant Center:** after the 29 Oct re-check, opt out of auto-add by 1 Nov if core items are still disapproved.
10. **GitHub:** go to Settings, then General, then Default branch, and change it to `main`.

## Update 16 Oct 18:30 UTC: owner-confirmed facts
George confirmed these facts at 18:26. They override the conclusions below wherever the two conflict. The full wording is in `change-log.md` F-001 and in each affected workstream file.

| Area | Before | Now |
|---|---|---|
| Country of origin (P0) | Blocked on records and a remove-now decision | **Resolved.** All products are made in China. Remove the 7 Portugal values and set the customs country to CN. No consumer origin copy. Ready to apply |
| GSM / fabric weight | Blocked on spec evidence; neutralise-or-keep decision open | **Resolved.** Hoodies and joggers 550gsm, 100% cotton; crewnecks and shorts 450gsm; jeans and jorts 14oz. Existing matching claims stay. Ready |
| Overselling tees (was P0) | Stop selling at 0 after shelf counts | **Withdrawn.** All tees are print on demand, so continue-selling is correct. Now a P1 honesty audit covering dispatch wording, feed availability and handling time, and the ReStock plan. It needs the dispatch time |
| Barcodes | Clear after the swing-tag check (batch 2 item 1) | **Reversed.** Item bags carry the codes, so Shopify values stay. Audit whether the bag codes match and whether anything scans them; fix invalid GTINs on the Merchant Center side instead |
| Merchant Center recommendations | Barcode clear in Shopify; origin open | GTIN fix via a Merchant Center rule or supplemental feed; `material` 100% cotton on hoodies and joggers only; tee availability and handling time; Set descriptions may include GSM; no Portugal anywhere |
| Reactive content gates | Fully blocked | **Partly lifted.** HydroCuff: water-triggered, reverts when dry, wash cold, do not iron, "reasonably durable". Puffa: heat-reactive, avoid washing. Reaction time, durability cycles and wash temperatures stay gated |

Nothing new is live because of this update. The completion estimate stays at about 34%.

## Update 16 Oct 18:35 UTC: owner decisions (second batch)
- **Theme copy on HOLD:** the schema (C-004) and popup (C-005) stay staged.
- **Batch 2 approved,** minus barcodes: colours and categories, descriptions (with GSM), Set images, Puffa alt and photo, the cap off the Google channel, and the Judge.me cart widget and Orderify embed off.
- **Gender** is mixed and set per product. **Tracksuits** lists the 3 Convict Sets.
- **Reviews:** not shown. **Mida:** kept. **Partner Hub:** kept. **Orderify:** no campaigns, so prepare removal.
- **About:** not approved yet. "Designed in-house" and "free size swaps" are confirmed.
- **sameAs:** site, Instagram @crooksldn and TikTok @crooksldn only. **Tier-1 samples:** declined for now.

## C. Your remaining action list (revised 18:35, deduplicated)
1. Confirm the gender for each product. The feed thread will send a per-product list (default men's for products with waist sizing) for you to correct, mainly marking which items are women's or unisex.
2. Dispatch time to promise for printed tees: __ working days
3. Does anything scan the item-bag barcodes now, or is that planned: **No / Yes now / Planned**
4. Photos of 3–4 item-bag barcode labels (OG Jeans, one Yard Jeans, one hoodie)
5. The Puffa's base colour (one word)
6. Search Console export (UK, 16 months, Queries and Pages)
7. Merchant Center Products CSV, now and around 30 Oct, plus you (or access) in Merchant Center for the barcode GTIN rule
8. Allow the Mac session card in the measurement thread
9. Paste the Sweats and Denim copy into Shopify, or say how those two collections are managed
10. In the live theme editor: add OUTERWEAR to footer slot 6, and turn off the Judge.me cart widget and the Orderify app embed if the programme thread can't reach the live theme
11. Submit Disco and Streetwear Directory from the pack, then tell us the date
12. Photos: Cream cap, HydroCuff dry and wet, on-body shots, Puffa normal and reacted, plus any reactive video
13. Shipping weights for the 11 products at 0 g
14. Low priority: Trustpilot name and bio; LinkedIn, Crunchbase and Shop-app profiles; start-trading date; what Pink hoodie "V1/V2" means

Parked by your choice, not asked again: theme publish, About approval, review stars, tier-1 samples.

### Superseded list (18:30)


**Quick decisions**
1. Publish the "Claude P1 fixes" theme after a phone check with `?ctc=1`: **Publish / Hold** (schema and popup)
2. Approve product-data batch 2, **without the barcode step**. It covers colours and categories, Set and Express descriptions (now with GSM), Set images, Puffa alt and photo, the cap off the Google channel, and the Judge.me cart widget and Orderify embed off: **Yes / No**
3. Google Shopping gender: **Men's (recommended) / Unisex / Mixed**
4. Should Tracksuits list the three Convict Sets: **Yes / No**
5. Show Judge.me reviews on product pages (three products are rated 1.0): **Yes / No**
6. Is anyone using the Mida recordings: **Yes / No**
7. Does Orderify's dashboard show any live campaigns: **Yes / No**
8. Crooks Partner Hub "creator gift": **Keep / Remove / Unsure**
9. About page copy: **Approve / Send changes**
10. Is "designed in-house" true: **Yes / No.** Is "free size swaps" true: **Yes / No**
11. Are these yours: crooksldn.uk, x.com/crooksuk, TikTok Shop, and any YouTube, Pinterest or Depop profiles
12. Tier-1 samples, 5 Convict hoodies (£300 at retail): **Approve / Decline**
13. The Puffa's base colour (one word)
14. **New:** the dispatch time to promise for printed tees: __ working days
15. **New:** does anything scan the item-bag barcodes now, or is that planned: **No / Yes now / Planned**

**Uploads and tasks**
16. **New:** photos of 3–4 item-bag barcode labels, including OG Jeans, one Yard Jeans and one hoodie
17. Search Console export (UK, 16 months, Queries and Pages)
18. Merchant Center Products CSV, now and again around 30 Oct. The barcode GTIN rule will also need you in Merchant Center, or access for Claude
19. Allow the Mac session card in the measurement thread
20. Paste the Sweats and Denim copy into Shopify, or say how those two collections are managed
21. Add OUTERWEAR to footer slot 6 in the theme editor
22. Submit Disco and Streetwear Directory from the pack, then tell us the date
23. Photos: Cream cap, HydroCuff dry and wet pair, on-body shots, Puffa normal and reacted, plus any reactive demo video
24. Shipping weights for the 11 products at 0 g
25. Low priority: Trustpilot name and bio; LinkedIn, Crunchbase and Shop-app profiles; start-trading date; what Pink hoodie "V1/V2" means

Closed by the 18:26 facts: the swing-tag question, the Portugal remove-now decision, the GSM neutralise decision, tee shelf counts, origin records, spec sheets and OG Jeans weight (read as 14oz), and the core reactive facts.

### Superseded version (16 Oct 17:50, kept for the record)


Everything you already answered on 16 Oct is excluded. These are only the questions and tasks that are still open after the latest thread replies.

**Quick decisions (one word each)**
1. Publish the theme copy "CROOKSLDN — Claude P1 fixes" after checking it on your phone with `?ctc=1`? **Publish / Hold.** This blocks the founder, Companies House and "Crooks LDN" schema, and the softer popup. The copy matches live apart from those two changes, and live hasn't been edited since 13:33. *(You publish it; Claude can't publish themes.)*
2. Approve product-data batch 2? **Yes / No.** It covers barcodes moved to SKU then cleared, colours and Google categories, descriptions for the 3 Sets and the Crooks Express tee, bottoms images on the Sets, Puffa alt text plus its heat-reacted photo, the Cream cap pulled from the Google channel only, and the Judge.me cart widget and Orderify embed switched off. This blocks a clean Merchant Center feed before the 1 Nov opt-out cut-off.
3. Do any printed swing tags or labels carry the 8-digit barcodes? **Yes / No.** This is the last check before the barcodes are cleared.
4. Google Shopping gender for the range? **Men's (recommended) / Unisex / Mixed.** This blocks the gender and age-group feed fields, and a missing gender can disapprove clothing items.
5. Remove the 7 unsupported "Made in Portugal" lines now, while the origin is being established? **Remove now (recommended, reversible) / Wait for records.** This is the P0 trust and compliance item.
6. Until spec sheets exist, neutralise the 550gsm, 450gsm and 14oz claims already on the site (product titles and alt text, homepage meta, the Tracksuits meta, the fit article)? **Neutralise / Keep until evidence.** You said no *new* claims, but the existing ones are still live.
7. Should Tracksuits list the three Convict Sets (Grey, Pink, Black), with /collections/sets folded into it? **Yes / No.** This decides what Tracksuits sells, and it is the collection that gets the most landings from search. Today it lists 6 single pieces that duplicate Sweats.
8. Show Judge.me reviews on product pages, which then allows review stars? **Yes / No.** Note that three products are rated 1.0.
9. Is anyone using the Mida recordings? **Yes / No.** If No, it gets switched off.
10. Does Orderify's own dashboard show any live campaigns? **Yes / No.** If No, it can be uninstalled after the embed goes off.
11. What does Crooks Partner Hub's "creator gift" do, and is it needed? **Keep / Remove / Unsure.**
12. About page copy in `workstreams/06-about-draft.md`: **Approve / Send changes.**
13. Is "every piece is designed in-house" true? **Yes / No.** Is "free size swaps" true? **Yes / No.**
14. Are these yours? **crooksldn.uk** Yes / No · **x.com/crooksuk** Yes / No · **TikTok Shop** active Yes / No · **YouTube / Pinterest / Depop** list any that are Crooks-controlled. Only verified profiles go into the sameAs schema.
15. Tier-1 creator samples, 5 Convict hoodies (about £300 at retail) for UK hoodie reviewers? **Approve / Decline.**
16. Double-Agent Puffa base colour (unheated)? Give one word.

**Uploads and owner tasks**
17. Upload the Search Console export: UK, last 16 months, Queries and Pages, with clicks, impressions, CTR and position. It blocks all query-led work, the Core Web Vitals baseline, index clean-up and every "measured" claim.
18. Upload the Merchant Center Products CSV (Products → All products) now, and again around 30 Oct. It blocks the parity check and the opt-in-or-opt-out call before 1 Nov.
19. Allow the Mac session using the card in the GEO and SEO measurement thread. It blocks the first UK GEO baseline, so all 21 queries currently have no data.
20. Paste the Sweats and Denim copy into Shopify admin from `workstreams/01`, or say how those two collections are managed. They are invisible to Claude's Shopify connection, which only sees empty sweats-1 and denim-1. This blocks the Sweats and Denim copy, the "Heavyweight" Sweats title and the fit-guide links.
21. Add OUTERWEAR to footer link slot 6 in the live theme editor.
22. Enter real shelf counts for CRX Garms and CRXST★RZ by colour and size, and for every Crooks Express size at 0 or below. XS is now at −4. This blocks the P0 oversell fix: the tees ship from stock, so they should stop selling at 0.
23. Submit Disco and Streetwear Directory from `workstreams/07-directory-submission-pack.md` (about 5 minutes each). Stop if a fee appears, then post the date in the authority thread.
24. Supplier or customs records (invoice or packing list) showing the country of manufacture for each product.
25. Supplier spec evidence for 550gsm, 450gsm and 14oz, plus the OG Jeans weight in oz.
26. Reactive garment facts from supplier or test data, for both HydroCuff and Puffa: trigger, reaction time, reversibility, durability, wash care and whether the effect degrades. Add a demo video if one exists.
27. Photos, uploaded to `seo/assets/incoming`: the Cream cap first, a HydroCuff dry and wet pair with identical framing, on-body shots, and Double-Agent normal and reacted states.
28. Shipping weights for the 11 products currently at 0 g (international rates are weight-based).
29. Low priority: rename the Trustpilot profile to "CROOKSLDN" and add a bio; set up LinkedIn, Crunchbase and Shop-app profiles under Crooks Clothing Company Ltd; give the start-trading date from your records; say what Pink hoodie "V1/V2" means.

---

## A. Executive status

27 tracked items: the 22 you listed plus 5 discovered during the programme. Each is counted once, under its main status.

| Status | Count | Items |
|---|---|---|
| Completed (no further work needed now) | 3 | Product JSON-LD audit (already correct), ProductGroup/variants (already correct), query research and map |
| Live, waiting on Google, AI or third parties | 1 | Outerwear collection plus the Tracksuits title and link (live 16 Oct) |
| Partly done | 2 | Core Web Vitals (code audit only, no field data), monitoring (weekly Shopify routine scheduled, first run 19 Oct) |
| Ready to restart (resolved 18:26) | 5 | Country of origin, GSM claims, tee print-on-demand honesty audit, barcode compatibility audit, reactive copy |
| Blocked or waiting on George | 11 | Collections (Sweats/Denim access, footer, Tracksuits decision), Merchant Center feed, Search Console, About page, Organization schema (staged), directories, images, popup (staged), apps, GEO panel, review stars |
| Not started | 5 | Commercial content pages, editorial and creator outreach, index hygiene, Trustpilot reputation, shipping-wording and currency parity |

**Estimated programme completion: about 34%.** This is progress through the programme's own pipeline, not SEO results. It is weighted as follows:
- **Research and audit, 25% weight:** 100% done (10 of 10 audits) = 25 points.
- **Implementation, 50% weight:** 3 of about 49 master-queue actions are live, about 6% = 3 points. Two more (the schema batch and the popup) are staged but not live; publishing the theme copy would add about 2 points.
- **Measurement baselines, 25% weight:** 1 of 4 signals exists (Shopify analytics; Search Console, the GEO panel and Merchant Center data are missing) = 6 points.

On outcomes, **0% is proven.** No ranking, indexing, Shopping or AI-mention change can be shown yet, because neither Search Console nor a GEO baseline exists. The old GEO 43→54 and SEO 70→74 scores have no recorded method, and the measurement thread marked them non-comparable.

---

## B. Changes that are live now

These are the only changes from this programme that a customer, Googlebot or an AI crawler can encounter today.

| # | What changed | Where | When | Verified | Expected effect |
|---|---|---|---|---|---|
| 1 | New Outerwear collection (smart rule: type = Outerwear) holding HydroCuff Windbreaker (£85) and Double-Agent Puffa (£140). SEO title "Water-Reactive & Heat-Reactive Jackets", meta description and short body copy | /collections/outerwear | 16 Oct ~15:40 UTC | Admin **[verified now]**: 2 products, published, SEO fields set. Page render: per the programme thread's 15:36 fetch | Gives "water reactive jacket" and "heat reactive puffer" queries a category page to land on. Watch for impressions on this URL 4–8 weeks after indexing. Today it has 0 search sessions |
| 2 | Double-Agent Puffa: product type blank → "Outerwear"; tags outerwear, heat-reactive, puffer | /products/double-agent-puffa (data, plus the Shopify feed) | 16 Oct ~15:40 | **[verified now]** | Lets it join Outerwear; product type flows to the Google channel |
| 3 | OUTERWEAR added to the SHOP dropdown in the main menu | Site-wide header | 16 Oct ~15:40 | Per the 15:36 thread fetch (menu not re-read now) | Internal link from every page, so crawlers find the new collection |
| 4 | Tracksuits SEO title → "Heavyweight Tracksuits: Matching Fleece Sets". It briefly read "…550gsm Fleece Sets" until about 16:00, when 550gsm was removed for lack of evidence. A sentence linking to /collections/sweats was added to the description | /collections/tracksuits | 16 Oct 15:42, title corrected about 16:00 | **[verified now]**: title. Link per the thread | Targets "heavyweight tracksuit UK" and adds a Tracksuits→Sweats link. Note that the collection still lists 6 single pieces, not the Sets (item C7) |

Changes made **outside this project** on 16 Oct (seen, details unknown): someone edited /collections/denim (title, copy, products), published the live theme "CROOKSLDN — SEO round 2" (13:33 UTC), and published the "Convict vs Cellblock" fit article at /blogs/news/convict-vs-cellblock-fit.

**Not live (staged on the unpublished theme copy):** the Organization/Brand/WebSite schema update (C-004) and the popup change (C-005). **Not live (not applied):** everything else in this report.

---

## D. Next autonomous work (ranked by ROI)

**Can execute now (no input needed)**
1. **Shipping-wording parity check (Q20, research).** Product pages say "Free UK Tracked 24 included" on £60 items, while the policy and FAQ say free from £80, and checkout and schema say £3 with free shipping from £30. This is a customer promise and a Google Merchant shipping mismatch risk.
2. **Schema currency check (Q18, research).** `priceCurrency` follows `cart.currency`, so a US-based crawl may see USD while Merchant Center has GBP. This can be partly checked from the theme code; full proof needs URL Inspection.
3. **Change-log hygiene (Q36).** Add the metric and the 4- and 8-week review dates to C-001 to C-005, and stop citing the old scores.
4. **Pre-write the Sweats and Denim copy into a ready-to-paste block with GSM and origin removed.** This is already done for Sweats; check Denim against the edit made outside the project today.
5. **Second-pass authority research** (national press, grime and music titles), which hit search limits the first time. Research only, with no contact.

**Can audit or prepare now, but can't deploy yet**
- **Batch 2 store changes (Q8–Q12, Q14 toggles):** fully specified and ready to apply the moment you approve (C2, C3).
- **Organization schema and popup:** done on the theme copy. They wait on your phone check and publish (C1).
- **Gender and age-group feed fields:** prepared, waiting on the gender value (C4).
- **About page and AboutPage JSON-LD:** drafted, waiting on approval (C12, C13).
- **Search Console analysis** (positions 5–20, low CTR, cannibalisation, index hygiene, CWV baseline): the method is written and waits on the export (C17).
- **Merchant Center opt-in check:** the feed thread says it will check on 29 Oct and needs the CSV (C18).
- **GEO panel:** the runbook and results format are ready, and it waits on the Mac session (C19).
- **Visible collection breadcrumbs and a homepage category link row (Q43):** these need a design review and a theme port, so they're lower value.

---

## Per-workstream detail

### 1. Collection architecture and internal linking (WS01, P1)
- **Done:** audited 16 Oct (`p1-collection-audit-2026-10-16.md`, `workstreams/01`). The audit was corrected after recheck: the homepage title and meta, the menu URLs, and the collection JSON-LD (CollectionPage, ItemList, BreadcrumbList) were already fine. Outerwear and the Tracksuits title are live (see B).
- **In progress:** nothing running.
- **Waiting on George:** C20 (Sweats and Denim copy cannot be applied by API; approved 15:33 but **not applied**, C-003), C21 (footer slot), C7 (Tracksuits to list the Sets).
- **External:** indexing of /collections/outerwear and the new Tracksuits title.
- **Not started:** visible breadcrumbs (P3), collection-to-guide links (P3, partly blocked by Sweats access), Tees copy (P4, revisit at the tee drop).
- **Expected impact:** category pages are the brand's weakest layer. Only 6.2% of organic sessions reach any product or collection page.

### 2. Outerwear and collection copy (WS01, P1)
- **Done and live:** Outerwear collection, Puffa type and tags, menu link, Tracksuits title and Sweats link (C-001, C-002). Validated by Admin read-back and the thread's live fetch.
- **Remaining:** Sweats and Denim copy (C20), footer (C21).
- **External:** Google recrawl and indexing. No Search Console data exists to confirm it.

### 3. Product structured data (WS02, P2)
- **Audited:** the PDP JSON-LD is already sound. It has ProductGroup, `hasVariant`, `variesBy`, per-variant Offers, price, availability, UK shippingDetails and returns. **No schema code change is needed.** The work is store data.
- **Open:** Q18 currency check (D2); aggregateRating waits on C8; the `color` fallback is part of the staged theme batch (Q13, being ported).
- **Expected impact:** cleaner Shopping and AI product understanding once the data gaps (colour, gender, descriptions) are fixed.

### 4. Product variants / ProductGroup (WS02)
- **Completed (pre-existing):** already modelled correctly by the theme before this programme; the audit verified it in code. Only a P4 note remains: what Pink hoodie "V1/V2" means (C29).

### 5. Merchant Center feed parity (WS03, P0 for the deadline)
- **Audited:** 25 products and 244 feed variants were compared against the site and JSON-LD; 11 findings are in `03-merchant-feed.md`, and the fixes in `03-merchant-feed-handoff.md`. Shipping already matches (£3, free from £30).
- **Decision on file:** opt in to Google's 2 Nov auto-add only if the feed is clean. No Merchant Center action is needed to opt in (it's the default); you opt out by 1 Nov if it isn't clean.
- **Waiting on George:** C2 (batch 2), C4 (gender), C18 (CSV now and about 30 Oct), C16 (Puffa colour), C27 (cap photo).
- **Not applied:** Shopping-style titles and `is_bundle`, which are Merchant Center-only and wait for the CSV.
- **[verified now]:** no feed fix has been applied yet. Colour is still missing, the cap has 0 images, and the 3 Sets have no description.

### 6. Inventory / overselling (WS02, P0)
- **Verified by WS02:** the tees are **not** printed to order. [n] orders since 31 Aug all shipped from stock within about a day. Under your rule, they should stop selling at 0.
- **[verified now]:** CRX Garms is at 0 and CRXST★RZ at −2 overall, and Crooks Express XS is at −4. All three are set to keep selling when out of stock. The legacy ReStock plan is still attached, which causes the "recurring purchase" notice at checkout.
- **Waiting on George:** C22 (real shelf counts). Then the fix takes about 10 minutes.

### 7. Barcodes / product identifiers (WS02/03, P1)
- **Verified:** iPacky was a trial uninstalled on 30 May; there's no warehouse, 3PL or scanner; fulfilment is manual with Royal Mail labels. The codes are the last 8 digits of the variant ID, and 5 of them are shared across all denim products. **[verified now]:** still present, and SKUs are mostly empty.
- **Waiting on George:** C3 (printed tags), then C2.
- **Plan:** copy each code into SKU, then clear the barcode. Nothing is lost.

### 8. Country of origin (discovered, P0)
- **Found:** 7 "Made in Portugal" values (Grey Convict Sweats, both Yard Jeans, both Yard Jorts, Cellblock Crewneck and Shorts) were added in one bulk edit on 6 Aug. Nothing in the inbox or Drive supports them. Customs data says China on 6 products. These values flow into page schema.
- **Waiting on George:** C5 (remove now or wait), C24 (records).

### 9. GSM / fabric-weight claims (discovered, P1)
- **Done:** "550gsm" was removed from the Tracksuits title; GSM and Portugal were stripped from the Sweats draft; the query map holds no new GSM targets.
- **Still live:** 550gsm, 450gsm and 14oz appear in product alt text and titles, the homepage meta, the Tracksuits meta and the fit article. **Waiting on George:** C6, C25.

### 10. Search Console analysis (WS04, P1)
- **Done:** a proxy analysis from Shopify. 92.9% of 3,910 organic sessions (90 days) land on the homepage, which suggests branded traffic. Search brought [n] orders worth £[redacted] in 90 days. /password and thin URLs are also picking up search entries. The crooksldn.com Domain property was verified at 14:22 on 16 Oct.
- **Waiting on George:** C17. Every query-level decision waits on it.

### 11. Query research (WS05)
- **Completed:** `05-query-map.md`, one URL per intent. **No new pages are justified yet.**
- **Updated with your answers:** Cellblock is a co-ord, not a tracksuit; reactive and GSM content is gated on evidence; "Made in Portugal" is dropped as a target.

### 12. Commercial-intent content (P4 in the brief, not started)
- **Not started, by evidence:** the 550gsm, fit and sizing intents are served by the existing fit article (published outside the project today), product tables and the FAQ. "Baggy jeans UK" would be a one-product thin page. "Best UK streetwear" and "brands like Corteiz" go to the About page and external editorial instead.
- **Blocked:** the reactive garments guide (C26) and the "is 550gsm heavy?" addition (C25). Revisit once the Search Console export shows real queries.

### 13. About and entity architecture (WS06, P1)
- **Done:** entity audit (`06-entity.md`); brand definition and About draft from your approved facts (`06-about-draft.md`).
- **Waiting on George:** C12, C13, C14. Then it gets built at /pages/about with AboutPage JSON-LD and footer and menu links.
- **Not live:** there is still no About page. **[verified now]:** the shop description is still blank (Q21, which feeds the Organization description, is ready but not applied).

### 14. Organization / OnlineStore schema (WS06 → WS01)
- **Staged, not live (C-004):** on the unpublished theme copy. It adds "Crooks LDN" to alternateName, founder George Hinxman, Companies House 16606021 and addressCountry GB, and uses your brand line as the fallback description. The Liquid compiles and the checksum matches. **Not tested:** the rendered JSON-LD. A Rich Results Test is needed after publish.
- **Waiting on George:** C1. OnlineStore type is P4. sameAs additions wait on C14.

### 15. External authority and editorial (WS07, P1–P2)
- **Done:** 222 opportunities scored and ranked, with pitch angles drafted (`07-authority.md`). Nothing has been contacted.
- **Not started:** press and podcast outreach (it waits for the About page to be live, plus your approval per contact), creator seeding (C15), and later-stage titles (which need the reactive video and evidence).

### 16. Directory submissions (WS07)
- **Approved and prepared:** Disco is confirmed free and reviewed by hand, typically in 5–7 days. Streetwear Directory is curated with no fee found. The pack uses approved facts only.
- **Waiting on George:** C23. You submit, since cloud threads can't reach either site.
- **External, afterwards:** each directory's review; profile URLs get logged in the tracker.

### 17. Visual and image search (WS08, P1–P2)
- **Audited:** the image code is solid; the gaps are content. The Sets show only the top, the cap has no image, the Puffa's alt text is empty **[verified now]** and its heat-reacted photo isn't attached. An upload folder has been set up (`seo/assets/`).
- **Waiting on George:** C2 (set images, Puffa alt and photo), C27 (shoots).

### 18. HydroCuff / reactive products
- **Live:** they now have the Outerwear collection hub (B1).
- **Waiting on George:** C26 (facts), C27 (dry and wet pair, Puffa states, video). No technical claims will be written until then.
- **GEO weight:** high, since reactive outerwear is the brand's most distinctive attribute for AI answers.

### 19. Core Web Vitals (WS09, P1 baseline / P3 trimming)
- **Audited (code only):** lazy loading, priority images, fonts and render-blocking are already handled; crawl settings and canonicals are fine. **There is no field or lab data**, because the PageSpeed quota is exhausted, CrUX needs a key and the site is unreachable from here.
- **Not started:** CSS and JS trimming, which waits on a baseline from the Search Console CWV report (C17).

### 20. Mobile popup (WS09 → WS01)
- **Staged, not live (C-005):** opens no sooner than 10 seconds and only after 50% scroll (or on a return visit or desktop exit intent). On phones it's a bottom sheet of at most 40% height with no scroll lock and a large ×; closing it hides it for the session, and NOT NOW hides it for 14 days. Analytics events were added. The JS passes a syntax check. **It has not been browser-tested.**
- **Waiting on George:** C1, with the phone preview.

### 21. Third-party apps and scripts (WS09)
- **Audited:** Orderify looks unused (no data on the shop or products, and none of the last [n] orders). Judge.me's cart widget is dead, because there's no cart drawer. Judge.me collects reviews but doesn't display them. Mida loads on every page. Shopify Forms and Omnisend are in use.
- **Waiting on George:** C2 (both toggles), C9, C10, C11. A manual review of Settings → Customer events and ScriptTags is also still to do, and is folded into C11.

### 22. GEO query panel (WS10, P1)
- **Done:** a repeatable runbook, query list and fixed CSV results format (`measurements/geo-panel/`). The Mac session brief is written.
- **Waiting on George:** C19. The request card is still pending, so no baseline exists for any of the 21 queries.

### 23. SEO/GEO monitoring system (WS10)
- **Done:** a Shopify baseline (90 days): Google organic 3,799 sessions and [n] orders worth £[redacted]; AI assistants sent 3 referrals in a year. A weekly routine is scheduled for Mondays 08:52 London; its first run is 19 Oct and it writes `seo/measurements/shopify-weekly.md`.
- **Remaining:** add the Search Console and GEO panel signals once C17 and C19 land.

### Other discovered work
- **Index hygiene (P2, not started):** /password, /collections/frontpage (in the sitemap), /collections/all, the -1 duplicates, and 5 archived products returning 404 with no redirect. Waiting on C17 to confirm impressions.
- **Trustpilot (P1, not started):** scored 3.3 from 50 reviews, which AI answers quote. Fixing it needs your access (replies, the official invitation flow, the profile name; C29).
- **Shipping wording parity and currency (P2):** see D1–D2.
- **Shipping weights (P3):** C28.

---

## Master table (highest commercial and GEO impact first)

| Priority | Workstream | Status | What is done | What remains | Waiting on | Next action |
|---|---|---|---|---|---|---|
| P0 | Merchant Center feed (1 Nov) | Blocked | Audit, 11 findings, handoff | Apply batch 2, gender, then check the CSV | George: C2, C4, C18 | Approve batch 2 |
| P1 | Tees (print on demand) | Ready to restart | Corrected 18:26: POD, continue-selling is correct | Dispatch wording, feed availability and handling time, ReStock check | George: C14 (dispatch time) | Audit setup |
| P0 | Country of origin | Ready to restart | Resolved 18:26: all China | Remove 7 Portugal values, customs CN | None | Apply (store write) |
| P1 | Collections + internal linking | Partly live | Outerwear and Tracksuits title live | Sweats and Denim copy, footer, Tracksuits Sets | George: C7, C20, C21 | Paste copy or explain access |
| P1 | Barcodes | Ready to restart (audit) | Bags carry codes, so do not clear | Match bag codes, Merchant Center GTIN rule | George: C15, C16 | Audit compatibility |
| P1 | Organization schema | Staged | Built on the theme copy | Publish, then Rich Results Test | George: C1 | Phone preview and publish |
| P1 | Mobile popup | Staged | Built on the theme copy | Publish, then measure signups | George: C1 | Phone preview and publish |
| P1 | About / entity | Blocked | Audit and draft | Approve, build page and JSON-LD | George: C12–C14 | Approve copy |
| P1 | Search Console | Blocked | Shopify proxy analysis | Full opportunity analysis | George: C17 | Upload export |
| P1 | GEO panel | Blocked | Runbook and format | First UK baseline | George: C19 | Allow Mac session |
| P1 | Directories | Blocked | Pack ready, both checked free | Submit, log URLs | George: C23 | Submit forms |
| P1 | Reactive products | Ready to restart (copy) | Outerwear hub live; core facts confirmed 18:26 | HydroCuff and Puffa PDP copy, guide draft, photos | George: C23 photos | Draft copy |
| P1 | GSM / composition | Ready to restart | Resolved 18:26: weights and 100% cotton confirmed | Copy and feed parity; optional 550gsm on Tracksuits | None | Audit copy, set material |
| P1 | Images | Blocked | Audit; upload folder | Set images, Puffa, shoots | George: C2, C27 | Approve batch 2 |
| P1 | Trustpilot | Not started | Score checked (3.3) | Replies, invites, profile | George: access | Owner task |
| P2 | Apps / scripts | Blocked | Audit | Toggles off, Mida, Orderify uninstall | George: C2, C9–C11 | Answer Mida and Orderify |
| P2 | Editorial / creator outreach | Not started | 222 targets, pitches | Pitch, seed | About live; George: C15 | Approve tier 1 |
| P2 | Review stars | Blocked | 37 reviews found | Show on PDPs, aggregateRating | George: C8 | Yes / No |
| P2 | Index hygiene | Not started | Issues listed | Confirm and redirect | Search Console export | After C17 |
| P2 | Shipping and currency parity | Not started | Mismatch spotted | Verify, fix wording | None | Research now |
| P1 base / P3 trim | Core Web Vitals | Partly done | Code audit | Field baseline, then trims | Search Console export | After C17 |
| P2 | Monitoring | Partly done | Shopify baseline, weekly routine | Add Search Console and GEO signals | First run 19 Oct; C17, C19 | Automatic |
| P4 | Commercial content pages | Not started (by evidence) | Query map: no new pages yet | Reactive guide; revisit with data | C25, C26, C17 | Wait |
| — | Product JSON-LD / ProductGroup | Completed | Verified correct | Currency check (Q18) | None | Research |
| — | Query research | Completed | Map with your answers | Refresh when data lands | Search Console export | — |
