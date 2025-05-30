# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Hamza","500","123-456-789")

print("Public:", emp.name) # hamza
print("protected:", emp._salary) # 500 # works, but by convention shouldn't be accessed directly 

try:
    print("Private:", emp.__ssn) # error(attribute error)
except AttributeError:
    print("private: cannot accessed directly")

print("private with name mangling:",emp._Employee__ssn) # works but recommended
