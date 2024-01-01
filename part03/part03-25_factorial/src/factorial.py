# Write your solution here

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break
    i = num
    fact = 1
    while i > 0:
        fact *= i
        i -= 1
    print(f"The factorial of the number {num} is {fact}")
print("Thanks and bye!")
