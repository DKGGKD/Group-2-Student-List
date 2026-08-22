def edit_student(student_list):
    print("\n--- Edit Student ---")

    if not student_list:
        print("The student list is currently empty.")
        return student_list

    search_num = input("Enter Student Number to edit: ").strip()
    for student in student_list:
        if student["Student Number"] == search_num:
            print(f"Editing Student: {student['Name']} ({student['Student Number']})")
            new_name = input("Enter new name (leave blank to keep current): ").strip()
            new_num = input("Enter new number (leave blank to keep current): ").strip()

            if new_name:
                student["Name"] = new_name
            if new_num:
                student["Student Number"] = new_num

            print("Student updated successfully!")
            return student_list

    print(f"Error: No student found with Number {search_num}.")
    return student_list
