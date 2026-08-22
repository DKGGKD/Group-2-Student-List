def search_student(student_list):
    print("\n" + "=" * 40)
    print("             SEARCH STUDENT")
    print("=" * 40)

    if not student_list:
        print("The student list is currently empty.")
        return

    print("1. Search by Student Number")
    print("2. Search by Name")
    print("3. Cancel")

    choice = input("\nEnter option: ").strip()

    if choice == "3":
        print("\nSearch cancelled.")
        return

    # Search by Student Number
    if choice == "1":
        search_number = input(
            "\nEnter Student Number: "
        ).strip().lower()

        matches = [
            student
            for student in student_list
            if student["Student Number"].lower() == search_number
        ]

    # Search by Name
    elif choice == "2":
        search_name = input(
            "\nEnter Student Name: "
        ).strip().lower()

        matches = [
            student
            for student in student_list
            if search_name in student["Name"].lower()
        ]

    else:
        print("\nInvalid option.")
        return

    # No results
    if not matches:
        print("\nNo matching student found.")
        return

    # Display results
    print("\n" + "=" * 40)
    print(f"              SEARCH RESULTS")
    print("=" * 40)

    print(f"Found {len(matches)} student(s).\n")

    for index, student in enumerate(matches, start=1):
        print(f"Result #{index}")
        print(f"Name          : {student['Name']}")
        print(f"Student Number : {student['Student Number']}")
        print("-" * 40)