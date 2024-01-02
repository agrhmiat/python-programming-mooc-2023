# Write your solution here

def shortest(strings: list) -> str:
    shortest_str = strings[0]
    for string in strings:
        if len(string) < len(shortest_str):
            shortest_str = string
    return shortest_str

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)
