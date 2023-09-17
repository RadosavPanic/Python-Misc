from student import Student

student1 = Student("John", "Doe", "IT14", 8.1)
student2 = Student("Mark", "Darm", "IT31", 7.8)
student3 = Student("Ana", "Morrison", "IT40", 7.6)

students = [student1, student2, student3]

for i in range(len(students)):
    print(students[i])

students.sort()

print("After sort:")
for i in range(len(students)):
    print(students[i])

file = open("students_list.txt", "a+")
for i in range(len(students)):
    file.write(students[i].__str__() + "\n")
file.close()

try:
    file = open("students_list.txt", "r")
    print(file.readlines())
except IOError as Error:
    print(f"Error occured: {Error}")
else:
    print("Successfully read and closed file.")
    file.close()

print(f"Number of students: {Student.student_count()}")
