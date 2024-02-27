# tuples are imutable, 

org = ("a", "b", "e", "c","b", "e")
print(org[0])
print(org[1])
print(org[:])
# count total number of elements
print(org.count("b"))

# index of elements
print(org.index("e"))

for element in org:
    print(element)