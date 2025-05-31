
# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


class Department:
    def __init__(self,dept,emp):
        self.dept = dept
        self.emp = emp

class Employee:
    def __init__(self,name):
        self.name = name
        
        
emp1 = Employee("Ali")
dept1 = Department("IT",emp1)
print("Employee:", dept1.emp.name)
print("Department:",dept1.dept)