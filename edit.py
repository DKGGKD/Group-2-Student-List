def edit_student(student_list):
    print("\n" + "=" * 40)
    print("              EDIT STUDENT")
    print("=" * 40)

    if not student_list:
        print("The student list is currently empty.")
        return

    search_number = input(
        "Enter Student Number of the student to edit: "
    ).strip()

    student_found = None

    for student in student_list:
        if student["Student Number"].lower() == search_number.lower():
            student_found = student
            break

    if student_found is None:
        print(
            f"\nNo student found with Student Number "
            f"'{search_number}'."
        )
        return

    print("\nStudent Found!")
    print(f"Current Name          : {student_found['Name']}")
    print(
        f"Current Student Number: "
        f"{student_found['Student Number']}"
    )

    print("\nLeave a field blank to keep its current value.")

    new_name = input(
        f"Enter new name [{student_found['Name']}]: "
    ).strip()

    new_number = input(
        f"Enter new Student Number "
        f"[{student_found['Student Number']}]: "
    ).strip()

    if new_name:
        student_found["Name"] = new_name

    if new_number:
        for student in student_list:
            if (
                student is not student_found
                and student["Student Number"].lower()
                == new_number.lower()
            ):
                print(
                    "\nError: Another student already uses "
                    "that Student Number."
                )
                return

        student_found["Student Number"] = new_number

    print("\nStudent updated successfully!")

    print("\nUpdated Information:")
    print(f"Name          : {student_found['Name']}")
    print(
        f"Student Number : "
        f"{student_found['Student Number']}"
    )