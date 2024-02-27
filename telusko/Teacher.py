class Teacher:
    
    def __init__(self, name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.rollno)
   
#    inner class
    class Laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i3'
            self.ram = 8
        
t1 = Teacher('Ben', 22)
t2 = Teacher('Asare', 44)

t1.show()

lap1 = t1.lap.brand
print(lap1)