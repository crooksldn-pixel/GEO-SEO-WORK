"""Shipping matrix: customer rate vs Royal Mail published online price (Oct 2026).
Net = local / FX less 2% conversion fee and 2.7% international card fee (25p ignored on the shipping share)."""
import math

FX = {"USD": 1.334, "EUR": 1.186, "JPY": 210.5, "AUD": 1.922, "CAD": 1.886, "GBP": 1.0}
FEE = 0.02 + 0.027

def net(local, cur):
    g = local / FX[cur]
    return g * (1 - (FEE if cur != "GBP" else 0.017))

def auto(gbp, cur, step):
    v = gbp * FX[cur] * 1.02
    return math.ceil(v / step) * step

# Royal Mail International Tracked, online, Oct 2026: (<=1kg, <=2kg) GBP; US includes 50p PDDP handling
RM = {"US": (17.53 + 0.50, 20.20 + 0.50), "EU-Z1": (15.15, 16.35), "EU-Z2": (16.35, 18.45),
      "ROW-Z1": (24.65, 29.90), "ROW-Z2": (27.90, 37.55)}

rows = [
    ("United States", 26, "USD", (25, 30), ["US"]),
    ("Eurozone", 15.95, "EUR", (20, 25), ["EU-Z1", "EU-Z2"]),
    ("World Zone 1 (JP, CA, ID...)", auto(18.99, "JPY", 100), "JPY", (auto(25.99, "JPY", 100), auto(31.99, "JPY", 100)), ["ROW-Z1"]),
    ("World Zone 2 (AU, NZ)", auto(18.99, "AUD", 1), "AUD", (auto(29.99, "AUD", 1), auto(39.99, "AUD", 1)), ["ROW-Z2"]),
]
for m, cur_now, cur, prop, keys in rows:
    for k in keys:
        c1, c2 = RM[k]
        now1, now2 = net(cur_now, cur) - c1, net(cur_now, cur) - c2
        p1, p2 = net(prop[0], cur) - c1, net(prop[1], cur) - c2
        print(f"{m} [{k}] now {cur_now} {cur}: {now1:+.2f} (1kg) {now2:+.2f} (2kg) | proposed {prop} -> {p1:+.2f} / {p2:+.2f}")
print("US >2kg $50 net", round(net(50, "USD"), 2), "vs Royal Mail Tracked Heavier 3kg 32.40 + 0.50")
