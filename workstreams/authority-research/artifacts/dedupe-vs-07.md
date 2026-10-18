# Dedupe: second pass vs 07-authority (first pass)

**Source for 07:** `cowork/project-files-import` → `project-files/seo/workstreams/07-authority.md` (222 deduplicated opportunities, sanitised copy).  
**Matched:** 18 Oct 2026. Rows are matched by registrable domain, then checked by outlet name, which catches 07's merged "Also:" entries.  
**For the outreach workstream (owner of 07):** the `in_07` column in `authority-targets-second-pass.csv` is the merge key. "new" rows are additions. For rows with a 07 ID, this pass adds verified routes, fresher evidence or a rescore, as noted below.

## Second-pass targets (§1.1)

**21 of the original 47 are new.** Most come from 07's own "Gaps" list:

| Group | Outlets |
|---|---|
| Mainstream (07 gaps) | IndyBest, Guardian, Evening Standard, BBC, Hunger, Notion, Crack, Link Up TV, GRM Daily |
| Music and culture titles | Mixtape Madness (news and video), Trench, Rolling Stone UK |
| Ranking directory | fastfashionnews.co.uk |
| Business press | FT |
| Student press | The Gryphon, The Courier, Redbrick, Glasgow Guardian |

**26 overlap with 07.** Where this pass changes something, it's listed here:

| 07 ID | Outlet | What this pass adds or changes |
|---|---|---|
| A004 | Complex UK (Brand to Watch; JP's UK Culture Picks merged in) | JP's column re-verified (10 Jun 2026 issue leads on Trapstar and Corteiz). The two angles are split into separate rows. |
| A025 | GUAP | Route contact@guap.co.uk, from /about |
| A040 | Clash | Fashion Editor and Fashion Director named on /contact-clash/; press@ for general. Rescored for a text-only pitch (L2). |
| A055 | British GQ | Peer coverage evidenced (Corteiz, Represent) |
| A006 | backwardfashion | Up and Coming slot criterion verified (under 100k Instagram followers). Ranks for 6 of 10 proxy queries. |
| A001 / A003 | Disco / Streetwear Directory | GEO panel: Streetwear Directory is ChatGPT's only cited source for "brands like Corteiz", and Gemini cites Disco. Owned by outreach. |
| A005, A007 | FashionBeans, Ape to Gentleman | Rescored for text-only pitches (no samples). L1, low priority. |
| A008, A020 | retailboss, apartstyle | Fresh dates (Feb 2026; Aug 2026) |
| A211 | The Tab | tips@thetab.com verified 18 Oct |
| A109 | Shift London | 07 has only the Substack newsletter (unverified). This pass adds the site and editor@shiftlondon.org, plus the 2023 Corteiz piece. |
| A022 | The Mancunion | Adds a 2021 small-brand Q&A precedent and the desk route |
| A015/A024/A034, A032/A145, A033, A188, A056, A019, A027, A062, A214 | Highsnobiety, Hypebeast, i-D, Dazed, Vogue, Sneaker Freaker, Sole Supplier, City AM, Varsity | Evidence and routes re-checked. No change in priority. |

## Journalist-request platforms (§1.2 vs 07's six)

| Platform | 07 | This pass (verified 16 Oct 2026) |
|---|---|---|
| Qwoted | A217 "free tier limits not shown" | Free Basic plan: 2 pitches a month, with a 2-hour delay |
| ResponseSource | A218 paid | Confirmed paid (from about £625 per category a year). Excluded. |
| Featured | A219 "pricing not shown" | Free plan "Free forever", with a daily allowance |
| JournoLink | A220 "confirm pricing" | **Paid only**: from £59 a month, no free plan. Excluded. |
| SourceBottle | A221 | Free tier; mainly Australia, NZ and Singapore |
| MentionMatch | A222 | B2B writers only. Irrelevant. |
| **#journorequest on Bluesky** (Dot Star Media's free feed) | not in 07 | **New**: free, a clean UK feed |
| **The Source Radar** | not in 07 | **New**: free feed tier. Fashion and retail are among its top categories. |
| **HARO (Featured) / Connectively.us** | not in 07 | **New**: free email digest, US-heavy |
| **Source of Sources** | not in 07 | **New**: free, US-heavy |

07's queue row 18 already covers #journorequest on X.

## Points where this pass disagrees with 07

**A002 LDNFASHION (07: P1)**
- Its frame is "top streetwear brands in London", which conflicts with the rule that CROOKSLDN is never described as being from London.
- Its routes are affiliate and "Advertise with us".
- This pass excludes it. Outreach should at least drop it out of P1.

**A009 ICON polls (07: P2)**
- 07 already says "do not seed the vote".
- ChatGPT cited it once in the GEO panel.
- Poll seeding is off (16 Oct), so there's no action left. Treat it as excluded.

## Follow-up rows (18 Oct 2026)

The follow-up added 16 rows to §1.1. Totals are now **63 rows: 33 new and 30 overlapping with 07**.

| Status | Outlets |
|---|---|
| **New (12)** | Man of Many, Yanko Design, designboom, Totally The Bomb, Trend Hunter, Proper Magazine, Uncrate (reactive-outerwear outlets); The London Standard ES Best, Men's Health UK, Esquire UK, The Times, ITV News Meridian (national press) |
| **In 07, reactive angle added (4)** | FashionUnited UK (A031, news@ route), Culted (A029, no editorial route found), nss magazine (A043), Gear Patrol (A198, pitches@ route) |

## 07 gaps after the follow-up

| 07 gap | Status |
|---|---|
| Telegraph, Metro | Checked in Google UK. Wrong fit, so not added (see §1.3). |
| Esquire UK | Added (60) |
| Wired UK | Print ended in 2025; no apparel coverage. Not added. |
| Pages about water- or heat-reactive outerwear | Covered: 11 RX rows |
| Time Out, MyLondon, Secret London | **Not pursued.** London-local framing conflicts with the descriptor rule. |
| Reddit threads | Ranking check only. Seeding is off, and reddit.com can't be fetched from the cloud. |
| Supplier/manufacturer case studies, Omnisend customer stories, UK TikTok follower counts | Out of scope for this workstream |
