#2. Maximum between three numbers
a = int(input("Pehla number: "))
b = int(input("Dusra number: "))
c = int(input("Tisra number: "))

if a >= b and a >= c:
    print("Maximum:", a)
elif b >= a and b >= c:
    print("Maximum:", b)
else:
    print("Maximum:", c)