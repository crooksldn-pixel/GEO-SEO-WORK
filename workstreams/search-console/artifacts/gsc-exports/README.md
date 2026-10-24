# Search Console exports

Property `sc-domain:crooksldn.com`, search type Web, country filter United Kingdom on every file. Read from the Search Console UI by the search-console workstream.

The property has no performance data for 23 Jul – 14 Oct 2026, so "16 months" in Search Console really means 21 Jan – 22 Jul 2026, and the `28d` files (read 18 Oct) hold only 15–16 Oct 2026. Files named `2026-10-15_to_22` were read on 24 Oct. See `../../FINDINGS.md`, Finding 1.

| File | Window | What it is | Rows |
|---|---|---|---|
| `gsc_uk_16m_queries.csv` | 21 Jan – 22 Jul 2026 | Queries tab: clicks, impressions, CTR, position | 270 |
| `gsc_uk_16m_pages.csv` | 21 Jan – 22 Jul 2026 | Pages tab | 24 |
| `gsc_uk_16m_dates.csv` | 21 Jan – 22 Jul 2026 | Daily totals (property total: 14,312 clicks, 35,948 impressions) | 183 |
| `gsc_uk_compare_H1_vs_H2_queries.csv` | 21 Jan – 21 Apr vs 22 Apr – 22 Jul 2026 | Queries in both halves, with differences | 270 |
| `gsc_uk_compare_H1_vs_H2_pages.csv` | same | Pages in both halves | 24 |
| `gsc_uk_16m_query_page_breakdowns.csv` | 21 Jan – 22 Jul 2026 | Which URL Google showed for each query cluster (page filter → queries, or query filter → pages) | 90 |
| `gsc_uk_28d_queries.csv` | 15–16 Oct 2026 | Queries tab, first days after the gap | 25 |
| `gsc_uk_28d_pages.csv` | 15–16 Oct 2026 | Pages tab | 22 |
| `gsc_uk_28d_dates.csv` | 15–16 Oct 2026 | Daily totals | 2 |
| `gsc_uk_2026-10-15_to_22_queries.csv` | 15–22 Oct 2026 | Queries tab, first post-gap week (read 24 Oct) | 56 |
| `gsc_uk_2026-10-15_to_22_pages.csv` | 15–22 Oct 2026 | Pages tab (two Merchant free-listing URLs shortened to their `?variant` + `utm_source/utm_content`) | 30 |
| `gsc_uk_2026-10-15_to_22_dates.csv` | 15–22 Oct 2026 | Daily totals, each day labelled (anchor, deploy, lock, T-shirt Week) | 8 |
| `gsc_uk_2026-10-15_to_22_query-crooks_dates.csv` | 15–22 Oct 2026 | The query "crooks", by day | 8 |
| `gsc_uk_2026-10-15_to_22_page-frontpage_dates.csv` | 15–22 Oct 2026 | /collections/frontpage (a brand sitelink), by day | 8 |
| `gsc_uk_2026-10-15_to_22_query_page_breakdowns.csv` | 15–22 Oct 2026 | Which URL Google showed for each product cluster | 23 |
| `gsc_index_reasons_2026-10-16_snapshot.csv` | report dated 16 Oct 2026 | Indexing > Pages: the 7 "why pages aren't indexed" reasons, page counts and what the example URLs are | 7 |
| `gsc_indexed_pages_2026-10-16_snapshot.csv` | report dated 16 Oct 2026 | All 43 indexed URLs | 43 |

Notes:
- Query rows cover only queries Google discloses. In the Jan–Jul window, 1,948 clicks and 7,257 impressions were anonymised, so query rows sum to less than the daily totals.
- Page rows sum to more than the daily totals because one search can show several URLs (sitelinks).
- One 15–16 Oct page row was dropped: its URL contained a query string that could not be read back safely.
- Positions are Search Console averages. In the comparison files, a blank position means no impressions in that half.
