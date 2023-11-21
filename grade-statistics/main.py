print("---Grade Statics---")
print("-------------------")


nStudents = int(input("Enter the number of students: "))

# Collecting data from each student
def store_and_calculate():
    infoStudent = []
    name = input("Student's name: ")
    note1 = float(input("First note: "))
    note2 = float(input("Second note: "))
    note3 = float(input("Third note: "))

    avarageGrade = (note1 + note2 + note3)/3

    listNotes = [note1, note2, note3]
    listNotes.sort()
    
    highestGradeS = listNotes[2]
    lowestGradeS = listNotes[0]

    infoStudent.append(name)
    infoStudent.append(avarageGrade)
    infoStudent.append(lowestGradeS)
    infoStudent.append(highestGradeS)


    return infoStudent

listStudents = []

# Creating general list of students
while nStudents != 0:

    listStudents.append(list(store_and_calculate()))

    nStudents -= 1

generalAverage = 0
highestGrade = 0
lowestGrade = 100

# Printing information for each student
for student in listStudents:
    print("O aluno {} ficou com a média {:.2f}! A nota mais baixa foi {:.1f} e a mais alta foi {:.1f}."
          .format(student[0], student[1], student[2], student[3]))
    
    generalAverage += student[1]
    
    # Making comparisons to obtain final result 
    if student[2] < lowestGrade:
        lowestGrade = student[2]
    
    if student[3] > highestGrade:
        highestGrade = student[3]
    
# Priting final result
print("-----------------------------------------------------------------------")
print("A média geral da turma foi de {:.2f}! A nota mais alta foi {:.1f} e a mais baixa foi {:.1f}"
      .format(generalAverage/len(listStudents), highestGrade, lowestGrade))
    
