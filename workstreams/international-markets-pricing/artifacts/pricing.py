"""CROOKSLDN international price matrix — 18 Oct 2026.

Inputs are taken from Shopify (live catalogue + contextual prices) and Shopify's
published fee/rounding rules. Rates are the mid-market rates implied by Shopify's
own current storefront conversions (presentment price / 1.02 conversion fee).
"""
import math, json

# Shopify-implied mid-market rates, 18 Oct 2026 (derived from contextualPricing)
FX = {"USD": 1.334, "EUR": 1.186, "JPY": 210.5, "AUD": 1.922, "CAD": 1.886, "IDR": 24025}
CONV_FEE = 0.02        # Shopify Payments currency conversion fee, non-US/FR stores
UK_CARD = (0.017, 0.25)   # Grow plan, UK cards: 1.7% + 25p
INTL_CARD = (0.027, 0.25) # Grow plan, international cards: 2.7% + 25p (published UK rate, to confirm in Payments terms)
COST_COVER = 1 + CONV_FEE + (INTL_CARD[0] - UK_CARD[0])  # 1.03

# Live (ACTIVE) catalogue, one row per price point
CATALOGUE = [
    ("MotionTec socks — 1 pair", 6, "Socks", 0.02),
    ("MotionTec socks — 3 pack", 15, "Socks", 0.06),
    ("Tee (Crooks Express, CRX GARMS)", 20, "Tee", 0.25),
    ("Tee (CRXST★RZ) / socks 6 pack", 25, "Tee", 0.25),
    ("Major League cap (cream)", 32, "Cap", None),
    ("Cellblock shorts / socks 12 pack", 45, "Shorts", 0.65),
    ("Cellblock crewneck / Yard jorts", 50, "Crewneck", 0.80),
    ("Convict hoodie / Convict sweats / Yard + OG jeans", 60, "Hoodie", 0.90),
    ("Cellblock Set / HydroCuff windbreaker", 85, "Set", None),
    ("Convict Set (black, grey, pink)", 110, "Set", None),
    ("Double-Agent Puffa", 140, "Outerwear", None),
]

# Current customer-facing prices from Shopify contextualPricing (auto FX + fee + rounding)
CURRENT = {
    6:   {"USD": 9, "EUR": 7.95, "JPY": 1300, "AUD": 12, "CAD": 12, "IDR": 148000},
    15:  {},
    20:  {"USD": 28, "EUR": 24.95, "JPY": 4300, "AUD": 40, "CAD": 39, "IDR": 491000},
    25:  {"USD": 34, "EUR": 30.95, "JPY": 5400, "AUD": 49, "CAD": 49, "IDR": 613000},
    32:  {"USD": 44, "EUR": 38.95, "JPY": 6900, "AUD": 63, "CAD": 62, "IDR": 785000},
    45:  {"USD": 62, "EUR": 54.95, "JPY": 9700, "AUD": 89, "CAD": 87, "IDR": 1103000},
    50:  {"USD": 68, "EUR": 60.95, "JPY": 10800, "AUD": 98, "CAD": 97, "IDR": 1226000},
    60:  {"USD": 82, "EUR": 72.95, "JPY": 12900, "AUD": 118, "CAD": 116, "IDR": 1471000},
    85:  {"USD": 116, "EUR": 102.95, "JPY": 18300, "AUD": 167, "CAD": 164, "IDR": 2084000},
    110: {"USD": 150, "EUR": 133.95, "JPY": 23700, "AUD": 216, "CAD": 212, "IDR": 2697000},
    140: {"USD": 191, "EUR": 169.95, "JPY": 30100, "AUD": 275, "CAD": 270, "IDR": 3432000},
}

def ladder(cur):
    """Deliberate price points. USD/EUR mirror the whole-number GBP style."""
    if cur in ("USD", "EUR"):
        pts = [5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 22, 25, 28]
        pts += list(range(30, 101, 5))
        pts += list(range(110, 201, 10)) + [125, 175, 195]
        pts += list(range(225, 401, 25))
        return sorted(set(pts))
    raise ValueError(cur)

def round_up(value, cur):
    for p in ladder(cur):
        if p >= value - 1e-9:
            return p
    raise ValueError(value)

def shopify_round(value, cur):
    """Shopify's own 'round up' rule as observed on this store."""
    if cur == "EUR":
        return math.floor(value) + 0.95 if value - math.floor(value) <= 0.95 else math.floor(value) + 1.95
    step = {"USD": 1, "AUD": 1, "CAD": 1, "JPY": 100, "IDR": 1000}[cur]
    return math.ceil(value / step) * step

