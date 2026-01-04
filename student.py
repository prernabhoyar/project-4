student_grades={}
#add student
def add_student(name,grade):
    student_grades[name]=grade
    print(f"Student {name} with grade{grade} added successfully")
#update student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"Student {name} with updated grade {grade}")
    else:
        print("Student not found")

#delete student
def del_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} deleted")
    else:
        print("Student not found")

#view students
def display():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print("Data not found!")
    
def main():
    while True:
        choice=int(input("Enter the choice\n1.ADD STUDENT\n2.UPDATE STUDENT\n3.DELETE STUDENT\n4.VIEW\n5.EXIT"))
        if choice==1:
            name=input("Enter the name of student: ")
            grade=int(input("Enter the grade of student: "))
            add_student(name,grade)
        elif choice==2:
            name=input("Enter the name of student: ")
            grade=int(input("Enter the grade of student: "))
            update_student(name,grade)
        elif choice==3:
            name=input("Enter the name of student: ")
            del_student(name)    
        elif choice==4:
            display()        
        elif choice==5:
            print("Closing the program....") 
            break
    else:
        print("Invalid input")
        
main()
    