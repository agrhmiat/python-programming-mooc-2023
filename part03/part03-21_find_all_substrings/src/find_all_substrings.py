# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

while True:
    if len(word) == 0:
        break
    i = word.find(char)
    if i == -1 or i+3 > len(word):
        break
    print(word[i:i+3])
    word = word[word.find(char, i+1):]
