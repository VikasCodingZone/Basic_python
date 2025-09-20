#16. Type of Triangle
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Working:

# Equilateral Triangle (समबाहु त्रिभुज)

# Sabhi sides barabar (equal) hoti hain.

# Condition: a == b == c

# Example: 5, 5, 5

# Isosceles Triangle (समद्विबाहु त्रिभुज)

# 2 sides barabar hoti hain.

# Condition: a == b or b == c or a == c

# Example: 5, 5, 7

# Scalene Triangle (विषमबाहु त्रिभुज)

# Sabhi sides alag hoti hain.

# Condition: else (jab upar ki koi condition satisfy na ho).

# Example: 3, 4, 5 