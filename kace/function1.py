def greet(name):
    print("Hello ",  name)
    


greet("kwaku")


def addition(num1, num2):
    result = num1 + num2 
    print(result)

addition(-10,200)
# Return keyword
def addition2(num1, num2):
    result = num1 + num2 
    return result
    # return  num1 + num2 

print(addition2(8,8) + 5)

#Function with default values
def addition3(num1=2, num2=17):
    result = num1 + num2
    print(result)

addition3(10,20)
addition3()

# keyword arguments kwargs

python -m pip install numpy