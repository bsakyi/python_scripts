
class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def work(self):
        print(self.name + "is working")


class SoftwareEngineer(Employee):
    pass



class Designer(Employee):
    pass 


se = SoftwareEngineer("MAx", 25)
print(se.name, se.age)

d = Designer("philip", 24)

print(d.name, d.age)

print(d.work())