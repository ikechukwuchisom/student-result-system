from student import Student
from storage import load_students, save_students
from results import enter_scores
from reports import student_report, class_report, save_text_report


def find_student(students, search_value):
    value = search_value.strip().lower()
    for student in students:
        if student.student_id.lower() == value or value in student.full_name.lower():
            return student
    return None


def add_student(students):
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if find_student(students, student_id):
        print("A student with that ID already exists.")
        return

    full_name = input("Full name: ").strip()
    class_form = input("Class/Form: ").strip()
    gender = input("Gender: ").strip()
    date_of_birth = input("Date of birth (YYYY-MM-DD): ").strip()

    if not all([full_name, class_form, gender, date_of_birth]):
        print("All student details are required.")
        return

    student = Student(student_id, full_name, class_form, gender, date_of_birth)
    students.append(student)
    save_students(students)
    print("Student registered successfully.")


def view_students(students):
    if not students:
        print("No students registered yet.")
        return
    print("\nREGISTERED STUDENTS")
    for student in students:
        print(f"{student.student_id} | {student.full_name} | "
              f"{student.class_form} | Average: {student.average_score():.2f}%")


def search_student(students):
    student = find_student(students, input("Enter student ID or name: "))
    if student:
        print(student_report(student))
    else:
        print("Student not found.")


def update_student(students):
    student = find_student(students, input("Enter the student's ID: "))
    if not student:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    new_name = input(f"Full name [{student.full_name}]: ").strip()
    new_class = input(f"Class/Form [{student.class_form}]: ").strip()
    new_gender = input(f"Gender [{student.gender}]: ").strip()
    new_dob = input(f"Date of birth [{student.date_of_birth}]: ").strip()
    student.full_name = new_name or student.full_name
    student.class_form = new_class or student.class_form
    student.gender = new_gender or student.gender
    student.date_of_birth = new_dob or student.date_of_birth
    save_students(students)
    print("Student information updated.")


def delete_student(students):
    student = find_student(students, input("Enter the student's ID: "))
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student.full_name}? (y/n): ").lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")


def record_or_update_scores(students):
    student = find_student(students, input("Enter the student's ID: "))
    if not student:
        print("Student not found.")
        return
    enter_scores(student)
    save_students(students)


def show_class_report(students):
    content = class_report(students)
    print(content)
    answer = input("\nSave this report to class_report.txt? (y/n): ").lower()
    if answer == "y":
        filename = save_text_report(content)
        print(f"Report saved as {filename}.")


def sort_students(students):
    if not students:
        print("No students to sort.")
        return
    choice = input("Sort by (1) average, highest first or (2) name? ")
    if choice == "1":
        ordered = sorted(students, key=lambda item: item.average_score(), reverse=True)
    elif choice == "2":
        ordered = sorted(students, key=lambda item: item.full_name.lower())
    else:
        print("Invalid sorting choice.")
        return
    for student in ordered:
        print(f"{student.full_name} | {student.average_score():.2f}% | {student.grade()}")


def main():
    students = load_students()
    actions = {
        "1": lambda: add_student(students),
        "2": lambda: view_students(students),
        "3": lambda: search_student(students),
        "4": lambda: update_student(students),
        "5": lambda: delete_student(students),
        "6": lambda: record_or_update_scores(students),
        "7": lambda: show_class_report(students),
        "8": lambda: sort_students(students),
    }

    while True:
        print("\n" + "=" * 48)
        print("       STUDENT RESULT MANAGEMENT SYSTEM")
        print("=" * 48)
        print("1. Register a student")
        print("2. View all students")
        print("3. Search and view report card")
        print("4. Update student information")
        print("5. Delete a student")
        print("6. Enter or update subject scores")
        print("7. Class report and statistics")
        print("8. Sort students")
        print("9. Save and exit")

        choice = input("Choose an option (1-9): ").strip()
        if choice == "9":
            save_students(students)
            print("All records saved. Goodbye.")
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except (OSError, ValueError) as error:
                print(f"An error occurred: {error}")
            finally:
                save_students(students)
        else:
            print("Invalid option. Choose a number from 1 to 9.")


if __name__ == "__main__":
    main()
