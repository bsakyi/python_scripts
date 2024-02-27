for value in range(1,6):
    print(value)

for value in range(1,101):
    print(value)

print("Stepping")
for value in range(1,101, 20):
    print(value)

for value in range(1,6):
    if value ==3:
        print("Inside loop")
        continue
print("Outside the loop")