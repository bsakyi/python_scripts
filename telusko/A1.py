class A:
    
    def __init__(self):
        print("A init")
    def feature1(self):
        print ("Feature 1 working")
        
    def feature2(self):
        print ("Feature 2 working")
        


# inheritance B inheriting from A
class B(A):
    def __init__(self):
        # calling the init of class A, the superclass
        super().__init__()
        print("B init")
    
    def feature1(self):
        print ("Feature 1b working")
        
    def feature2(self):
        print ("Feature 2b working")
        


a1 = A()
b1 = B()



a1.feature1()
a1.feature2()