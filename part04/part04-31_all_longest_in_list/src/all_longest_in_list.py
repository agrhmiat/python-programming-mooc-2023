# Write your solution here

def all_the_longest(strings: list) -> list:
    all_longest = []
    longest_len = len(strings[0])
    for string in strings:
        if len(string) > longest_len:
            longest_len = len(string)
    for string in strings:
        if len(string) == longest_len:
            all_longest.append(string)
    return all_longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
