student_grade = int(input("Input your grade: "))

if student_grade >= 90 and student_grade <= 100:
    print("Grade A")
elif student_grade >= 80 and student_grade <= 89:
    print("Grade B")
elif student_grade >= 70 and student_grade <= 79:
    print("Grade C")
elif student_grade >= 60 and student_grade <= 69:
    print("Grade D")
elif student_grade < 60 and student_grade >= 0:
    print("Grade F")
else:
    print("Invalid Input")