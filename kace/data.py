list1 = ["p", "r", "e", "s", "i", "d", "e", "n", "t"]
# slicing
print(list1[:4])
print(list1[2:-3])
print(list1[2:-2])
print(list1[-2:-2])
print(list1[-2:1])
print(list1[:-2])
print(list1[-2:])
print(list1[-4:])
print(list1[:-4])

# for element in list1:
    # element.index = e
    # print(element)

    # write a program to read 5 names and print in alphabetical order

    # use  sort and for loop to print the names

# print(list1.sort())

# names = ["kofi", "kwane", "ama", "akosua"]
user_names = []

for i in range(3):
    name = (input("Enter a name: "))
    user_names.append(name)

print(user_names)
# sorted_names = user_names.sort()
sorted_names = sorted(user_names)
print(sorted_names)
# for name in names:
#     ordered = print(name)
# ordered.sort()






# for i in range(len(names)):
#     print(i)
