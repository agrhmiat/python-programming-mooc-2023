# Write your solution here

num = int(input("Please type in a number: "))

i = 1
while i < num:
    print(i+1)
    print(i)
    i += 2
if num % 2 != 0:
    print(num)
