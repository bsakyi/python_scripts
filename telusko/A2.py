class A:
    
    def __init__(self):
        print("A init")
    def feature1(self):
        print ("Feature 1a working")
        
    def feature2(self):
        print ("Feature 2 working")
        


# inheritance B inheriting from A
class B:
    def __init__(self):
        print("B init")
    
    def feature1(self):
        print ("Feature 1b working")
        
    def feature2(self):
        print ("Feature 2b working")
        
class C(A,B):
    
    def __init__(self):
        super().__init__()
        print("in C init")
        
        
# Method Resolution order MRO
# a1 = A()
# b1 = B()
c1 = C()


# a1.feature1()
# a1.feature2()