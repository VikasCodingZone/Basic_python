
#19. Percentage & Grade
p = int(input("Physics marks: "))
c = int(input("Chemistry marks: "))
b = int(input("Biology marks: "))
m = int(input("Maths marks: "))
comp = int(input("Computer marks: "))

total = p + c + b + m + comp
percentage = (total / 500) * 100

print("Percentage =", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")