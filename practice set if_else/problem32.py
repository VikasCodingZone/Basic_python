#32. Employee service place decide karna
age = int(input("Age dalo: "))
sex = input("Sex (M/F) dalo: ")
married = input("Married (Y/N) dalo: ")

if sex.upper() == 'F':
    print("Urban areas me kaam karegi")
elif sex.upper() == 'M' and 20 <= age <= 40:
    print("Kahin bhi kaam kar sakta hai")
elif sex.upper() == 'M' and 40 < age <= 60:
    print("Urban areas me hi kaam karega")
else:
    print("ERROR")

#     Logic (Simple words me)

# Sex check:

# Agar female hai (F) → Hamesha Urban areas me kaam karegi.

# Male & age check:

# Agar male hai (M) aur age 20-40 ke beech → Kahin bhi kaam kar sakta hai.

# Agar male hai (M) aur age 41-60 ke beech → Sirf Urban areas me kaam karega.

# Other cases:

# Agar input galat hai (jaise age 0 ya 100+ ya sex galat input) → "ERROR" print hoga.

# 📝 Example Inputs & Outputs

# Input:
# Age = 25, Sex = M, Married = Y
# Output:

# Kahin bhi kaam kar sakta hai


# Input:
# Age = 45, Sex = M, Married = N
# Output:

# Urban areas me hi kaam karega


# Input:
# Age = 30, Sex = F, Married = Y
# Output:

# Urban areas me kaam karegi


# Input:
# Age = 65, Sex = M, Married = N
# Output: