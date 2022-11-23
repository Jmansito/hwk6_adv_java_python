from re import search
from course import Course
from student import UnderGrad, Graduate


class University:

    def __init__(self, name: str):
        self._name = name
        self.students = []
        self.courses = []

    # Create undergrad student object
    def add_undergrad(self, name, email, gpa):
        self.students.append(UnderGrad(name, email, gpa))

    # Create graduate student object
    def add_graduate(self, name, email, level):
        self.students.append(Graduate(name, email, level))

    def add_course(self, *args):
        try:
            self.courses.append(Course(*args))
        except ValueError:
            print("There is already a course with those fields.")

    def remove_student(self, name):
        students_removed = []
        for student in self.students:
            if student.name == name:
                students_removed.append(student)
                self.students.remove(student)
        return [students_removed]

    def get_students(self, name="", id=0, email=""):
        students_found = []
        for student in self.students:
            if search(name, student.name) or student.id == id or search(email, student.email):
                students_found.append(student)
        return [students_found]

    def get_courses(self, subject="", number=0, title=""):
        courses_found = []
        for course in self.courses:
            if search(subject, course.subject) or course.number == number or search(title, course.title):
                courses_found.append(course)
        return [courses_found]

    def enroll_student(self, id, subject, number):
        for student in self.students:
            if id == student.id:
                for course in student.enrolled_to:
                    if subject == course.subject or number == course.number:
                        print("Student is already enrolled in course")
                        break
                    else:
                        student.enroll_to(subject, number)

    def enrollment_report(self):
        return "Dictionary return placeholder"
