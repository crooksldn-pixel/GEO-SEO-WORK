<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# CROOKSLDN SEO/GEO — What George Actually Needs To Answer

Prepared 18 Oct 2026 from `main` and all 12 `cowork/*` branches of GEO-SEO-WORK (latest commits 17:17 UK), plus the Project's `seo/` files. The branches asked 96 questions between them. After removing everything already answered, already fixed, answerable from the repo, or duplicated, 33 remain.

## Summary

- P0 questions: 6
- P1 questions: 12
- P2 questions: 6
- P3 questions: 9
- **Total genuine decisions/questions: 33**
- **Total manual tasks: 10** (6 actions + 4 checks)
- **Total uploads/assets needed: 4**
- **Workstreams that can resume immediately after these answers: 10 of 11** (`cowork/international-markets-pricing` has no work on it yet)

**The fastest unblock:** answer #1–#4, #7 and #8, and untick the checkout box (Manual action M1). That clears every customer-facing promise problem and frees the theme, product-data, live-site and Merchant Center workstreams at once.

**How to answer:** reply in the project thread with the item number and your answer (e.g. "1: 2–4 days, 2: yes"). The table at the end shows which Cowork chat needs which numbers.

---

## P0 — Answer these first

### 1. How many working days does a print-on-demand T-shirt take to leave you after someone orders it? `[A · 2-minute answer]`

**Why I'm asking:** every live tee page says "IN STOCK", "Ordered now — leaves tomorrow" and "order before 18:00, ships today". 14 more T-shirt Week tees are drafted with the same problem. Google is also told tees ship the same day. The theme's fallback line says "9–16 days", which isn't your number either.
Note: Shopify shows some tee orders were fulfilled within a day, so if it's genuinely quick, say so.

**My recommendation:** give the honest range you can hit in a busy drop week, not your best case.

**Unlocks:** `cowork/theme-editor` (tee page wording), `cowork/live-site-checks` (shipping copy), `cowork/merchant-center` (Google handling time), `cowork/product-data`, product schema

