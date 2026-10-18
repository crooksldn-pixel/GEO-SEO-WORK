# Questions for George

Answers given in the workstream chat on 18 Oct 2026 are recorded under each question. Open questions are Q3b and Q12–Q16.

## Q1. Tiers and mechanism

**Answer: A — APPROVE.** Tier 1 fixed USD (US) and EUR (Eurozone); Channel Islands GBP; everything else automatic.

## Q2. The USD and EUR lists

**Answer: A — APPROVE as listed.**

## Q3. US duties

**Answer: NOT SURE.** Re-asked as Q3b with the new cost facts.

## Q4. How do international parcels ship now?

**Answer:** "Use CROOKS Shipping to find the prices — we use a mix of Easyship API + Parcel2Go." Parcel2Go quotes pulled from George's account (F8). Easyship needs a login I can't enter.

## Q5. Shipping rates

Superseded by Q13 (rebuilt on real costs).

## Q6. Channel Islands free Tracked 48 from £30

**Answer: A — YES.** Live (IMP-4). See Q14.

## Q7. International free shipping and unit costs

Not answered — parked. No international threshold.

## Q8. EU VAT

Not answered — parked. Kept as now (buyer pays on delivery).

## Q9. VAT registration

**Answer: CROOKS IS VAT-registered.** Consequences and accountant points in F9.

## Q10. Tee blanks

**Answer: printed in-house at the office.** Follow-up in Q15.

## Q11. Country selector

Not answered here; the theme workstream owns it. It decides whether local prices show before checkout.

---

## Q3b. US duties — collect at checkout? (open)

New facts: Royal Mail to the US via Parcel2Go is duty-prepaid by the sender. If US orders go that way and nothing is collected, CROOKS pays ~£23 duty on an $85 hoodie (~36% of value), leaving ~£37 against £48.73 on a UK sale.

- **A) Yes (recommended):** Shopify collects US duty at checkout as a line item, US only, switched on once every product has an HS code. Shelf price stays $85; buyer sees ~$31 duty.
- **B) No — duties included in price:** tee $40, crewneck/jorts $90, hoodie $110, Cellblock Set $160, Convict Set $200, Puffa $325.
- **C) No change** (accept the duty cost on Royal Mail parcels).

Answer:

## Q12. Eurozone catalog — non-euro EU (open)

- **A) Split (recommended):** new "Eurozone" market (21 euro states + MC, AD, SM, VA, ME, XK) with the EUR list; PL, DK, SE, CZ, HU, RO stay on automatic conversion from £, as approved.
- **B) One EU market in EUR:** non-euro countries get the EUR price converted; Poland's hoodie goes from 318 zł to about 335 zł (~+5%).

Answer:

## Q13. International shipping rates on real costs (open)

Bands by order value, because 31 of 45 products have no weight (one fleece piece or jeans stays under the threshold; a set or two pieces goes over). Margins in F8.

| Zone | Under threshold | From threshold |
|---|---:|---:|
| United States (fixed USD) | $25 under $100 | $30 |
| Eurozone (fixed EUR) | €15 under €90 | €18 |
| Japan, Canada, rest of world | £22.99 under £75 | £30.99 |
| Australia / New Zealand | £20.99 under £75 | £26.99 |
| Rest of Europe | £12.99 (no quotes yet) | £12.99 |

- **A) Approve (recommended).** Light Eurozone parcels to France/Italy run £0.25–£1.00 under cost; everything else covers cost.
- **B) Flat, no loss at any quoted weight:** US $30, Eurozone €18, rest of world £30.99, AU/NZ £26.99.
- **C) Other.**

Answer:

## Q14. Channel Islands carrier (open)

CROOKS Shipping quoted Guernsey order CROOKS-2202 as Parcelforce £16.71. Earlier CI parcels went Royal Mail Tracked 48. Confirm CI will ship Royal Mail Tracked 48 and fix the rule in CROOKS Shipping; on Parcelforce, free CI shipping costs ~£17 an order.

Answer:

## Q15. Tee blanks (open)

Which blank brand and style do you print on? Customs origin is where the blank was made, not where it's printed, so it can't be GB.

Answer:

## Q16. Go for the USD prices (open)

Type **go** and I load the USD list into the US catalog, activate it and run the test script. Or import [artifacts/catalog-prices-USD.csv](artifacts/catalog-prices-USD.csv) yourself.

Answer:
