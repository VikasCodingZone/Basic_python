#30. Attendance + Medical cause
total = int(input("Total classes held: "))
attended = int(input("Classes attended: "))

percentage = (attended / total) * 100
print("Attendance % =", percentage)

if percentage >= 75:
    print("Exam me baithne ki permission hai")
else:
    medical = input("Kya medical cause hai? (Y/N): ")
    if medical.upper() == 'Y':
        print("Medical cause hai, isliye Exam me baith sakte ho")
    else:
        print("Exam me baithne ki permission nahi hai")