studentList = []

def studentRecords(student):
    global studentList
    studentList.append(student)
    
for _ in range(5):
    student = input("Input student to add: ")
    studentRecords(student)

print(studentList)