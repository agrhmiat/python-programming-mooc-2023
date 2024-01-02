# Write your solution here

def most_common_character(string: str) -> str:
    char = string[0]
    for letter in string:
        if string.count(letter) > string.count(char):
            char = letter
    return char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
