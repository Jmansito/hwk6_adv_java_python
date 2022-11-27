from re import search
from course import Course
from student import UnderGrad, Graduate


class University:

    def __init__(self, name: str):
        self._name = name
        self._students = []
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def students(self):
        return self._students

    @property
    def courses(self):
        return self._courses

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

    def get_students(self, name="", _id=0, email=""):
        students_found = []
        for student in self.students:
            if search(name, student.name) or student.id == _id or search(email, student.email):
                students_found.append(student)
        return [students_found]

    def get_courses(self, subject="", number=0, title=""):
        courses_found = []
        if subject == "" and number == 0 and title == "":
            for course in self.courses:
                courses_found.append(course)
            return [courses_found]
        else:
            for course in self.courses:
                if search(subject, course.subject) or course.number == number or search(title, course.title):
                    courses_found.append(course)
            return [courses_found]

    def enroll_student(self, _id, subject, number):
        for student in self.students:
            if _id == student.id:
                for course in student.enrolled_to:
                    if subject == course.subject or number == course.number:
                        print("Student is already enrolled in course")
                        break
                    else:
                        student.enroll_to(subject, number)

    def enrollment_report(self):
        return "Dictionary return placeholder"

    def __str__(self):
        # Return string for University
        return f'{self.name} University with {len(self.get_students())} students and {len(self.get_courses())} courses.'
