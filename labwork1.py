
def input_students(): #- call name for a funtion 
    students = []

    n = int(input("Enter number of students: ")) # input number of student

    for i in range(n):  # reapeat for every student
        print("\nStudent", i + 1)

        student_id = input("Enter student ID: ")# input number of Id
        name = input("Enter student name: ")    # name
        dob = input("Enter date of birth: ")    # date of birth

        student = {    # creat a students
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student) # add student to the list

    return students # return the list
def input_courses(): # call name  same as student

    courses = []

    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print("\nCourse", i + 1)
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)
    return courses
def input_marks(students, courses):

    marks = {} # creat a dictionary

    for course in courses: # go thought in course 

        print("\nEnter marks for course:", course["name"]) # display the course name

        marks[course["id"]] = {} # creat an emty dictionary for the course 

        for student in students: # go thought every student

            mark = float(input(
                "Enter mark for " + student["name"] + ": "
            ))
            marks[course["id"]][student["id"]] = mark
    return marks
def list_students(students):

    print("\n===== STUDENTS =====")

    for student in students:

        print(

            student["id"],

            "-",

            student["name"],

            "-",

            student["dob"]

        )

def list_courses(courses):

    print("\n===== COURSES =====")

    for course in courses:

        print(

            course["id"],

            "-",

            course["name"]

        )

def show_marks(students, courses, marks):

    course_id = input("\nEnter course ID: ")

    # Find the course

    course_name = ""

    for course in courses:

        if course["id"] == course_id:

            course_name = course["name"]

    if course_name == "":

        print("Course not found!")

        return

    print("\n===== MARKS =====")

    print("Course:", course_name)

    for student in students:

        student_id = student["id"]

        mark = marks[course_id][student_id]

        print(

            student_id,

            "-",

            student["name"],

            ":",

            mark

        )

---------- Main program ----------
students = input_students()

courses = input_courses()

marks = input_marks(students, courses)

list_students(students)

list_courses(courses)

show_marks(students, courses, marks)

