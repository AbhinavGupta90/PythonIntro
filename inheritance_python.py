class Person:

    def __init__ (self, name):
        self.name = name

    def __repr__(self):
        return repr((self.name))

class Student(Person):

    def __init__(self, name, college, year):
        self.college = college
        self.year = year
        super().__init__(name)

    def __repr__(self):
        return repr((self.name, self.college, self.year))


person1 = Person("Thomas")
student1 = Student("Thomas", "Yale", 3)

print(type(person1))
print(type(student1))
print(person1.__repr__())
print(student1.__repr__())
