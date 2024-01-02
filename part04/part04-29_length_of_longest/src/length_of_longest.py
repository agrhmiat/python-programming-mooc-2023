# Write your solution here

def length_of_longest(strings: list) -> int:
    max_length = len(strings[0])
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return max_length

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)
