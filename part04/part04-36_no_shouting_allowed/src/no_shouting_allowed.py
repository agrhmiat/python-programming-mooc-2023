# Write your solution here

def no_shouting(strings: list) -> list:
    des_lst = []
    for string in strings:
        if string.isupper():
            continue
        des_lst.append(string)
    return des_lst

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
