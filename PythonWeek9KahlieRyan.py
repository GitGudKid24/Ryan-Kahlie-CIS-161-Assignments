class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def nag(self):
        return f"Name: {self.name} Age: {self.age} Grade: {self.grade}"

student1 = Students('Ryan', 24, 18)
student2 = Students('Dude', 69, 420)

print(student1.nag())
print(student2.nag())

class Staff:
    def __init__(self, name, role, department, salary=None):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, age, role, department):
        super().__init__(name, role, department)
        self.age = age

    def teach_info(self):
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Department: {self.department}"

Teacher1 = Teacher('James', 40, 'Professor', 'CIS')
Teacher2 = Teacher('Jenna', 26, 'Professor', 'Math')

print(Teacher1.teach_info())
print(Teacher2.teach_info())


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

side_input = int(input("Enter the side length of a square: "))
my_square = Square(side_input)

print(f"The area is {my_square.area()} and the perimeter is {my_square.perimeter()}")