**Answer with:** `___ to ___ working days` (and say if it's longer during drops)

### 2. Can we stop T-shirts showing "IN STOCK" and "1 LEFT", since they're printed to order? `[B · Yes/No]`

**Current situation:** tees are set up as if stock sits on a shelf. Some sizes show negative stock (e.g. Express White XS at −4) and one shows a false "1 LEFT". You still keep selling them at zero, which is correct.

**What would happen:** stock counting is switched off on all 17 tees (3 live, 14 T-shirt Week drafts). They stay buyable. Barcodes are not touched. The tee pages then show "Printed to order. Dispatched within [your #1 answer] working days."

**My recommendation:** Yes, before any T-shirt Week tee goes live.

**Unlocks:** `cowork/product-data`, `cowork/theme-editor`, `cowork/live-site-checks`

**Answer with:** `Yes / No`

### 3. Are these UK delivery times right? `[A · 2-minute answer]`

**Why I'm asking:** your policies, FAQ, Terms and Google data all say UK delivery takes 1–2 working days. Your own checkout says the free Tracked 48 (what every £30–£[redacted] order gets) takes 2–3 working days. One of them is wrong, and customers are promised the faster one.

**My recommendation:** Tracked 48 = 2–3 working days, Tracked 24 = 1–2 working days, as checkout says.

**Unlocks:** `cowork/live-site-checks` (wording in 14 places), `cowork/theme-editor`, `cowork/merchant-center`, product schema

**Answer with:** `Correct / Different: Tracked 48 = __ days, Tracked 24 = __ days`

### 4. Can we add a pre-order cancellation policy? `[B · Yes/No]`

**Current situation:** when someone pre-orders (e.g. the Pink Convict Sweats, "dispatch by 31 October"), checkout makes them tick "I agree to the cancellation policy". No such policy exists, and the link goes nowhere. That's a consumer-law and chargeback risk on every pre-order.

**What would happen:** a short policy goes into Shopify's policy settings: cancel any time before dispatch for a full refund, you'll be told if the date moves, normal returns apply after dispatch. Draft: `cowork/live-site-checks` → `artifacts/proposed-copy.md` section B.

**My recommendation:** Yes, as written.

**Unlocks:** `cowork/live-site-checks`

**Answer with:** `Yes / Yes with these edits: … / No`

### 5. Is the 5-star Trustpilot review from "kellan mullane" (8 Feb 2026) written by Preston? `[A · 2-minute answer]`

**Why I'm asking:** the name matches a director of Crooks Clothing Company Ltd. Trustpilot bans reviews from people who work for the business, and UK law now treats staff reviews as fake reviews. Only the reviewer can delete it.

**My recommendation:** if it's him, ask him to delete it this week.

**Unlocks:** `cowork/authority-research` (Trustpilot clean-up)

**Answer with:** `Yes, he'll delete it / Yes, leave it / No, someone else`

### 6. Can we change how you ask customers for Trustpilot reviews? `[B · Yes/No]`

**Current situation:** the review link sits in the "shipped today" email, which goes out before the parcel arrives, and orders with problems are kept out of it. Trustpilot treats that as screening out unhappy customers, which can put a public warning on your profile and hide your score. UK fake-review rules point the same way.

**What would happen:**
1. The Trustpilot link comes out of the shipped-today email.
2. Trustpilot's own free Shopify app is installed and invites every customer automatically a few days after delivery, with no hand-picking (free plan: 50 invites a month).

**My recommendation:** Yes to both. Your live score is 4.2 from 80 reviews, so a fair process isn't something to fear.

**Unlocks:** `cowork/authority-research`

**Answer with:** `Yes to both / Only 1 / Only 2 / Neither for now`

---

## P1 — Next

### 7. Can Claude make the approved theme fixes directly in the live theme's files? `[B · Yes/No]`

**Current situation:** the visual theme editor loads as a blank page for Claude (three attempts), so even pre-approved toggles (footer OUTERWEAR link, Judge.me cart widget off) haven't been done. Fixes such as the tee "IN STOCK" label and the delivery times also need small code edits, and no workstream is allowed to touch the live theme's code today.

**What would happen:** a backup copy of the live theme is made first. Claude then makes only the changes you've approved in this pack, one at a time, and checks each on the live site. The "Claude P1 fixes" copy **stays on hold** and is never published as a whole, because publishing it later would silently undo these live fixes. Its two changes (popup, brand schema) get moved across separately whenever you lift the hold.

**My recommendation:** Yes. If you'd rather not, see the fallback in Manual action M6.

**Unlocks:** `cowork/theme-editor`, `cowork/live-site-checks`, `cowork/search-console` (schema fixes)

**Answer with:** `Yes / No`

### 8. Can we delete the 10 duplicate products someone added by hand in Google Merchant Center? `[B · Yes/No]`

**Current situation:** 10 all-caps copies of Convict hoodies and sweats, Cellblock pieces and Yard denim sit beside your real Shopify listings. They have no brand, size, colour or category, show in the UK as unbranded duplicates, and are rejected in 33 other countries. The real Shopify listings already cover all 10.

**My recommendation:** Yes. Only those 10 are deleted; the Shopify feed isn't touched.

**Unlocks:** `cowork/merchant-center`

**Answer with:** `Yes / No (say what they're for)`

### 9. What seller name should Google Shopping show? `[A · 2-minute answer]`

**Why I'm asking:** Google rejects "CROOKSLDN" as a business name, so Shopping currently shows your seller name as "crooksldn.com".

**My recommendation:** "Crooks LDN" (matches the brand's alternate name everywhere else).

**Unlocks:** `cowork/merchant-center`

**Answer with:** `Crooks LDN / Crooks London / Keep as is`

### 10. Which products are women's, which are men's, and which are for both? `[A · 2-minute answer]`

**Why I'm asking:** you confirmed Shopping should cover men's and women's items per product, but nothing in Shopify says which is which. Google uses this to decide who sees each product.

**My recommendation:** reply with **only the exceptions** to this starting point. Sets follow their two pieces.

| Product | Suggested |
|---|---|
| Convict Hoodie (Black, Grey, Pink) | both |
| Convict Sweats (Black, Grey, Pink) | both |
| Black / Grey / Pink Set | both |
| Cellblock Crewneck, Shorts, Set | both |
| Blue / Grey Wash Yard Jeans, OG Jeans | **you tell us** |
| Blue / Grey Wash Yard Jorts | **you tell us** |
| HydroCuff Windbreaker, Double-Agent Puffa | both |
| All tees (incl. the 14 T-shirt Week drafts) | both |
| MotionTec socks, Cream Cap | both |

**Unlocks:** `cowork/product-data`, `cowork/merchant-center`, `cowork/outreach` (Disco's "who is it for?")

**Answer with:** `All as suggested, plus: jeans = __, jorts = __` (or list any others that differ)

### 11. Two Double-Agent Puffa facts `[A · 2-minute answer]`

**Why I'm asking:** Google needs one base colour for it (it's the only product without one, and its own photo text says "black shell"). The reactive copy also needs to know whether it changes back.

**My recommendation:** none; these are facts only you have.

**Unlocks:** `cowork/product-data`, `cowork/merchant-center`, `cowork/collections` (reactive guide)

**Answer with:**
- `Base colour (unheated): ___`
- `Does it go back to normal as it cools? Yes / No`

### 12. Approve this batch of product-page fixes? `[B · Yes/No]`

**Current situation:** product pages and Google listings still carry claims you haven't confirmed, and two Shopping titles are in all caps.

**What would happen:**
- "Cotton", "premium cotton" and "cotton blend" come off the 3 live tees and both MotionTec socks (text, Google titles, photo descriptions, fabric fields), plus the unused `cotton` tag on the tees.
- Cellblock Shorts' fabric becomes "fleece" only.
- OG Jeans gets "14oz" like the other jeans.
- Google titles: "Charcoal Cellblock Crewneck — 450gsm Fleece | CROOKSLDN" and "Double-Agent Puffa — Heat-Reactive Puffer Jacket | CROOKSLDN".
- Every product is marked "adult" for Google.
- Exact before/after: `cowork/product-data` → `artifacts/c-fabric-claim-fixes.md`.

**Exception:** if the tee blanks or socks really are cotton, give the composition and we keep it.

**My recommendation:** Yes.

**Unlocks:** `cowork/product-data`, `cowork/merchant-center`

**Answer with:** `Yes / Yes, but tees are __% cotton / No`

### 13. Approve this batch of collection and page copy fixes? `[B · Yes/No]`

**Current situation:** the live Sweats and Denim pages still say "made in Portugal", and the Contact page says the brand is "run out of London". Both break rules you've already set, and AI answers are repeating the London line. Three small internal links are also ready.

**What would happen:**
- Sweats gets the copy you approved on 16 Oct, with your confirmed weights and no Portugal line.
- Denim: "made in Portugal" removed, plus one line linking to the Convict Hoodie and tees.
- Contact page: "run out of London" becomes "an independent British streetwear brand".
- Tracksuits gets a line linking to the fit guide.
- The fit guide's 550gsm section is rewritten to answer "Is 550gsm heavy?" (550gsm Convict vs 450gsm Cellblock).
- Exact text: `cowork/collections` → `artifacts/proposed-changes.md`.

**My recommendation:** Yes.

**Unlocks:** `cowork/collections`, `cowork/authority-research`, `cowork/geo-measurement` (next run)

**Answer with:** `Yes / Yes except: … / No`

### 14. Can we use this one-line brand description everywhere? `[B · Yes/No]`

> CROOKSLDN is an independent British streetwear brand making heavyweight fleece, baggy denim, graphic tees and reactive outerwear, cut in oversized, street-led silhouettes and released in drops.

**Current situation:** it's drafted but not signed off (it was part of the About page draft, which stays unapproved). Your Shopify store description is empty, and Google and AI tools read it.

**What would happen:** it goes into the Shopify store description now, and is reused word for word on Trustpilot, directory listings and new profiles. This does **not** approve or publish the About page.

**My recommendation:** Yes.

**Unlocks:** `cowork/product-data`, `cowork/outreach`, `cowork/authority-research`

**Answer with:** `Yes / Yes with this wording: … / No`

### 15. Approve the reactive-jacket copy? `[B · Yes/No]`

**Current situation:** the GEO baseline shows reactive outerwear is an open lane: AI answers for "water reactive jacket" and "heat reactive puffer" name nobody consistently, and nothing ties Crooks to it yet.

**What would happen:** new HydroCuff and Puffa product descriptions, a matching intro on the Outerwear collection, and a short guide at `/blogs/news/reactive-outerwear`. They use only your confirmed facts (reacts to rain, back to normal when dry, wash cold, don't iron; Puffa heat-reactive, avoid washing). Two wording calls:
- HydroCuff: "made to react wear after wear" (your "durable", with no lifetime figure).
- Puffa care: "spot clean if needed" (not yet confirmed by you).

Draft: Project file `seo/workstreams/05-reactive-drafts.md`.

**My recommendation:** Yes to both lines. The Puffa "changes back" line follows your #11 answer.

**Unlocks:** `cowork/product-data`, `cowork/collections`, `cowork/geo-measurement`

**Answer with:** `Yes / Yes, drop "wear after wear" / Yes, drop "spot clean" / No`

### 16. Public GitHub repo: OK to copy the project files in with private details removed? `[B · Yes/No]`

**Current situation:** seven workstreams are stuck because they can't see the Project's `seo/` folder (change log, master queue, query map, reactive drafts, authority list, directory pack). Claude can copy them into the repo for you, but the repo is public. Some files hold Shopify sales figures, your age, the £[redacted]+ figure and the [town redacted] address. Three details already in the repo are also sensitive: a named director linked to a review, monthly order counts, and the IP address of the network the GEO tests run from.

**What would happen:** the files are copied to a new branch with £ sales, order counts, age, revenue and town removed. The three existing details are reworded ("a reviewer whose name matches a company officer", "a few hundred orders a month", "GB" only). Past history isn't rewritten.

**My recommendation:** Yes.

**Unlocks:** `cowork/programme-records`, `cowork/product-data`, `cowork/collections`, `cowork/merchant-center`, `cowork/outreach`, `cowork/authority-research`, `cowork/geo-measurement`

**Answer with:** `Yes / Yes, but leave existing details as they are / No`

### 17. Which email inbox do you actually read and reply from? `[A · 2-minute answer]`

**Why I'm asking:** past Trustpilot replies sent customers to three different addresses, and recent brand emails went out from the Gmail address while the site lists team@. Customer replies and press pitches need to go to an inbox someone checks.

**My recommendation:** team@crooksldn.com for everything, if it's checked daily.

**Unlocks:** `cowork/authority-research` (Trustpilot replies), `cowork/outreach` (pitch drafts)

**Answer with:** `team@crooksldn.com / support@crooksldn.com / the Gmail address`

### 18. Post 12 Trustpilot replies, and report two reviews from models? `[F · External action]`

**What would happen:** you post 12 replies to unanswered 1–3★ reviews (drafts in `cowork/authority-research` → `artifacts/09-authority-research.md` §2.4). They apologise, ask for the order number by email and promise nothing beyond your policies. Separately, you report two 5★ reviews (Tee Wizza and georgia, 16 Sep) from people who say they modelled for you.
**Cost:** your time, about 30 minutes. Free.
**Upside:** 8 of the unanswered reviews say "scam", and AI answers about "Crooks LDN reviews" quote Trustpilot directly. Visible replies change what shoppers and AI see.
**Downside:** you lose two 5★ reviews; replies are public and permanent.

**My recommendation:** Yes to both, using the inbox from #17.

**Unlocks:** `cowork/authority-research`, `cowork/geo-measurement`

**Answer with:** `Post all 12 / Post all except: … / Report both: Yes / No`

---

## P2 — Useful but not urgent

### 19. Which magazines and podcasts can we pitch? `[F · External action]`

**What would happen:** Claude prepares text-only Gmail drafts (and fills free forms) for you to send. No samples and no paid features.
**Cost:** free.
**Upside:** independent mentions that help AI tools describe Crooks correctly and separate it from Crooks & Castles.
**Downside:** uncertain response without samples; a no from an outlet is mostly permanent for a while.

**My recommendation:** PAUSE (email), GUAP (free form), Menswear Style Podcast (email). Skip The Sole Supplier, OPUMO and WMTV LDN (paid-only or inactive).

**Unlocks:** `cowork/outreach`

**Answer with:** `Recommended 3 / Recommended + FashionBeans and Ape to Gentleman / My own list: …`

### 20. Create LinkedIn and Crunchbase company pages, and rename Trustpilot to "CROOKSLDN"? `[F · External action]`

**What would happen:** profiles for Crooks Clothing Company Ltd (16606021) from the prepared copy, with the line "CROOKSLDN is the trading name of Crooks Clothing Company Ltd (company no. 16606021)". You as founder; Preston not listed unless you say so. Trustpilot's display name changes from "Crooks ldn" to "CROOKSLDN" with the #14 description.
**Cost:** free, about 30 minutes for you, since profiles need your login.
**Upside:** AI tools currently link the brand to a different company of yours (Crooks London Limited, 16396366). Consistent profiles fix that.
**Downside:** public company pages to keep current.

**My recommendation:** Yes, founder George only.

**Unlocks:** `cowork/authority-research`

**Answer with:** `Yes / Yes, add Preston as director / Not now`

### 21. Tidy up dead and duplicate pages Google still finds? `[B · Yes/No]`

**Current situation:** seven old product pages return "not found", two of which still got search traffic. An old generic collection page, `/collections/frontpage`, appears under your brand in Google results, titled "PRODUCTS".

**What would happen:**
- 4 old tees (OG Crook, 3 Clives, Broadcast, Evil Clive) send visitors to /collections/tees; the Large Duffle Bag to /collections/accessories.
- The two old "Tesco tee" pages (238 searches in six months, and rising) send visitors to the Crooks Express tee if it's the same design, or to /collections/tees if not.
- `/collections/frontpage` is hidden from search results (not deleted).

**My recommendation:** Yes.

**Unlocks:** `cowork/collections`, `cowork/search-console`

**Answer with:** `Yes, and the Express tee IS / IS NOT the Tesco tee`

### 22. Switch off the Judge.me script that shows shoppers nothing? `[B · Yes/No]`

**Current situation:** you've decided not to show reviews. Judge.me's main script still loads on every page (about 34 KB) but displays nothing: no stars, tab or badge. Review request emails don't depend on it. (The Judge.me cart widget is already approved to go off.)

**My recommendation:** Yes. It can be switched back on in one click.

**Unlocks:** `cowork/theme-editor`

**Answer with:** `Yes / No`

### 23. Shipping weights `[A · 2-minute answer]`

**Why I'm asking:** 11 products weigh 0g in Shopify, including all four sets, so international orders are under-charged for postage.

**My recommendation:** we use these unless you correct them: Black and Grey Set 1,700g, Pink Set 1,700g, Cellblock Set 1,450g, CRX Garms and CRXST★RZ tees 250g (same as the Express tee).

**Answer with:**
- `Pink Convict Sweats: 700g or 800g?` (it was set to 700g on 17 Oct; Black and Grey are 800g)
- `Yard Jorts: __g · Puffa: __g · Cap: __g`
- `Socks per pack: 1 pair __g · 3 __g · 6 __g · 12 __g` (Black/Blue packs all say 20g today)

**Unlocks:** `cowork/product-data`

### 24. Any drops, launches or password-locked days before 14 November? `[A · 2-minute answer]`

**Why I'm asking:** drops spike brand searches, and a locked store sends them to the password page. Search Console and the GEO panel need those dates marked so a drop isn't mistaken for an SEO win or loss. T-shirt Week also needs fixes #1 and #2 in place first.

**My recommendation:** include T-shirt Week's date if it's planned.

**Unlocks:** `cowork/search-console`, `cowork/geo-measurement`, `cowork/product-data`

**Answer with:** `None planned / Dates: …`

---

## P3 — Low-priority questions (don't block anything important)

### 25. Remove the old ReStock "pre-order" option from tees (and Pink Sweats)? `[B]`
Leftover setup that may add a "deferred purchase" notice at checkout. None of the last [n] orders used it. ReStock stays installed; the Pink Sweats' own pre-order (dispatch by 31 Oct) stays.
**Recommendation:** Yes, on the 3 live tees and the Pink Sweats. **Answer:** `Yes / Tees only / No` · **Unlocks:** `cowork/product-data`

### 26. Do you still want customers to edit or cancel their own orders through Orderify? `[B]`
Orderify stays installed either way: 5 customers used it (latest 26 Sep). If you don't want self-service, it can be removed later.
**Recommendation:** Keep. **Answer:** `Keep / Remove later` · **Unlocks:** `cowork/theme-editor`, `cowork/programme-records`

### 27. Were the old "CB1" jeans and jorts grey wash, and "CB2" blue? `[A]`
The old redirects disagree between jeans and jorts. Search data hints CB2 was grey.
**Recommendation:** CB1 = blue, CB2 = grey (fix the two jeans redirects). **Answer:** `CB1 = __, CB2 = __` · **Unlocks:** `cowork/collections`

### 28. Also show the Cellblock Set in the Sweats collection? `[B]`
Today it's only findable through Sets and "All".
**Recommendation:** Yes. **Answer:** `Yes / No` · **Unlocks:** `cowork/collections`

### 29. Sell on Dripscan (12% commission, free tier)? `[B]`
Its magazine is cited by Gemini for "Corteiz alternatives", but listing is a new sales channel.
**Recommendation:** Not now; revisit after their launch. **Answer:** `No / Not now / Yes` · **Unlocks:** `cowork/authority-research`

### 30. Keep one Convict colourway permanently in stock? `[A]`
Evergreen "best hoodie" roundups drop products whose links sell out.
**Recommendation:** only if it suits the drop model. **Answer:** `Yes: ___ colourway / No, drops only` · **Unlocks:** `cowork/authority-research`, `cowork/outreach`

### 31. Do you sell to Liechtenstein, Bulgaria, Croatia, Malta or South Korea? `[A]`
They show Google shipping errors that come from Shopify's market settings.
**Recommendation:** if not, leave them alone. **Answer:** `No / Yes: …` · **Unlocks:** `cowork/merchant-center`

### 32. Two historic facts `[A]`
What does "V1/V2" on the Pink Convict Hoodie mean, and roughly when did Crooks start trading?
**Answer:** `V1/V2 = … · Trading since: …` · **Unlocks:** `cowork/product-data`, `cowork/authority-research`

### 33. Does anything scan the barcodes on the item bags, now or planned? `[A]`
Barcodes stay untouched either way, and Google shows no barcode problem today. This only matters if a warehouse or courier will scan them.
**Recommendation:** if anything scans them, add photos of 3–4 bag labels (OG Jeans first) to the product-data chat (not the public repo) for a check. **Answer:** `No / Yes now / Planned` · **Unlocks:** `cowork/product-data`

---

## Uploads / assets

| # | What to upload | Where to get it | Why it matters | Priority |
|---|---|---|---|---|
| U1 | **Cream Cap photos** (front, plus side or back) | Your own shoot or supplier images | The cap is live with no photos and is the only product Google rejects in the UK. Without photos, Google's automatic additions on 2 Nov can re-add it and reject it again. | P1 |
| U2 | **Square logo + one portrait (4:5) campaign image with no text on it** (PNG/JPG, under 5 MB) | Brand files / campaign shoot | Disco's directory listing uses both. Streetwear Directory needs none, so it goes first. | P1 |
| U3 | **HydroCuff dry and wet pair** (same framing), **Puffa normal and heat-reacted**, plus any short reaction video | New shoot or existing content | Lets shoppers and AI see the reactive effect. The video unlocks design-press pitches. | P2 |
| U4 | **On-body shots** of Convict hoodie and sweats, OG Jeans, Puffa, HydroCuff | Existing campaign or creator content you own | Fit doubt is a common reason not to buy; also used for Google image results. | P2 |

Product photos can go in the project thread or the product-data chat. They'll be public on the site anyway.

**Not needed (already collected):** Search Console exports (on `cowork/search-console`), Merchant Center product and issue exports (on `cowork/merchant-center`; the 29 Oct re-export is done by Claude), GEO panel runs (on `cowork/geo-measurement`). The Project-file uploads all branches asked for are replaced by #16.

---

## Things George needs to physically/admin check

### C1. Is anyone else editing the website right now? (P1)
**How:** ask anyone else who works on the store whether they're editing the live theme ("CROOKSLDN — SEO round 2") or products this week. Also: on 17 Oct someone set the Cellblock Crewneck to 800g and the Pink Convict Sweats to 700g, and three collections were touched on 18 Oct at 12:25. Was that you, someone you know, or an app?
**Why:** two people saving the same theme or product silently overwrite each other. No theme save happens until this is answered.
**Answer:** `Nobody else editing / Someone is: … · The 17 Oct weight change was: me / ___ / don't know`

### C2. Measure the jeans (P1)
**How:** lay one pair of each jean flat in XS, S, M, L and XL. Measure in cm: waist (across, doubled), inseam, and leg opening. Rise and thigh are optional. Say whether Yard and OG Jeans fit the same.
**Why:** all three jeans pages show the Convict Sweats size chart by mistake, and customers size from it.
**Answer:** a table pasted in the thread.

### C3. Do you run any Shopify Forms pop-ups? (P3)
**How:** Shopify admin → Apps → Forms. Check for pop-up forms, or forms anywhere other than the homepage signup and password page.
**Why:** if not, the Forms script (262 KB on every page) can be tested switched off on a copy theme to speed up mobile pages. The homepage signup stays.
**Answer:** `Homepage and password page only / Also: …`

### C4. Is crooksldn.com set up in Search Console on any other Google account? (P3)
**How:** in any other Google account used for the business, open search.google.com/search-console and look for crooksldn.com in the property list.
**Why:** the current account has no data for 23 Jul – 14 Oct. Another property could fill the gap and give a proper before-and-after.
**Answer:** `None / Yes, on ___ (add team@crooksldn.com as a user)`

---

## Manual actions

### M1. Untick the pre-ticked marketing box at checkout (P0, 2 minutes)
1. Shopify admin → **Settings** → **Checkout**.
2. Scroll to **Marketing options**.
3. Untick **"Preselect the sign-up option"** for email. Leave the sign-up option itself on.
4. Save.

**Why:** checkout pre-ticks "Keep me updated". Pre-ticked boxes aren't valid consent under UK GDPR/PECR, and those sign-ups feed Omnisend. Still ticked when re-checked on 18 Oct.

### M2. Take the Cream Cap off Google (P1, 1 minute)
You approved this on 16 Oct, but Claude's Shopify connection isn't allowed to unpublish.
1. Shopify admin → **Products** → **MAJOR LEAGUE CROOKS CAP (CREAM)**.
2. In **Publishing** (right-hand side), click **Manage**.
3. Untick **Google & YouTube** only. Leave every other channel ticked.
4. Save.

### M3. Give the go for the two directory listings (P1, 5 minutes)
You approved free, human-reviewed directories on 16 Oct, and both are free. The outreach session fills in Streetwear Directory first (ChatGPT's only cited source for "brands like Corteiz"), then Disco once U2 arrives, and shows you each filled form. Type **go** in that chat for each one.

### M4. Make `main` the repo's default branch (P2, 1 minute)
1. github.com/crooksldn-pixel/GEO-SEO-WORK → **Settings** → **General**.
2. Under **Default branch**, click the switch icon, choose **main** → **Update** → confirm.

**Why:** new sessions currently start on the GEO workstream's branch by mistake. Claude can't change repo settings.

### M5. Perplexity for the GEO tests (P3, 5 minutes, or say "drop it")
1. Create a Perplexity account **with email, not "Continue with Google"**.
2. Sign in to it in the Claude desktop app's built-in browser, in the Perplexity tab.
3. Turn off memory and personalisation in its settings.

**Why:** logged out, Perplexity blocked 58 of 63 test runs. **Recommendation:** do it when convenient; otherwise reply "drop Perplexity" and the panel continues on Google, ChatGPT and Gemini.

### M6. Only if you answer No to #7: open the theme editor once (P1)
In Chrome, go to Shopify admin → **Online Store** → **Themes** → **Customize** on the live theme. Clear any pop-up or prompt waiting there, then tell the theme-editor session it loads.

---

## Contradictions found

**1. Trustpilot score**
- Branch A (16 Oct brief, project memory) says 3.3 "Average" from 50 reviews.
- Branch B (`cowork/authority-research`, checked in a real browser 16 and 18 Oct) says 4.2 "Great" from 80.
- **Best interpretation:** 3.3/50 came from a cached copy dated 30 Jul. The live score is 4.2/80.
- **Do you actually need George?** No.

**2. How tee pages learn a tee is printed to order**
- `cowork/product-data` and `cowork/live-site-checks` say add a new `made-to-order` tag to all 17 tees.
- `cowork/theme-editor` says point the theme at the existing `tee` tag, which only tees carry.
- **Best interpretation:** use the existing `tee` tag (no product edits, works on save). product-data still switches stock counting off (#2).
- **Do you actually need George?** No.

**3. Will removing ReStock change what tee buyers see at checkout?**
- `cowork/product-data` expects the ReStock plan to trigger the "deferred purchase" notice on tee orders.
- `cowork/live-site-checks` thinks it doesn't (untested).
- **Best interpretation:** it's clean-up either way (#25). The test cart is dropped.
- **Do you actually need George?** No.

**4. Which company is the brand's public operator**
- AI tools cite Crooks London Limited (16396366, you're sole director).
- The profiles use Crooks Clothing Company Ltd (16606021).
- **Best interpretation:** you decided on 16 Oct that Crooks Clothing Company Ltd is the trading company. Profiles (#20) and site schema will name it consistently.
- **Do you actually need George?** No.

**5. Orderify**
- The 16 Oct decision said "prepare removal".
- A later finding shows customers use it to edit and cancel orders.
- **Best interpretation:** it stays installed. Only whether you want self-service is open (#26).
- **Do you actually need George?** Only #26.

**6. Google's automatic product additions (deadline 1 Nov)**
- `cowork/merchant-center` asks for your stance again.
- Your 16 Oct rule was: stay in if the 29 Oct check is clean in the UK, otherwise opt out by 1 Nov.
- **Best interpretation:** your rule stands. The cap risk is handled by M2 plus U1.
- **Do you actually need George?** No. You get a one-line stay-in or opt-out call on 29 Oct.

**7. "112 invalid barcodes"**
- The Merchant Center brief says 112 invalid GTINs.
- Merchant Center itself shows only 8 sent and no barcode issue.
- **Best interpretation:** 112 was a count of Shopify barcodes (Project file `02-product-schema.md`), not Google errors. No feed fix is needed.
- **Do you actually need George?** No.

**8. Mida**
- `cowork/live-site-checks` recommends switching it off to fix slow mobile taps.
- You said Mida is in use.
- **Best interpretation:** keep it.
- **Do you actually need George?** No.

**9. Sweats and Denim pages "can't be edited"**
- The master queue says these two pages are invisible to Claude.
- `cowork/collections` found both and edits them in the Shopify admin screen.
- **Best interpretation:** the old question about how they're managed is closed.
- **Do you actually need George?** No.

**10. Tees printed to order but fulfilled within a day**
- The owner fact says all tees are print-on-demand.
- Shopify shows [n] tee orders fulfilled within about a day.
- **Best interpretation:** printing is fast, not stocked. #1 captures the real time.
- **Do you actually need George?** Only #1.

---

## Already answered or handled without George (removed from the list)

Everything in your confirmed-facts list, plus: Search Console and Merchant Center exports (done); the GEO baseline and Mac session (done); Made in Portugal and China origin (live 16 Oct); batch 2 and Tracksuits sets (live); the cap off Google (approved, now M2); the Judge.me cart widget and footer OUTERWEAR (approved, waiting on #7); directory approval (approved, now M3); the Sweats copy (approved 16 Oct); IndyBest samples (declined with the other samples); publishing "Claude P1 fixes" (on hold, not asked); Mida (keep). The records workstream's six decisions, the Disco style and price picks, Search Console scheduling, the GEO re-run date and extra query, the owner of page copy and shipping settings, all use Claude's recommended default. The `cowork-results/` folder the records workstream asked for doesn't exist, so there's nothing to upload.

---

## What happens after George answers

| Workstream | Restarts on | What it does first |
|---|---|---|
| `cowork/product-data` | #2, #10–#12, #14, #23 (#25 and photos later) | Tee stock off, fabric fixes and titles, gender and age, Puffa colour, weights, store description |
| `cowork/theme-editor` | #1, #7, #22 and C1 | Tee dispatch line, footer OUTERWEAR, Judge.me off, sitewide status bar wording |
| `cowork/live-site-checks` | #1, #3, #4, #7 and M1 | Final shipping wording in all 14 places, pre-order cancellation policy, checks the checkout box |
| `cowork/merchant-center` | #1, #8, #9 | Deletes the duplicates, fixes the seller name, sets tee handling time; 29 Oct opt-in check |
| `cowork/collections` | #13, #15, #16, #21 | Sweats and Denim copy, contact page fix, fit guide, redirects, reactive guide |
| `cowork/outreach` | #16, #17, #19, M3 and U2 | Streetwear Directory, then Disco, then pitch drafts |
| `cowork/authority-research` | #5, #6, #17, #18, #20 | Final Trustpilot replies and profile copy, then a research follow-up |
| `cowork/programme-records` | #16 and M4 | Change log metrics and review dates, queue tidy-up, status update |
| `cowork/search-console` | #24 (#21 for redirect targets) | Indexing check 20 Oct, 7-day read 24 Oct, 28-day read 14 Nov |
| `cowork/geo-measurement` | #16 (M5 optional) | Control re-run 13 Nov; full re-measure about 4 weeks after the first live changes |

Each Cowork session still needs you to type **answered** (and **go** before live store or theme saves) in its own chat. That's their permission rule, not a new question. Paste the numbered answers each one needs (left column) into its chat.
