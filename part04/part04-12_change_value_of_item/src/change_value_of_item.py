# Write your solution here

values = [1, 2, 3, 4, 5]

while True:
    i = int(input("Index: "))
    if i == -1:
        break
    val = int(input("New value: "))
    values[i] = val
    print(values)
