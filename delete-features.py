def delete_student(student_list):
    print("\n--- Delete Student ---")

    if not student_list:
        print("The student list is currently empty.")
        return student_list

    print("1. Delete by Student ID")
    print("2. Delete by Name")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        search_id = input("Enter Student ID to delete: ").strip()
        student_to_remove = None

        for student in student_list:
            if student["id"] == search_id:
                student_to_remove = student
                break

        if student_to_remove:
            student_list.remove(student_to_remove)
            print(f"Success: Student with ID {search_id} has been deleted.")
        else:
            print(f"Error: No student found with ID {search_id}.")

    elif choice == "2":
        search_name = input("Enter Student Name to delete: ").strip().lower()
        matches = [s for s in student_list if s["name"].lower() == search_name]

        if not matches:
            print(f"Error: No student found with the name '{search_name}'.")
        elif len(matches) == 1:
            student_list.remove(matches[0])
            print(f"Success: Student '{matches[0]['name']}' has been deleted.")
        else:
            print(f"\nMultiple students found matching '{search_name}':")
            for student in matches:
                print(f"- ID: {student['id']} | Name: {student['name']}")

            confirm_id = input("\nEnter the specific Student ID to delete: ").strip()
            student_to_remove = None

            for student in matches:
                if student["id"] == confirm_id:
                    student_to_remove = student
                    break

            if student_to_remove:
                student_list.remove(student_to_remove)
                print(f"Success: Student with ID {confirm_id} has been deleted.")
            else:
                print("Error: Invalid ID selection. Deletion cancelled.")
    else:
        print("Invalid option selected. Returning to menu.")

    return student_list