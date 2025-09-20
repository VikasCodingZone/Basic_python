#17. Roots of Quadratic Equation
import math

a = float(input("a dalo: "))
b = float(input("b dalo: "))
c = float(input("c dalo: "))

d = b*b - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Do real roots:", root1, "aur", root2)
elif d == 0:
    root = -b / (2*a)
    print("Ek hi real root:", root)
else:
    print("Imaginary roots hai")

# d > 0 → 2 alag-alag real roots

# d == 0 → ek hi real root (repeated root)

# d < 0 → imaginary (complex) roots    