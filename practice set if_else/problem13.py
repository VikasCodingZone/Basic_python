#13. Count Notes
amount = int(input("Amount dalo: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} ke {count} note")


#         Step by Step Logic:

# Loop har note ke liye chalega.

# Pehle 2000 dekhega → fir 500 → fir 200 … last 1 tak.

# if amount >= note:

# Check karta hai ki current note se amount cover ho sakta hai ya nahi.

# Agar amount us note ke barabar ya bada hai → to use karenge.

# count = amount // note:

# // matlab integer division.

# Isse pata chalega ki kitne note lagenge.

# Example: 3700 // 2000 = 1 → ek 2000 ka note chahiye.

# amount = amount % note:

# % remainder deta hai.

# Matlab current note use karne ke baad kitna paisa bacha.

# Example: 3700 % 2000 = 1700 → ab 1700 bacha.

# print(f"{note} ke {count} note"):

# Output me batata hai ki kitne note chahiye.