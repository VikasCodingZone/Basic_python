basic = float(input("Basic salary dalo: "))

if basic <= 10000:
    hra = basic * 0.20
    da = basic * 0.80
elif basic <= 20000:
    hra = basic * 0.25
    da = basic * 0.90
else:
    hra = basic * 0.30
    da = basic * 0.95

gross = basic + hra + da
print("Gross Salary =", gross)

# 🧠 Logic

# Gross Salary = Basic Salary + HRA + DA

# HRA aur DA ka percentage basic salary pe depend karta hai:

# Agar basic <= 10000 → HRA = 20%, DA = 80%

# Agar basic <= 20000 → HRA = 25%, DA = 90%

# Agar basic > 20000 → HRA = 30%, DA = 95%