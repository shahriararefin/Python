student_grades = {}

def addStudent():
    while True:
        name = input("Enter student name(or toye 'done' to stop): ").strip()
        if name.lower()== 'done':
            break
        try:
            grade = float(input(f"Enter grade for {name}: "))
            student_grades[name] = grade
        except ValueError:
            print("Invalid input. Please enter a numeric value: ")
            
def retrieveGrade():
    name = input("Enter name to to get grade: ").strip()
    grade = student_grades.get(name)
    if grade is not None:
        print(f"{name}'s grade is : {grade}")
    else:
        print(f"No record found for {name}")
        
print("Welcome to Student Grade Tracket")
while True:
    print("\nMenu:")
    print("1. Add student grades")
    print("2. Retrieve a student's grade")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, 3): ").strip()
    
    if choice == '1':
        addStudent()
    elif choice == '2':
        retrieveGrade()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")