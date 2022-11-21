import abc
from abc import ABC


@abc.abstractmethod
class Student(ABC):
    __metaclass__ = abc.ABCMeta
    id_counter = 0o00001

    # Abstract class that represents general students
    def __init__(self, name: str, email: str):
        # Initialize values of student
        self._name = name
        # Validate email
        if email.islower() and email.endswith('@ucdenver.edu'):
            self._email = email
        else:
            print("Incorrect Email Format")
            self._email = ""
        self._id = Student.id_counter
        # Checking for first id
        Student.id_counter += 1
        self._enrolled_to = []

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    # Get the standing of the student
    def get_standing(self):
        pass

    @property
    def enroll_to(self):
        return [self._enrolled_to]

    # Enroll to course from Course class
    @enroll_to.setter
    def enroll_to(self, course):
        self._enrolled_to.append(course)

    @staticmethod
    def reset_id_numbering():
        Student.id_counter = 0o00001
        # self._id = 0o00001

    def __str__(self):
        # Return string for Student
        return f'{self.name:<{20}} -   {self.id:06}   - {self._email:50} - Standing: {self.get_standing()}'


class UnderGrad(Student):
    _gpa: float
    _standing: str

    def __init__(self, name: str, email: str, gpa: float):
        super().__init__(name, email)

        if gpa < 0 or gpa > 4:
            raise ValueError('Invalid gpa')
        else:
            self._gpa = gpa
        self._standing = "Undergraduate"

    def get_standing(self):
        self._standing = "Undergraduate"
        return self._standing

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, gpa):
        if self._gpa not in range(1, 4):
            raise ValueError('Invalid gpa')
        else:
            self._gpa = gpa


class Graduate(Student):
    current_level: str

    def __init__(self, name: str, email: str, current_level: str):
        super().__init__(name, email)
        self.current_level = current_level

    def get_standing(self):
        if self.current_level != "master" and self.current_level != "phd":
            raise ValueError('Invalid level')
        elif self.current_level == "master":
            return "Master"
        elif self.current_level == "phd":
            return "PhD"

