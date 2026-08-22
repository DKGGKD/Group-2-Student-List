def delete_student():
    if not students: return print("The student list is empty.")
    
    mode = "Student Number" if input("1. By ID\n2. By Name\nOption: ") == "1" else "Name"
    val = input(f"Enter {mode}: ").strip().lower()
    matches = [s for s in students if str(s[mode]).lower() == val]
    
    if not matches: return print("No matching student found.")
    
    to_remove = matches[0] if len(matches) == 1 else next((s for s in matches if str(s["Student Number"]).lower() == input("Multiple found. Enter exact ID: ").strip().lower()), None)
    
    if to_remove:
        students.remove(to_remove)
        print("Student deleted successfully!")
    else:
        print("Invalid selection. Cancelled.")
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
