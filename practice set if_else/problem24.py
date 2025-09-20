#24. Bonus calculation
salary = float(input("Salary dalo: "))
year = int(input("Service years dalo: "))

if year > 5:
    bonus = salary * 0.05
    print("Bonus =", bonus)
else:
    print("Bonus nahi milega")


#     📖 Explanation

# Salary = employee ki monthly ya yearly basic salary.

# Year = employee ne kitne saal kaam kiya hai company me.

# Rule: Agar service 5 saal se zyada hai → 5% salary bonus milega.

# Nahi toh → bonus nahi milega.

# 🧠 Logic (Simple Words Me)

# Input me salary aur service years lete hain.

# Agar year > 5 → bonus = salary × 0.05 (yaani 5% salary extra).

# Else (5 ya usse kam saal) → bonus = 0.

# 🧾 Example

# 👉 Salary = ₹20,000, Service years = 7

# Condition true (7 > 5)

# Bonus = 20000 × 0.05 = ₹1000

# 👉 Salary = ₹15,000, Service years = 4

# Condition false (4 > 5 nahi hai)

# Bonus = nahi milega.