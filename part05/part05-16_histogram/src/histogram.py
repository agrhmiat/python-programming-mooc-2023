# Write your solution here

def histogram(string: str) -> None:
    letters = {}
    for char in string:
        if char not in letters:
            letters[char] = string.count(char)
    for letter, stars in letters.items():
        print(f"{letter} {"*" * stars}")

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")
