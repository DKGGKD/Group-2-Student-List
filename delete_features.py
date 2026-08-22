def delete_student(student_list):
    print("\n" + "=" * 40)
    print("            DELETE STUDENT")
    print("=" * 40)

    if not student_list:
        print("The student list is currently empty.")
        return

    print("1. Delete by Student Number")
    print("2. Delete by Name")
    print("3. Cancel")

    choice = input("\nEnter option: ").strip()

    if choice == "3":
        print("\nDeletion cancelled.")
        return

    if choice == "1":
        search_value = input(
            "Enter Student Number: "
        ).strip().lower()

        matches = [
            student
            for student in student_list
            if student["Student Number"].lower() == search_value
        ]

    elif choice == "2":
        search_value = input(
            "Enter Student Name: "
        ).strip().lower()

        matches = [
            student
            for student in student_list
            if student["Name"].lower() == search_value
        ]

    else:
        print("\nInvalid option.")
        return

    if not matches:
        print("\nNo matching student found.")
        return

    if len(matches) > 1:
        print("\nMultiple students found:")

        for index, student in enumerate(matches, start=1):
            print(
                f"{index}. "
                f"{student['Name']} - "
                f"{student['Student Number']}"
            )

        try:
            selection = int(
                input("\nSelect the student to delete: ")
            )

            if selection < 1 or selection > len(matches):
                print("\nInvalid selection.")
                return

            student_to_remove = matches[selection - 1]

        except ValueError:
            print("\nInvalid input.")
            return

    else:
        student_to_remove = matches[0]

    print("\nStudent selected:")
    print(f"Name          : {student_to_remove['Name']}")
    print(f"Student Number : {student_to_remove['Student Number']}")

    confirmation = input(
        "\nAre you sure you want to delete this student? (Y/N): "
    ).strip().lower()

    if confirmation == "y":
        student_list.remove(student_to_remove)
        print("\nStudent deleted successfully!")
    else:
        print("\nDeletion cancelled.")