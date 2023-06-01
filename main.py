class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f'name: {self.name}, age: {self.age}')
Student = Student(name = "John", age = 22)
Student.get_info()