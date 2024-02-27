# inheritance
# polymorphism
# Encapsulation
# Abstraction

se1  = ["Software Engineer", "Max", 20, "Junior", 50000]
se12 = ["SOftware Engineer", "Max", 20, "Senior", 7000]

class SoftwareEngineer:
    
    alias = "Keyboard Magician"
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary 
        
    def code(self):
        print(f"{self.name} is writing code..")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")
        
    def __str__(self):
        information = f"na
        me = {self.name} , age={self.age}, level = {self.level}"
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def entry_salary(age):
        if age<25:
            return 5000    
        if age < 20:
            return 7000
        return 9000

se1 = SoftwareEngineer("Max", 20, "Junior", 50000)
print(se1.name)
print(se1.code())
print(se1.code_in_language("PHP"))
print(se1)