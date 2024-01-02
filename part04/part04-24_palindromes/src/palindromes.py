# Write your solution here

def palindromes(word: str) -> bool:
    if len(word) == 1:
        return True
    i = 0
    while i < len(word)//2:
        if word[i] != word[len(word)-i-1]:
            return False
        i += 1
    return True

def main() -> None:
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            break
        print("that wasn't a palindrome")
    print(f"{word} is a palindrome!")

main()

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
