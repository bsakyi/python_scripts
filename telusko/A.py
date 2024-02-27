class A:
    def feature1(self):
        print ("Feature 1 working")
        
    def feature2(self):
        print ("Feature 2 working")
        
class Z:
    def feature1(self):
        print ("Feature Z working")

# inheritance B inheriting from A
class B(A)
    def feature1(self):
        print ("Feature 1b working")
        
    def feature2(self):
        print ("Feature 2b working")
        
# multilevel inheritance
class C(B):
     def feature2(self):
        print ("Feature 2C working")
        
# Multiple inheritance
class D(C,A):
    def feature4(self):
        print("Feature 4 working")

a1 = A()
b1 = B()
d1 = D()


a1.feature1()
a1.feature2()