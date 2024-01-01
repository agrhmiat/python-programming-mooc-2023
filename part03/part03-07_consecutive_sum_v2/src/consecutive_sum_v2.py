# Write your solution here

limit = int(input("Limit: "))

i = 1
total = 0
my_sum = ""
while total < limit:
    total += i
    if total >= limit:
        my_sum += f"{i}"
    else:
        my_sum += f"{i} + "
    i += 1

print(f"The consecutive sum: {my_sum} = {total}")
