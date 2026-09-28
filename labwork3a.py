# 3.student.mark.oop.math.py
import math
import numpy as np
import curses


class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa


class Course:
    def __init__(self, course_id="", name="", credits=0):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits


class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = {}  

    def get_students(self):
        return self._students

    def get_courses(self):
        return self._courses

    def get_marks(self):
        return self._marks

    def add_student(self, student):
        self._students.append(student)

    def add_course(self, course):
        self._courses.append(course)

    def set_mark(self, course_id, student_id, mark):
        if course_id not in self._marks:
            self._marks[course_id] = {}
        # Làm tròn xuống 1 chữ số thập phân bằng math.floor()
        rounded_mark = math.floor(mark * 10) / 10.0
        self._marks[course_id][student_id] = rounded_mark

    def calculate_gpa(self, student_id):
        student_marks = []
        course_credits = []

        for course in self._courses:
            cid = course.get_id()
            if cid in self._marks and student_id in self._marks[cid]:
                student_marks.append(self._marks[cid][student_id])
                course_credits.append(course.get_credits())

        if not student_marks:
            return 0.0

        # Sử dụng mảng numpy để tính trung bình tích lũy theo trọng số
        marks_arr = np.array(student_marks)
        credits_arr = np.array(course_credits)

        weighted_sum = np.sum(marks_arr * credits_arr)
        total_credits = np.sum(credits_arr)

        if total_credits == 0:
            return 0.0

        gpa = weighted_sum / total_credits
        return math.floor(gpa * 100) / 100.0

    def update_all_gpas(self):
        for student in self._students:
            gpa = self.calculate_gpa(student.get_id())
            student.set_gpa(gpa)

    def sort_students_by_gpa(self):
        self.update_all_gpas()
        self.i_sort_descending()

    def i_sort_descending(self):
        self._students.sort(key=lambda s: s.get_gpa(), reverse=True)


# --- HÀM HỖ TRỢ CURSES UI ---

def get_input_str(stdscr, prompt, y, x=0):
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()
    curses.echo()
    input_bytes = stdscr.getstr(y, x + len(prompt))
    curses.noecho()
    return input_bytes.decode('utf-8').strip()


def input_students_ui(stdscr, manager):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== NHẬP DANH SÁCH SINH VIÊN ===")
    n = int(get_input_str(stdscr, "Nhập số lượng sinh viên: ", 2))
    row = 4
    for i in range(n):
        stdscr.addstr(row, 0, f"--- Sinh viên {i + 1} ---")
        row += 1
        sid = get_input_str(stdscr, "ID sinh viên: ", row)
        row += 1
        name = get_input_str(stdscr, "Tên sinh viên: ", row)
        row += 1
        dob = get_input_str(stdscr, "Ngày sinh: ", row)
        row += 2
        manager.add_student(Student(sid, name, dob))
    stdscr.addstr(row, 0, "Đã lưu sinh viên! Nhấn phím bất kỳ...")
    stdscr.getch()


def input_courses_ui(stdscr, manager):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== NHẬP DANH SÁCH MÔN HỌC ===")
    n = int(get_input_str(stdscr, "Nhập số lượng môn học: ", 2))
    row = 4
    for i in range(n):
        stdscr.addstr(row, 0, f"--- Môn học {i + 1} ---")
        row += 1
        cid = get_input_str(stdscr, "Mã môn học: ", row)
        row += 1
        name = get_input_str(stdscr, "Tên môn học: ", row)
        row += 1
        credits = int(get_input_str(stdscr, "Số tín chỉ: ", row))
        row += 2
        manager.add_course(Course(cid, name, credits))
    stdscr.addstr(row, 0, "Đã lưu môn học! Nhấn phím bất kỳ...")
    stdscr.getch()


def input_marks_ui(stdscr, manager):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== NHẬP ĐIỂM SỐ ===")
    if not manager.get_courses() or not manager.get_students():
        stdscr.addstr(2, 0, "Cần nhập sinh viên và môn học trước! Nhấn phím bất kỳ...")
        stdscr.getch()
        return

    row = 2
    for course in manager.get_courses():
        stdscr.addstr(row, 0, f"Môn học: {course.get_name()} ({course.get_id()})")
        row += 1
        for student in manager.get_students():
            raw_mark = float(get_input_str(stdscr, f" Điểm cho {student.get_name()}: ", row))
            manager.set_mark(course.get_id(), student.get_id(), raw_mark)
            row += 1
        row += 1

    stdscr.addstr(row, 0, "Đã lưu điểm! Nhấn phím bất kỳ...")
    stdscr.getch()


def show_students_ui(stdscr, manager):
    stdscr.clear()
    manager.sort_students_by_gpa()
    stdscr.addstr(0, 0, "=== DANH SÁCH SINH VIÊN (SẮP XẾP THEO GPA GIẢM DẦN) ===")
    row = 2
    stdscr.addstr(row, 0, f"{'ID':<10} | {'Tên':<20} | {'Ngày sinh':<12} | {'GPA':<6}")
    stdscr.addstr(row + 1, 0, "-" * 55)
    row += 2

    for student in manager.get_students():
        stdscr.addstr(row, 0, f"{student.get_id():<10} | {student.get_name():<20} | {student.get_dob():<12} | {student.get_gpa():<6.2f}")
        row += 1

    stdscr.addstr(row + 2, 0, "Nhấn phím bất kỳ để quay lại...")
    stdscr.getch()


def main_curses(stdscr):
    manager = StudentMarkManagement()
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "================ QUẢN LÝ ĐIỂM SINH VIÊN ================")
        stdscr.addstr(2, 0, "1. Nhập danh sách sinh viên")
        stdscr.addstr(3, 0, "2. Nhập danh sách môn học")
        stdscr.addstr(4, 0, "3. Nhập điểm số")
        stdscr.addstr(5, 0, "4. Xem danh sách sinh viên & GPA (Đã sắp xếp)")
        stdscr.addstr(6, 0, "0. Thoát")
        stdscr.addstr(8, 0, "Lựa chọn của bạn: ")
        stdscr.refresh()

        choice = stdscr.getkey()
        if choice == '1':
            input_students_ui(stdscr, manager)
        elif choice == '2':
            input_courses_ui(stdscr, manager)
        elif choice == '3':
            input_marks_ui(stdscr, manager)
        elif choice == '4':
            show_students_ui(stdscr, manager)
        elif choice == '0':
            break


if __name__ == "__main__":
    curses.wrapper(main_curses)