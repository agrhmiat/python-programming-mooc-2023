# Write your solution here

def everything_reversed(strings: list) -> list:
    des_lst = []
    for string in strings[::-1]:
        des_lst.append(string[::-1])
    return des_lst

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
