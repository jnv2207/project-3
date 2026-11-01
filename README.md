# project-3
# 🎓 Student Data Organizer
### 📚 Collection Manipulator | Python Project

<p align="center">
  <img src ="C:\Users\dell\Downloads\Student Data Organizer Showcase.png" >
</p>

---

## 📌 About the Project

The **Student Data Organizer** is a menu-driven Python application developed to manage student records efficiently.

It allows users to add, display, update, and delete student information. It can also display all unique subjects offered by students.

This project demonstrates the practical use of Python collection data types, string formatting, mutability, immutability, type casting, and the `del` keyword.

## 🎯 Objectives

- Manage multiple student records efficiently.
- Understand Lists, Tuples, Sets, and Dictionaries.
- Demonstrate mutable and immutable data types.
- Apply string formatting techniques.
- Perform type casting on user input.
- Delete student records using the `del` keyword.

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Student | Add a new student's details. |
| 📋 Display Students | View all registered students. |
| ✏️ Update Student | Modify age, grade, or subjects. |
| 🗑️ Delete Student | Remove a student using their ID. |
| 📚 Display Subjects | Show unique subjects without duplicates. |
| 🚪 Exit | Exit the application. |

## 🛠️ Technologies Used

- **Language:** Python 3
- **Editor:** Visual Studio Code / IDLE
- **Version Control:** Git
- **Repository:** GitHub

## 🧠 Python Concepts Implemented

- **List:** Stores multiple student records.
- **Tuple:** Stores fixed information, such as student ID and date of birth.
- **Set:** Stores unique subjects without duplicates.
- **Dictionary:** Organizes student information using student IDs as keys.
- **String Formatting:** Displays information in a readable format.
- **Type Casting:** Converts input into appropriate data types.
- **Mutability and Immutability:** Demonstrates changeable and unchangeable data.
- **`del` Keyword:** Removes student records.

## 🔄 Project Workflow

```text
          START
            |
            v
    Display Main Menu
            |
            v
    Select an Operation
            |
     +------+------+-------+-------+
     |      |      |       |       |
     v      v      v       v       v
    Add   Display Update  Delete Subjects
 Student Students Student Student  Offered
     |      |      |       |       |
     +------+------+-------+-------+
                    |
                    v
              Return to Menu
                    |
                    v
              Exit Selected?
                /       \
              No         Yes
              |           |
              v           v
          Main Menu      END
```

## 📸 VIDEO EXPLAINATION
https://drive.google.com/file/d/1kuMkv2FdLl804MuDXRXVpwbTCGOJZtLk/view?usp=drive_link

### 1. Main Menu

![Student Data Organizer Main Menu](screenshots/main_menu.png)

### 2. Adding a Student

![Adding Student Details](screenshots/add_student.png)

### 3. Displaying Student Records

![Displaying Student Records](screenshots/display_students.png)

### 4. Updating Student Information

![Updating Student Information](screenshots/update_student.png)

### 5. Displaying Unique Subjects

![Displaying Unique Subjects](screenshots/subjects.png)

### 6. Deleting a Student

![Deleting a Student](screenshots/delete_student.png)

> **Note:** Add your actual screenshots to the `screenshots` folder using the filenames shown above. The images will appear here when you upload the files to GitHub.

## 💻 Sample Output

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice: 1

Enter student details:
Student ID: 101
Name: Alice
Age: 20
Grade: B+

Student added successfully!
```

*The output above is an example. Actual output depends on the program and user input.*

## 🚀 How to Run the Project

### Prerequisites

Install Python 3 on your computer.

### Steps

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd Collection-Manipulator
```

**3. Run the Python program**

```bash
python student_data_organizer.py
```

**4. Use the application**

Choose an option from the menu and follow the instructions displayed in the terminal.

## 📂 Project Structure

```text
Collection-Manipulator/
│
├── student_data_organizer.py
├── README.md
└── screenshots/
    ├── main_menu.png
    ├── add_student.png
    ├── display_students.png
    ├── update_student.png
    ├── subjects.png
    └── delete_student.png
```

## ⚙️ Assumptions and Limitations

- Every student must have a unique student ID.
- Age must be entered as an integer.
- Subjects are entered as comma-separated values.
- Student records are stored in memory during program execution.
- Records are not permanently saved in the basic implementation.
- Student ID and date of birth are treated as fixed information.

## 🔮 Future Enhancements

- Permanent storage using file handling.
- Database integration.
- Improved input validation and error handling.
- A graphical user interface.
- Student search and sorting functionality.

## ✅ Conclusion

The Student Data Organizer demonstrates the practical application of Python collection data types for managing student information.

The project improves understanding of data organization, collection manipulation, and basic programming logic through a simple, interactive application.

---

## 👩‍💻 Author

**Name:** JANVI TEJANI
**Course:** Computer Science and Engineering  
**Project:** Collection Manipulator – Student Data Organizer

---

⭐ *Thank you for visiting this project!*
