student={
    "Iram_Malik":80,
    "nazima":82,
    "raza":85
}
print("student names and marks are:")
for name, marks in student.items():
    print(name, ":", marks)

student["abida"] = 83
print ("\nAfter adding new student:" )
for name, marks in student.items():
    print(name, ":", marks)

student["Iram_Malik"] = 92
print ("\nAfter updating marks of Iram_Malik:" )
for name, marks in student.items():
    print(name, ":", marks)


del student["raza"]
print ("\nAfter deleting raza:" )
for name, marks in student.items():
    print(name, ":", marks)


highest_student = ""
highest_marks = 0

for name, marks in student.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = name

print("\nStudent with highest marks:", highest_student)
print("Highest marks:", highest_marks)

total = 0
for marks in student.values():
    total = total + marks
average = total / len(student)
print("Average marks:", average)



#Note
#student.items()    keys + values
#student.keys()     keys only
#student.values()   values only