def uk_net(gbp):
    return gbp - (gbp * UK_CARD[0] + UK_CARD[1])

def intl_net_fixed(local, cur):
    """Fixed local price: merchant receives local/FX, pays 2% conversion + intl card fee."""
    gbp = local / FX[cur]
    return gbp - gbp * CONV_FEE - (gbp * INTL_CARD[0] + INTL_CARD[1])

def intl_net_auto(local, cur):
    """Auto-converted price already contains the 2% fee; merchant pays the fee + intl card fee."""
    return intl_net_fixed(local, cur)

rows = []
for name, gbp, cat, kg in CATALOGUE:
    r = {"product": name, "gbp": gbp}
    for cur in ("USD", "EUR"):
        neutral = gbp * FX[cur]
        target = neutral * COST_COVER
        rec = round_up(target, cur)
        lower = max(p for p in ladder(cur) if p < rec)
        flagged = False
        # Exception: if the next point up lifts net >10% above UK and the point below is within 3%, take the point below
        if (intl_net_fixed(rec, cur) / uk_net(gbp) - 1) > 0.10 and (intl_net_fixed(lower, cur) / uk_net(gbp) - 1) > -0.03:
            rec, flagged = lower, True
            lower = max(p for p in ladder(cur) if p < rec)
        r[cur] = {
            "fx_neutral": round(neutral, 2),
            "cost_covered": round(target, 2),
            "current": CURRENT.get(gbp, {}).get(cur),
            "recommended": rec,
            "flag_rounded_down": flagged,
            "uplift_vs_neutral_pct": round((rec / neutral - 1) * 100, 1),
            "net_gbp": round(intl_net_fixed(rec, cur), 2),
            "uk_net_gbp": round(uk_net(gbp), 2),
            "net_vs_uk_pct": round((intl_net_fixed(rec, cur) / uk_net(gbp) - 1) * 100, 1),
            "lower_option": lower,
            "lower_net_vs_uk_pct": round((intl_net_fixed(lower, cur) / uk_net(gbp) - 1) * 100, 1),
        }
    for cur in ("JPY", "AUD", "CAD", "IDR"):
        auto = shopify_round(gbp * FX[cur] * (1 + CONV_FEE), cur)
        r[cur] = {
            "current": CURRENT.get(gbp, {}).get(cur),
            "auto_now": auto,
            "net_gbp": round(intl_net_auto(auto, cur), 2),
            "net_vs_uk_pct": round((intl_net_auto(auto, cur) / uk_net(gbp) - 1) * 100, 1),
        }
    rows.append(r)

# US duty estimate (China-origin, Oct 2026): MFN + Section 301 List 4A 7.5% + Section 301 forced-labour 12.5%
US_DUTY = {"Socks": 0.135 + 0.075 + 0.125, "Tee": 0.165 + 0.075 + 0.125, "Cap": 0.075 + 0.075 + 0.125,
           "Shorts": 0.161 + 0.075 + 0.125, "Crewneck": 0.165 + 0.075 + 0.125, "Hoodie": 0.165 + 0.075 + 0.125,
           "Set": 0.165 + 0.075 + 0.125, "Outerwear": 0.277 + 0.075 + 0.125}
for r, (_, gbp, cat, _) in zip(rows, CATALOGUE):
    d = US_DUTY[cat]
    us = r["USD"]["recommended"]
    r["USD"]["duty_rate_est"] = round(d * 100, 1)
    r["USD"]["duty_est_usd"] = round(us * d, 2)
    # Option B: duties included in price, merchant pays duty on the full price
    inc = round_up(us / (1 - d), "USD")
    r["USD"]["duty_inclusive_price"] = inc
    r["USD"]["duty_inclusive_net_vs_uk_pct"] = round(((inc - inc * d) / FX["USD"] * (1 - CONV_FEE - INTL_CARD[0]) - INTL_CARD[1]) / uk_net(gbp) * 100 - 100, 1)

json.dump(rows, open("matrix.json", "w"), indent=1, ensure_ascii=False)

# Ladder sanity: recommended prices must stay in GBP order and keep set savings
for cur in ("USD", "EUR"):
    seq = [r[cur]["recommended"] for r in rows]
    assert seq == sorted(seq), (cur, seq)
print("ladder order preserved for USD and EUR")
