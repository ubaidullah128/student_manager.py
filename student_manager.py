students = {}

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists!\n")
        return
    try:
        marks = float(input("Enter marks out of 100: "))
        students[name] = marks
        print("Student added successfully!\n")
    except:
        print("Invalid marks!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- Student Records ---")
    for name, marks in students.items():
        print(f"{name} : {marks} marks")
    print()

def update_marks():
    name = input("Enter student name to update: ")
    if name not in students:
        print("Student not found.\n")
        return
    try:
        marks = float(input("Enter new marks: "))
        students[name] = marks
        print("Marks updated successfully!\n")
    except:
        print("Invalid input!\n")

def calculate_percentage():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found.\n")
        return
    percentage = (students[name] / 100) * 100
    print(f"{name}'s Percentage: {percentage}%\n")

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
        print("===== Student Manager CLI =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Calculate Percentage")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            calculate_percentage()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
