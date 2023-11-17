print("---Grade Statics---")
print("-------------------")


nStudents = int(input("Enter the number of students: "))

# Collecting data from each student
def store_and_calculate():
    name = input("Student's name: ")
    note1 = float(input("First note: "))
    note2 = float(input("Second note: "))
    note3 = float(input("Third note: "))

    avarageGrade = (note1 + note2 + note3)/3

    listNotes = [note1, note2, note3]
    listNotes.sort()
    
    highestGrade = listNotes[2]
    lowestGrade = listNotes[0]

    infoStudent.append(name)
    infoStudent.append(avarageGrade)
    infoStudent.append(lowestGrade)
    infoStudent.append(highestGrade)

    return infoStudent

infoStudent = []
student = store_and_calculate()
print(student)
