class Item():
    pay_rate = 0.8 # The rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} must be greater than zero"
        assert quantity >=0, f"Quantity {quantity} must be greater than or equal to zero"
        
        self.name = name 
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, 6)
item2.has_numpad = False
item2.price = 1000
item2.quantity = 3


print(item1.calculate_total_price())
print(item1.pay_rate)
print(Item.__dict__)
print(item1.__dict__)