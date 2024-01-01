# Write your solution here

string = input("Please type in a string: ")

vowels = "aeo"

i = 0
while i < len(vowels):
    vowel = vowels[i]
    if vowel in string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
    i += 1 
