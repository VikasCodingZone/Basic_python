#6. Leap Year
year = int(input("Year dalo: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year hai")
else:
    print("Leap year nahi hai")


# Rule of Leap Year:

# Agar year % 400 == 0 → Leap year hai.
# (Matlab 400 se completely divide ho raha hai, jaise 1600, 2000).

# Agar year % 4 == 0 aur year % 100 != 0 → Leap year hai.
# (Matlab 4 se to divide ho raha hai par 100 se nahi, jaise 2024, 2028).

# Baki sab leap year nahi hai.

# Code me logic:
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# (year % 400 == 0)
# → Directly leap year (special case for century years).

# or
# → Matlab agar pehla false ho jaye to doosra check hoga.

# (year % 4 == 0 and year % 100 != 0)
# → Matlab year 4 se divide ho raha hai lekin 100 se divide nahi ho raha.

# Example 1:

# year = 2000

# 2000 % 400 == 0 ✅ → Leap year

# Example 2:

# year = 2024

# 2024 % 400 == 0 ❌

# 2024 % 4 == 0 ✅ aur 2024 % 100 != 0 ✅ → Leap year

# Example 3:

# year = 1900

# 1900 % 400 == 0 ❌

# 1900 % 4 == 0 ✅ but 1900 % 100 != 0 ❌ → Not a leap year    