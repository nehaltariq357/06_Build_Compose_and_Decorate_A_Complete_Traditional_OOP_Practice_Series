# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student marks: {self.marks}")
        print() #empty line for spacing
#student 1
s1 = Student("Nehal",99)
s1.display()

#student 2 
s2 = Student("Ali",85)
s2.display()

