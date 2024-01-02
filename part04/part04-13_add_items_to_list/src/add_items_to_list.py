# Write your solution here

items = []

no_of_items = int(input("How many items: "))

i = 0
while i < no_of_items:
    item = int(input(f"Item {i+1}: "))
    items.append(item)
    i += 1

print(items)
