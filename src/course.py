class Course:
    def __init__(self, subject, number, title):
        self._subject = subject
        self._number = number
        self._title = title

    @property
    def subject(self):
        return self._subject

    @property
    def number(self):
        return self._number

    @property
    def title(self):
        return self._title

    def __str__(self):
        return f'{self._subject}:{self._number}'
