class Student:
    counter = 0

    def __init__(self, name, surname, index, average_mark):
        self.name = name
        self.surname = surname
        self.index = index
        self.average_mark = average_mark

    def __str__(self):
        return f"Name: {self.name}, surname: {self.surname}, index: {self.index}, average mark: {self.average_mark}"

    def __lt__(self, other):
        return self.name < other.name

    @staticmethod
    def student_count():
        return Student.counter
