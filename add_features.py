def add_student(student_list):
    print("\n" + "=" * 40)
    print("             ADD STUDENT")
    print("=" * 40)

    name = input("Enter Student's Name: ").strip()
    student_number = input("Enter Student's Number: ").strip()

    if not name:
        print("\nError: Student name cannot be empty.")
        return

    if not student_number:
        print("\nError: Student number cannot be empty.")
        return

    # Check for duplicate Student Numbers
    for student in student_list:
        if student["Student Number"].lower() == student_number.lower():
            print(
                "\nError: A student with this "
                "Student Number already exists."
            )
            return

    student = {
        "Name": name,
        "Student Number": student_number
    }

    student_list.append(student)

    print("\nStudent added successfully!")
    print(f"Name          : {name}")
    print(f"Student Number : {student_number}")