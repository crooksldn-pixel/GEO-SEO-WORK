<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 4: Search Console opportunity analysis

Status: **Blocked on data access** (16 Oct 2026). Read-only workstream; no changes made.

## Current state

- **No Search Console data is reachable from this project.** Checked 16 Oct 2026:
  - No Search Console connector exists in the claude.ai connector directory or is installed.
  - gcloud/BigQuery: no credentials, so no GSC bulk export can be read.
  - Google Drive: no Search Console export found (search for "Search Console", "Queries", performance exports).
  - Project files: no GSC export uploaded.
  - User's Mac: no folder connected to this thread.
- **The crooksldn.com Domain property was only verified today.** Gmail (team@crooksldn.com) has a Search Console email dated 16 Oct 2026 13:22 UTC: "you recently verified this Domain property". Google normally shows past performance data for a newly verified property, but this is unconfirmed until someone opens the report.
- Nothing below about queries, positions, CTR or cannibalisation is known yet. No such data has been invented.

## Evidence available now (proxy: Shopify analytics, read-only)

Shopify sessions with referrer source = search, by landing page. Last 90 days to 16 Oct 2026 vs the previous 90 days.

| Landing page | Search sessions (90d) | Previous 90d | Conv. rate (90d) |
|---|---|---|---|
| / (homepage) | 3,631 | 2,157 | 2.2% |
| /collections | 74 | 0 | 2.7% |
| /password | 36 | 919 | 0% |
| /collections/tracksuits | 22 | 0 | 0% |
| /collections/frontpage | 13 | 0 | 0% |
| /products/hydrocuff-windbreaker | 13 | 0 | 7.7% |
| /products/black-joggers | 13 | 43 | 15.4% |
| /collections/all | 12 | 1 | 0% |
| /products/cb2-wash-jorts | 10 | 9 | 0% |
| /collections/tees | 9 | 0 | 0% |
| /products/blue-wash-yard-jeans | 8 | 0 | 12.5% |
| /products/v2-baggies | 8 | 2 | 0% |
| /collections/sweats | 6 | 0 | 0% |
| /collections/new | 6 | 0 | 0% |
| /collections/denim | 3 | 0 | 0% |
| /collections/denim-1 (legacy handle) | 1 | 0 | 0% |
| All search landings | 3,928 | ~3,150 | |

Other facts from the same source:
- Organic search sessions by month: Mar 248 (store's first month with data), Apr 1,424, May 1,911, Jun 231, Jul 1,116, Aug 983, Sep 1,742, Oct 1–16 768. Search conversion rate 1.3–2.7% by month.
- Search engines, last 90 days: Google 3,799, Bing 99, Ecosia 11, Yahoo 11, DuckDuckGo 9. ChatGPT referrals: 2.
- Orders attributed to search referrer, last 90 days: [n] orders, £[redacted]. ([n] orders, £[redacted] have no referrer recorded, so search's true share is likely higher.)

What this shows (inferred, not GSC-confirmed):
1. **~92% of organic search sessions land on the homepage.** That pattern almost always means branded queries ("crooks ldn"). Non-branded discovery through collection and product pages is close to zero: the four priority collections got 6, 9, 3 and 0 search sessions in 90 days (/outerwear does not appear).
2. **Some product pages convert well from search on tiny volume:** black joggers 15%, blue wash yard jeans 12.5%, Hydrocuff windbreaker 7.7%. These are the pages worth pushing up for non-branded queries first.
3. **/password got 919 search sessions in the previous period.** The store was likely password-protected for a stretch (the June dip to 231 sessions fits). Google may still hold the /password URL; check it is not indexed once GSC is open.
4. **Thin/duplicate collection URLs are getting search entries:** /collections, /collections/frontpage, /collections/all, /collections/denim-1. Possible index bloat and diluted signals for the real category pages; confirm with GSC's Pages report.

## Affected URLs/files

/, /collections/sweats, /collections/denim, /collections/tees, /collections/outerwear, /collections/tracksuits, /collections/frontpage, /collections/all, /collections/denim-1, /password, /products/black-joggers, /products/blue-wash-yard-jeans, /products/hydrocuff-windbreaker, /products/v2-baggies. No files touched.

## Opportunities (ranked)

| Rank | Action | Commercial impact | SEO impact | GEO impact | Effort | Confidence | Dependencies | Status |
|---|---|---|---|---|---|---|---|---|
| **P0** | Get GSC data into the project (see "How to unblock") | Unlocks every query-level decision in workstreams 1, 2, 5 | Prerequisite | Prerequisite | 5 min for the user | High | User action | Waiting on user |
| **P1** | Once data lands: pull queries at positions 5–20 with ≥50 impressions, map each to its best URL, and hand the list to workstream 1 (collections) and 5 (content) | Highest: these are the queries closest to page one | High | Medium (AI answers lean on pages that already rank) | Small | Medium until data is seen | P0 | Not started |
| **P1** | Measure the branded vs non-branded split from GSC queries and set the baseline in the change log | Sets the KPI the whole programme is judged on | High (measurement) | Medium | Small | High | P0 | Not started |
| **P2** | Check whether /password, /collections/frontpage, /collections/all, /collections/denim-1 and the -1 smart collections are indexed; recommend noindex/redirect/canonical fixes to workstream 1 | Medium: consolidates signals onto the real category URLs | Medium | Low | Small | Medium (traffic shows they are reachable from search) | P0; workstream 1 owns the theme | Not started |
| **P2** | Cannibalisation check: queries where 2+ URLs get impressions (e.g. denim vs denim-1 vs baggies product; homepage vs collections) | Medium | Medium | Low | Small | Low until data is seen | P0 | Not started |
| **P2** | Low-CTR check: pages with high impressions and CTR below expected for their position; feed title/meta proposals back with the query evidence | Medium | Medium | Low | Small | Low until data is seen | P0 | Not started |
| **P3** | Declining pages: compare last 3 months vs previous 3 in GSC | Low now: the store is ~7 months old with little non-branded history | Low | Low | Small | Low | P0 | Not started |

Expected commercial impact overall: search already brings ~80 attributed orders / £[redacted] per quarter, almost all branded. The upside is non-branded traffic to collections and best-converting products, which today is near zero.

## How to unblock (simplest first)

1. **An export is enough; no account access is needed.** In Search Console, open crooksldn.com → Performance → Search results, set Date to "Last 16 months" (or the longest available), then Export → Download CSV (or Google Sheets). Upload the zip/CSVs in this thread. Do the same with "Compare: last 3 months vs previous 3 months" if you can.
2. If you choose Google Sheets: the sheet lands in the Drive of whichever Google account is signed into Search Console. The Drive this project reads may be a different account, so either share the sheet with that account or just upload the CSV here.
3. Optional, for ongoing monitoring (workstream 10): enable Search Console's BigQuery bulk export, or connect a reporting tool. This needs a Google Cloud project and is a bigger decision; not needed to start.

## Recommended implementation

None yet. This workstream stays read-only. When the export arrives: run the P1 analyses, update this file with the query tables, and pass URL-level recommendations to workstream 1 (collections) and 5 (content) rather than editing anything directly.
