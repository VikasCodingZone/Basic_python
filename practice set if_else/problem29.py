#29. Attendance % aur exam allow
total = int(input("Total classes held: "))
attended = int(input("Classes attended: "))

percentage = (attended / total) * 100
print("Attendance % =", percentage)

if percentage >= 75:
    print("Exam me baithne ki permission hai")
else:
    print("Exam me baithne ki permission nahi hai")

#     Logic (Simple words me)

# Total classes: Ye bata raha hai ki semester me kitni classes hui.

# Attended classes: Ye bata raha hai ki student ne kitni classes attend ki.

# Percentage calculate:

# percentage = attendence / total * 100

# Example: Total = 80, Attended = 60 → (60/80)*100 = 75%

# Permission check:

# Agar percentage ≥ 75 → Student ko exam me baithne ki permission milti hai.

# Agar percentage < 75 → Student ko permission nahi milti.

# 📝 Example

# Input:
# Total classes: 100
# Classes attended: 80

# Calculation:
# Percentage = (80/100)*100 = 80%

# Output:

# Attendance % = 80.0
# Exam me baithne ki permission hai


# Input:
# Total classes: 100
# Classes attended: 60

# Calculation:
# Percentage = (60/100)*100 = 60%

# Output:

# Attendance % = 60.0
# Exam me baithne ki permission nahi hai