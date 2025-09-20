#15. Triangle Valid (by sides)
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    print("Triangle valid hai")
else:
    print("Triangle valid nahi hai")



# User input le raha hai

# a = side 1

# b = side 2

# c = side 3

# Condition check karta hai (Triangle Inequality Theorem ke basis par):

# a + b > c

# a + c > b

# b + c > a

# Agar ye teeno sahi hain → valid triangle.
# Agar ek bhi galat ho → triangle valid nahi.

# Output:

# Agar conditions true hain → "Triangle valid hai"

# Agar ek bhi false ho → "Triangle valid nahi hai"    