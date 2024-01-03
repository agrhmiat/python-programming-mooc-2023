# Write your solution here

def dict_of_numbers() -> dict:
    numbers = {}
    ones = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    teens = ["eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    for i in range(0, 100):
        if i != 0 and i % 10 == 0:
            numbers[i] = tens[i//10-1]
        elif i >= 0 and i < 10:
            numbers[i] = ones[i]
        elif i >= 11 and i <= 19:
            numbers[i] = teens[i-10-1]
        else:
            numbers[i] = tens[i//10-1] + "-" + ones[i%10]
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
