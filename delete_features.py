def delete_student(students):
    if not students:
        print("The student list is empty.")
        return students

    option = input("1. By ID\n2. By Name\nOption: ").strip()

    if option == "1":
        mode = "Student Number"
    elif option == "2":
        mode = "Name"
    else:
        print("Invalid option selected. Returning to menu.")
        return students

    val = input(f"Enter {mode}: ").strip().lower()

    matches = [
        student for student in students
        if str(student.get(mode, "")).strip().lower() == val
    ]

    if not matches:
        print("No matching student found.")
        return students

    # If only one student matches, delete directly
    if len(matches) == 1:
        student_to_remove = matches[0]

    # If multiple students have the same name, ask for exact ID
    else:
        print(f"\nMultiple students found matching '{val}':")

        for student in matches:
            print(
                f"- ID: {student.get('Student Number', 'N/A')} | "
                f"Name: {student.get('Name', 'N/A')}"
            )

        confirm_id = input(
            "\nEnter the specific Student ID to delete: "
        ).strip()

        student_to_remove = None

        for student in matches:
            if str(student.get("Student Number", "")).strip() == confirm_id:
                student_to_remove = student
                break

        if student_to_remove is None:
            print("Error: Invalid ID selection. Deletion cancelled.")
            return students

    students.remove(student_to_remove)
    print("Student deleted successfully!")

    return students