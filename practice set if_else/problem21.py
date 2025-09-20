#21. Bijli ka bill nikalna
units = int(input("Bijli ke units dalo: "))

if units <= 50:
    amt = units * 0.50
elif units <= 150:
    amt = 50 * 0.50 + (units - 50) * 0.75
elif units <= 250:
    amt = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
else:
    amt = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

surcharge = amt * 0.20
total = amt + surcharge

print("Total Electricity Bill =", total)


# Units ke hisaab se rate lagega aur 20% extra surcharge add hoga.

# 📖 Explanation

# ⚡ Units = jitna bijli use kiya.
# ⚡ Rates slab ke hisaab se badhte hain:

# Pehle 50 units → ₹0.50 per unit

# Next 100 units (51–150) → ₹0.75 per unit

# Next 100 units (151–250) → ₹1.20 per unit

# Above 250 → ₹1.50 per unit

# 🔹 Fir 20% surcharge (tax/extra charge) add hota hai.
# 🔹 Final total bill = amount + surcharge.

# 🧠 Logic (Simple Words Me)

# Agar units ≤ 50 → bill = units × 0.50

# Agar units 51–150 →

# Pehle 50 × 0.50

# Baaki (units–50) × 0.75

# Agar units 151–250 →

# Pehle 50 × 0.50

# Next 100 × 0.75

# Baaki (units–150) × 1.20

# Agar units > 250 →

# Pehle 50 × 0.50

# Next 100 × 0.75

# Next 100 × 1.20

# Baaki (units–250) × 1.50

# Surcharge = 20% of bill.

# Total Bill = Bill + Surcharge.

# 🧾 Example

# 👉 Suppose units = 120

# 50 × 0.50 = ₹25

# 70 × 0.75 = ₹52.5

# Amount = 77.5

# Surcharge = 20% of 77.5 = 15.5

# Total = 93.0