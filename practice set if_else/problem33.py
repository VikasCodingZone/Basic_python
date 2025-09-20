#33. 4 digit number ko reverse karna
num = int(input("4 digit number dalo: "))

reverse = int(str(num)[::-1])

print("Reverse number =", reverse)

# 🧠 Logic (Simple words me)

# Input lena:

# num = int(input(...)) → User se 4-digit number le rahe hain.

# Example: num = 1234

# Number ko string me convert karna:

# str(num) → Number ko string me convert kar dete hain, taaki usko reverse kar sakein.

# Example: str(1234) → "1234"

# String reverse karna:

# "1234"[::-1] → Python ka slicing trick [start:stop:step].

# [::-1] ka matlab hai piche se aage tak read karo, yaani reverse.

# Result: "4321"

# Dubara integer me convert karna:

# int("4321") → 4321

# Kyunki final output number format me chahiye, na ki string.

# Print karna:

# print("Reverse number =", reverse) → Output dikha deta hai.

# 📝 Example
# Input	Step 1 (String)	Step 2 (Reverse)	Step 3 (Integer)	Output
# 1234	"1234"	"4321"	4321	4321
# 5982	"5982"	"2895"	2895	2895