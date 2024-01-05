# Write your solution here

text = input("Write text: ")
words = text.split(" ")

dictionary = []
with open("wordlist.txt") as dictionary_file:
    for line in dictionary_file:
        line = line.strip()
        dictionary.append(line)

sentence = ""
for word in words:
    if word.lower() in dictionary:
        sentence += word + " "
    else:
        sentence += "*" + word + "*" + " "

print(sentence)
