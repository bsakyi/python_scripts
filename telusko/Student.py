class Student:
    # class variable
    school = 'Bensco'
    
    def __init__(self,m1,m2,m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3= m3 
    # instance methods
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    # class method
    @classmethod    
    def getSchool(cls):
        return cls.school
    
    # static method
    @staticmethod
    def info():
        print("This is Student Class...")
        
s1 = Student(34,67,85)
s2 = Student(65,85,97)

print(s1.avg())
print(s2.avg())
print(Student.info())
print(2+2)