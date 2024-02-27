
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age 
        self.salary = salary
        
    def work(self):
        print(self.name + "is working")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
        



class Designer(Employee):
    pass 


se = SoftwareEngineer("MAx", 25)
print(se.name, se.age)

d = Designer("philip", 24)

print(d.name, d.age)

print(d.work())