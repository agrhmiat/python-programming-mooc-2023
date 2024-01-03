# Write your solution here

def double_items(numbers: list) -> list:
    des_lst = []
    for num in numbers:
        des_lst.append(num*2)
    return des_lst

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
