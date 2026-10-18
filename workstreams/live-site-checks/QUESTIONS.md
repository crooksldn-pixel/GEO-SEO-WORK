# Questions for George — live-site checks

> **ANSWERED 18 Oct 2026, 17:03 UTC.** George's answers are recorded in [ANSWERS.md](ANSWERS.md), which is the source of truth. The answer slots below were left as they were. What this workstream does with them is in `STATUS.md` and `NEXT.md`.

**How to answer:** write under each **Answer:** line and commit to `cowork/live-site-checks`, or answer in the main chat. Then tell this session **"answered"**.

These are facts and decisions only. This workstream is research only and doesn't change the store. Product data belongs to `cowork/product-data`, and theme and settings changes to whoever is implementing them.

If a question needs this session to do something on the live site (Q9), it will still confirm with George in this chat first.

Recommendations come first in each option list.

---

## Q1 — How long do print-on-demand tees take to leave you?

**Why:** every live tee page says "IN STOCK" and "Ordered now — leaves tomorrow", and 14 more tees are about to launch the same way. The fix swaps that for a made-to-order line, which needs your real number. The theme's "9–16 days" is a default, not yours.
**Unblocks:** proposed copy A3, A5, A6, A7, A8 (`{TEE LEAD TIME}`), and tee schema `handlingTime`.
**Answer in this form:** "X–Y working days from order to dispatch". Say if it's different during a drop or for some colours.

**Answer:**

---

## Q2 — Are these UK delivery times right?

**Why:** every policy, the FAQ, Terms and the product schema say UK delivery is 1–2 working days. Your own checkout says the free Tracked 48 takes **2–3 business days**, and Tracked 48 is what every £30–£79.99 order gets by default. One of them is wrong.

- **(a) Recommended:** Tracked 48 = 2–3 working days, Tracked 24 = 1–2 working days, as checkout says. The copy in `artifacts/proposed-copy.md` uses these.
- **(b)** Different real figures. Give them, and checkout's labels need changing too.

**Answer:**

---

## Q3 — Turn off the pre-ticked marketing box at checkout (your action, about 2 minutes)

**Why:** checkout pre-ticks "Keep me updated." Pre-ticked boxes aren't valid consent under UK GDPR/PECR, and those sign-ups feed Omnisend. Re-checked live 18 Oct: still ticked.
**How:** Shopify admin → Settings → Checkout → Marketing options → untick **"Preselect the sign-up option"** (the email one). Leave the sign-up option itself on.

- **(a) Recommended:** done.
- **(b)** Not doing it. Say why.

**Answer:**

---

## Q4 — Mida session recording: keep it on?

**Why:** Mida's recorder (`recorder.msr.js`) is the heaviest script on every page: 350–590 ms of main-thread time per page on mobile. The homepage is failing Core Web Vitals on mobile because of INP (228 ms, should be ≤ 200), and Mida is the prime suspect. Mida has **no sampling or page-exclusion setting**; its docs list only IP and country exclusion. So it's on or off.

- **(a) Recommended:** switch the Mida app embed off. Online Store → Themes → Customize → App embeds → MIDA recorder → off. Switch it back on for short windows when you actually want recordings. Re-check homepage INP 28 days after.
- **(b)** Keep it on. You're using the recordings and accept the INP cost.
- **(c)** Uninstall Mida.

Note: an app embed toggle is stored in the theme (`config/settings_data.json`). If "Claude P1 fixes" is published afterwards, Mida comes back on, because that theme still has it enabled. See Q8.

**Answer:**

---

## Q5 — Do you use any Shopify Forms besides the homepage signup?

**What I found:** the homepage early-access signup (the "informant intake" section) and the password page both use **Shopify Forms** (form 923202). Forms is needed and stays. But its app embed also loads a **262 KiB script on every page**, 244 KiB of it unused on the homepage, including product and collection pages where there's no form.
**Question:** in Shopify admin → Apps → Forms, do you run any **popup** forms, or forms on pages other than the homepage and password page?

- **Recommended answer if you don't:** "No popups." Then a theme workstream can test, on a copy theme, whether the homepage form still works with the Forms *app embed* switched off. The block on the homepage stays either way.
- If you do run popups, say where. The embed stays.

**Answer:**

---

## Q6 — Approve the pre-order cancellation policy

**Why:** with a pre-order in the bag, cart and checkout make the shopper tick "I agree to the cancellation policy…", but no cancellation policy exists. The link goes nowhere, and `/policies/subscription-policy` returns 404.
**Text:** `artifacts/proposed-copy.md`, section B. It covers cancelling any time before dispatch for a full refund, being told if the date moves, and the normal refund policy after dispatch.

- **(a) Recommended:** approved as written. It goes in Settings → Policies → Cancellation policy.
- **(b)** Approved with edits. Write them.
- **(c)** Different terms. Say what they are.

**Answer:**

---

## Q7 — Approve the shipping and delivery wording

**Why:** the shipping promise appears in 14 places and they disagree on delivery time, threshold wording and the set line.
**Text:** `artifacts/proposed-copy.md`, section A (A1–A11). Each place is listed with its exact location and the before and after wording.

- **(a) Recommended:** approved as written, with the Q1 and Q2 answers dropped in.
- **(b)** Approved with edits. Write them.

**Answer:**

---

## Q8 — Lift the hold on the "Claude P1 fixes" theme?

**What I found (18 Oct, checksum of all 499 files):** "CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)" is identical to the live theme except two files:
1. **The popup** (`snippets/crack-the-cuffs.liquid`): never sooner than 10 s, a bottom sheet of at most 40% of the screen on phones, × quiets it for the session, plus measurement events. Your owner decision of 16 Oct, built by 09-performance.
2. **Organization schema** (`snippets/crooks-schema-site.liquid`): founder, Companies House 16606021, sameAs limited to Instagram and TikTok, the "independent British streetwear brand" description, and "Crooks LDN" as an alternate name.

Live hasn't been edited since 16 Oct 13:33 UTC, so today publishing the held theme changes exactly those two things.

**Why it matters:** any theme edit made on live from now on (status bar, FAQ, PDP lines, schema, app-embed toggles) is **silently undone** if the held theme is published later.

- **(a) Recommended:** lift the hold and publish it now, before any other theme edits. Rollback is one click (republish "SEO round 2"). All later theme work then happens on one theme.
- **(b)** Keep holding. Say what it's waiting on. Every theme fix then has to be made in both themes.

**Answer:**

---

## Q9 — OK to run one tee-only test cart?

**Why:** the checkout's "deferred / recurring purchase" notice appeared with the Pink Sweats pre-order in the bag. It probably doesn't appear for tees: their old ReStock plan is optional and the product page never sends it. `cowork/product-data` assumes it does. One test settles it.
**What it involves:**
- add one tee to the test cart in your Claude built-in browser
- open checkout and read the notice
- remove the tee

No payment, no personal details, and the existing cart is left as it was. This session will confirm with you in this chat before running it.

- **(a) Recommended:** yes.
- **(b)** No. It stays recorded as "most likely, untested".

**Answer:**
