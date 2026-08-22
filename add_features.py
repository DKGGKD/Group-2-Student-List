students = []
def add_students():
    name = input("Enter Student's Name: ")
    stud_num = input("Enter Student's Number: ")

    student = {
        "Name" : name,
        "Student Number" : stud_num
    }

    students.append(student)
    print ("Student Added Successfully!")
