# 2.student.mark.oop.py

class Student:
    def __init__(self, student_id="", name="", dob=""):
        # Private attributes (Encapsulation)
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    # Polymorphic input method
    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter date of birth: ")

    # Polymorphic list method
    def list(self):
        print(f"{self.__id} - {self.__name} - {self.__dob}")


class Course:
    def __init__(self, course_id="", name=""):
        # Private attributes (Encapsulation)
        self.__id = course_id
        self.__name = name

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    # Polymorphic input method
    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    # Polymorphic list method
    def list(self):
        print(f"{self.__id} - {self.__name}")


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # Structure: {course_id: {student_id: mark}}

    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"\nStudent {i + 1}")
            student = Student()
            student.input()  # Polymorphic call
            self.__students.append(student)

    def input_courses(self):
        n = int(input("\nEnter number of courses: "))
        for i in range(n):
            print(f"\nCourse {i + 1}")
            course = Course()
            course.input()  # Polymorphic call
            self.__courses.append(course)

    def input_marks(self):
        for course in self.__courses:
            print(f"\nEnter marks for course: {course.get_name()}")
            self.__marks[course.get_id()] = {}
            for student in self.__students:
                mark = float(input(f"Enter mark for {student.get_name()}: "))
                self.__marks[course.get_id()][student.get_id()] = mark

    def list_students(self):
        print("\n===== STUDENTS =====")
        for student in self.__students:
            student.list()  # Polymorphic call

    def list_courses(self):
        print("\n===== COURSES =====")
        for course in self.__courses:
            course.list()  # Polymorphic call

    def show_marks(self):
        course_id = input("\nEnter course ID: ")
        target_course = None
        for course in self.__courses:
            if course.get_id() == course_id:
                target_course = course
                break

        if not target_course:
            print("Course not found!")
            return

        print("\n===== MARKS =====")
        print(f"Course: {target_course.get_name()}")
        for student in self.__students:
            sid = student.get_id()
            mark = self.__marks.get(course_id, {}).get(sid, "N/A")
            print(f"{sid} - {student.get_name()}: {mark}")


# Main Program
if __name__ == "__main__":
    manager = StudentMarkManagement()
    manager.input_students()
    manager.input_courses()
    manager.input_marks()

    manager.list_students()
    manager.list_courses()
    manager.show_marks()