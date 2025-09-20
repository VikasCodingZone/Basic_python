#12. Days in Month
month = int(input("Month number dalo (1-12): "))

if month in [1,3,5,7,8,10,12]:
    print("31 din")
elif month in [4,6,9,11]:
    print("30 din")
elif month == 2:
    print("28 ya 29 din (leap year pe depend karega)")
else:
    print("Galat month number")

# 🔹 Pure Logic (Simple Words Me):

# Saal ke kuch mahine 31 din ke hote hain → (Jan, Mar, May, Jul, Aug, Oct, Dec).
# → Matlab agar user in me se koi month number de (1,3,5,7,8,10,12) → print "31 din".

# Saal ke kuch mahine 30 din ke hote hain → (Apr, Jun, Sep, Nov).
# → Matlab agar user in me se koi month number de (4,6,9,11) → print "30 din".

# February (2nd month) alag hota hai → usme 28 din ya 29 din ho sakte hain.

# Normal saal me → 28 din.

# Leap year me → 29 din.

# Agar user 1 se 12 ke alawa koi month number daale → wo galat input hai, isliye "Galat month number" print hoga.    