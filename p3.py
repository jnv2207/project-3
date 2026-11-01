
# Project: Student Data Organizer
# PR 3: Collection Manipulator

# List to store all student records
students = []

# Dictionary to store student information using Student ID
student_data = {}

# Set to store unique subjects
unique_subjects = set()


def show_menu():
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")


# 1. Add Student
def add_student():
    print("\nEnter student details:")

    student_id = input("Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    if student_id in student_data:
        print("Student ID already exists!")
        return

    name = input("Name: ").strip()

    try:
        age = int(input("Age: "))  # Type casting
        if age <= 0:
            print("Age must be positive!")
            return
    except ValueError:
        print("Please enter a valid age!")
        return

    grade = input("Grade: ").strip()
    dob = input("Date of Birth (YYYY-MM-DD): ").strip()

    subjects_input = input(
        "Subjects (comma-separated): "
    )

    # Convert comma-separated input into a list
    subjects_list = [
        subject.strip()
        for subject in subjects_input.split(",")
        if subject.strip()
    ]

    # Set removes duplicate subjects
    subjects_set = set(subjects_list)

    # Tuple stores fixed student ID and date of birth
    personal_info = (student_id, dob)

    # Dictionary stores the student's details
    record = {
        "personal_info": personal_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": sorted(subjects_set)
    }

    # Add record to the list and dictionary
    students.append(record)
    student_data[student_id] = record

    # Add subjects to the unique subject set
    unique_subjects.update(subjects_set)

    print("\nStudent added successfully!")


# 2. Display All Students
def display_students():
    print("\n--- Display All Students ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        student_id, dob = student["personal_info"]

        subjects = ", ".join(student["subjects"])

        # Different string formatting methods
        print(
            f"Student ID: {student_id} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']} | "
            f"Subjects: {subjects}"
        )

        print("Date of Birth: {}".format(dob))

        print("-" * 50)


# 3. Update Student Information
def update_student():
    print("\n--- Update Student Information ---")

    student_id = input("Enter Student ID: ").strip()

    if student_id not in student_data:
        print("Student not found!")
        return

    student = student_data[student_id]

    print("1. Update Age")
    print("2. Update Grade")
    print("3. Update Subjects")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            age = int(input("Enter new age: "))

            if age <= 0:
                print("Age must be positive!")
                return

            student["age"] = age
            print("Age updated successfully!")

        except ValueError:
            print("Please enter a valid age!")

    elif choice == "2":
        student["grade"] = input("Enter new grade: ")
        print("Grade updated successfully!")

    elif choice == "3":
        subjects_input = input(
            "Enter new subjects (comma-separated): "
        )

        subjects = {
            subject.strip()
            for subject in subjects_input.split(",")
            if subject.strip()
        }

        student["subjects"] = sorted(subjects)

        # Recalculate unique subjects from all current records
        unique_subjects.clear()

        for record in students:
            unique_subjects.update(record["subjects"])

        print("Subjects updated successfully!")

    else:
        print("Invalid choice!")

    # The personal_info tuple remains unchanged.


# 4. Delete Student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID to delete: ").strip()

    if student_id not in student_data:
        print("Student not found!")
        return

    student = student_data[student_id]

    # Remove record from the main list
    students.remove(student)

    # Delete record using the del keyword
    del student_data[student_id]

    # Update the unique subject set
    unique_subjects.clear()

    for record in students:
        unique_subjects.update(record["subjects"])

    print("Student deleted successfully!")


# 5. Display Unique Subjects
def display_subjects():
    print("\n--- Subjects Offered ---")

    if not unique_subjects:
        print("No subjects available.")
        return

    for subject in sorted(unique_subjects):
        print(subject)


# Main program
def main():
    print("Welcome to the Student Data Organizer!")

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_subjects()

        elif choice == "6":
            print(
                "\nThank you for using the "
                "Student Data Organizer!"
            )
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


# Execute the program
if __name__ == "__main__":
    main()
