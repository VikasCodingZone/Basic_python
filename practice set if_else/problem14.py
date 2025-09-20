
#14. Triangle Valid (by angles)
a = int(input("Angle 1: "))
b = int(input("Angle 2: "))
c = int(input("Angle 3: "))

if a + b + c == 180:
    print("Triangle valid hai")
else:
    print("Triangle valid nahi hai")


# if (a+b>c) → check karta hai side a + b ka sum c se bada hai ki nahi.

# if (a+c>b) → check karta hai side a + c ka sum b se bada hai ki nahi.

# if (b+c>a) → check karta hai side b + c ka sum a se bada hai ki nahi.

# Agar teeno condition true → triangle valid.

# Agar ek bhi condition fail → else chalega → "Triangle valid nahi hai".