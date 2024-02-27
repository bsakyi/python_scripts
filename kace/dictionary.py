# dictionary---key value pair

user_numbers = {
    "Akosua":"2354479", "Ben":"22457851", "carl":87966217
}

# print(user_numbers)

# print(user_numbers["Akosua"])

# print(user_numbers["Ben"] + 1)

# print(user_numbers["carl"] + 1)

user_numbers.update({"Ben":'123'})
print(user_numbers)
# delete item

# user_numbers.pop("carl")
# print(user_numbers)
# delete item using del 
# del user_numbers["carl"]
# del last item
# user_numbers.popitem()
# # delete all items 
# user_numbers.clear()
# print(user_numbers)

#looping through keys
# for key in user_numbers.keys():
    # print(key) 
# looping through values
# for values in user_numbers.values():
    # print(values) 
#looping through items
for items in user_numbers.items():
    print(items[1])

for items in user_numbers.items():
    print(f'=>{items}')

for key, value in user_numbers.items():
    print(key, "=>", value)