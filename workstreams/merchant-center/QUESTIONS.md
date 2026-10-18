# Questions for George — Merchant Center

Everything this workstream needs from George is in this one file. Nothing is needed from George that isn't listed here.

**How to answer:** write each answer on the **Answer:** line under its question and commit it to `cowork/merchant-center`. This workstream gives the orchestrator permission to edit this file only. Then tell this Cowork session "answered". It will read this file and carry on. A question left blank is treated as unanswered, and the work that depends on it stays on hold.

Asked 18 Oct 2026. Evidence is in [FINDINGS.md](FINDINGS.md); exact before/after values are in [artifacts/04-merchant-center.md](artifacts/04-merchant-center.md).

---

## Q1 — Delete the 10 hand-added `CROOKSRELEASESEPT` products? (needed now)

Merchant Center holds 10 products someone added by hand, all in caps:
- Black, Grey and Pink Convict Hoodie
- Black, Grey and Pink Convict Sweats
- Charcoal Cellblock Crewneck and Shorts
- Blue Wash Yard Jeans and Jorts

IDs are `G-65230983` to `G-65230992`. They have no brand, size, colour or category. They show in the UK beside the proper Shopify listings for the same pages, and they're disapproved in 33 other countries. Shopify already sends all 10 products. (FINDINGS 1)

- **Yes:** this session deletes those 10 products only. The Shopify sources aren't touched.
- **No:** say what they're for, and they stay.

**Answer:**

## Q2 — Business name in Merchant Center (needed now)

Google rejects "CROOKSLDN", so Shopping shows the seller as "crooksldn.com". (FINDINGS 4)

- **A:** change it to "Crooks LDN" (recommended)
- **B:** change it to "Crooks London"
- **C:** keep "CROOKSLDN" and accept "crooksldn.com" as the seller name

**Answer:**

## Q3 — Tee print-on-demand time (needed for task D)

How many working days from a tee order to dispatch? Give a minimum and a maximum, for example "3–5". Every tee currently tells Google it ships the same day. (FINDINGS 3)

This number becomes the tee handling time. Tees will also get the label `print-on-demand`, unless George wants a different label.

**Answer:**

## Q4 — Auto-add stance (can answer now; deadline 1 Nov)

On 2 Nov Google will add the 30 extra products it found on crooksldn.com, unless the account opts out by 1 Nov. Google adds only products that aren't in any feed. So anything taken off the Google channel can come back, unchecked, through the crawl. The Cream Cap is the first case. (FINDINGS 7)

- **A:** stay opted in if the 29 Oct export is clean in the UK, and accept that risk. This was George's original rule.
- **B:** opt out whatever the 29 Oct export shows, to keep full control of what's listed.

**Answer:**

## Q5 — Files from the `seo` project folder (needed to finish task A)

Commit `workstreams/03-merchant-feed.md` (the 11 findings) and `workstreams/03-merchant-feed-handoff.md` (the "Workstream 3 corrections", sections A–E) to this repo on any branch, and give the path here. Or connect the `seo` folder to this Cowork session.

**Answer:**

## Q6 — Where did "112 invalid codes" come from? (optional)

The brief says all 112 invalid GTINs are 8 digits. Today Merchant Center has 8 variants sending a GTIN, and no GTIN issue. If the 112 came from a Shopify count or an older Merchant Center report, say which. (FINDINGS 2)

**Answer:**

## Q7 — Small markets (optional; default is to leave them)

Liechtenstein, Bulgaria, Croatia, Malta and South Korea show "missing shipping" or "missing Korean registration" issues. These come from Shopify Markets, not Merchant Center. Does CROOKSLDN sell to any of them? If not, nothing is done. (FINDINGS 5)

**Answer:**

---

## Not for George: orchestrator decision

**O1. Who owns Shopify Settings > Shipping?** The 2–4 day delivery shown on the two free UK tiers, the 12:00 AM cut-off and the 0-day handling on every item all come from Shopify. Shopify is likely to overwrite any edit made to them in Merchant Center. No workstream owns these settings yet.

**Answer:**

## Also waiting on George, in another workstream

- `cowork/product-data` item A: say yes there to taking the Cream Cap off Google & YouTube. It's the only product disapproved in the UK.
