# CLASSES

class Employee:
    """Base class for employees."""

    count = 0

    def __init__(self, name, position, salary):  # Constructor
        self.name = name
        self.position = position
        self.salary = salary
        class_name = self.__class__.__name__
        Employee.count += 1
        print(f"{class_name} instance created (Constructor)")

    def __del__(self):  # Destructor
        class_name = self.__class__.__name__
        print(f"{class_name} destroyed (Destructor)")

    def displayInfo(self):
        print(f"\nEmployee: {self.name}\nPosition: {self.position}\nSalary: {self.salary}€\n")

    def displayCount(self):
        print(f"Total {self.__class__.__name__}s: {self.__class__.count}")


emp1 = Employee("John", "DevOps Administrator", 3700)
emp2 = Employee("Jack", "Full-Stack Developer", 2500)

emp1.displayInfo()
emp2.displayInfo()

emp2.displayCount()

# ----ATTRIBUTES (ADD,MODIFY,DELETE)

emp1.age = 21

print(getattr(emp1, 'age'))  # 21
setattr(emp1, 'age', 22); print(getattr(emp1, 'age'))  # 22
delattr(emp1, 'age')

# ----BUILT-IN CLASS ATTRIBUTES----

print(Employee.__dict__)  # holds namespace in a dictionary
"""{'__module__': '__main__', '__doc__': 'Base class for employees.', 
'employeeCount': 2, '__init__': <function Employee.__init__ at 0x00000199122D87C0>, 
'displayEmployeeInfo': <function Employee.displayEmployeeInfo at 0x00000199122D8860>, 
'displayCount': <function Employee.displayCount at 0x00000199122D8EA0>, 
'__dict__': <attribute '__dict__' of 'Employee' objects>, 
'__weakref__': <attribute '__weakref__' of 'Employee' objects>}"""

print(Employee.__doc__)  # Base class for employees. (documentation string or none if not defined)
print(Employee.__name__)  # Employee (name of class)
print(Employee.__module__)  # __main__ (name of module where class is defined, in interactive mode is __main__)
print(Employee.__bases__)  # (<class 'object'>,) (tuple for holding base classes that a class inherits)


class Programmer(Employee):
    """Class for programmer specific methods."""

    count = 0

    def __init__(self, name, position, salary, skills):
        super().__init__(name, position, salary)
        self.skills = skills
        class_name = self.__class__.__name__
        Programmer.count += 1
        print(f"{class_name} instance created (Constructor)")

    def __del__(self):
        class_name = self.__class__.__name__
        print(f"{class_name} destroyed (Destructor)")

    def showSkills(self):
        if type(self.skills == 'list'):
            print("Skills: ")
            for skill in self.skills:
                print(skill)
        else:
            print(self.skills)


programmer1 = Programmer('Jack', "Front-End Developer", 1900, ['JavaScript', 'React', 'Redux', 'Gatsby'])
programmer1.displayInfo()
programmer1.showSkills()
programmer1.displayCount()

print(issubclass(Programmer, Employee))  # True -> issubclass(sub, sup)
print(isinstance(programmer1, Programmer))  # True -> isinstance(obj, Class)

# ----FAST INHERITANCE----

class Road:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def roadInfo(self):
        print("-" * 30)
        print("Road definition")
        print(f"Name:\t {self.name}")
        print(f"Length:\t {self.length}m")


class Highway(Road):
    pass


class MainRoad(Road):
    pass


class LocalRoad(Road):
    pass


highway1 = Highway("A1", 2500)
mainroad1 = MainRoad("G75", 750)
localroad1 = LocalRoad("P12", 200)

highway1.roadInfo()
mainroad1.roadInfo()
localroad1.roadInfo()


