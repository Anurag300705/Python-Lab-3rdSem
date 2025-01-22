# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived class
class Student(Person):
    def __init__(self, name, age, student_id):
        # Calling the constructor of the base class
        super().__init__(name, age)
        self.student_id = student_id

    # Method to display student details
    def display_student(self):
        self.display_person()  # Call method from Person class
        print(f"Student ID: {self.student_id}")

# Example usage
student = Student("Alice", 20, "S123456")
student.display_student()
