# write your solution here

def largest() -> int:
    numbers = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            numbers.append(int(line))
    largest_number = numbers[0]
    for num in numbers:
        if num > largest_number:
            largest_number = num
    return largest_number

if __name__ == "__main__":
    print(largest())
