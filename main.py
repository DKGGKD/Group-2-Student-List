from add_features import add_students
from delete_features import delete_student
from edit import edit_student
from search import search_student


def display_students(student_list):
    print("\n" + "=" * 50)
    print("                 STUDENT LIST")
    print("=" * 50)

    if not student_list:
        print("The student list is currently empty.")
        print("=" * 50)
        return

    for index, student in enumerate(student_list, start=1):
        print(f"{index}. Name          : {student['Name']}")
        print(f"   Student Number : {student['Student Number']}")
        print("-" * 50)


def main():
    student_list = []

    while True:
        print("\n" + "=" * 50)
        print("              STUDENT LIST SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. Delete Student")
        print("3. Edit Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_students(student_list)

        elif choice == "2":
            delete_student(student_list)

        elif choice == "3":
            edit_student(student_list)

        elif choice == "4":
            search_student(student_list)

        elif choice == "5":
            display_students(student_list)

        elif choice == "6":
            print("\nThank you for using the Student List System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()