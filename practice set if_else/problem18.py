#18. Profit or Loss
cp = float(input("Cost price dalo: "))
sp = float(input("Selling price dalo: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("Na profit na loss")


# Cost Price (CP): jis rate pe maal kharida

# Selling Price (SP): jis rate pe maal becha

# 🧠 Logic

# Agar sp > cp → bechne ki price jyada → Profit

# Agar cp > sp → kharidne ki price jyada → Loss

# Agar dono barabar → Na profit, na loss