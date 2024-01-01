# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

second_occurrence = False

i1 = string.find(substring)
if i1 != -1:
    i2 = string.find(substring, i1+len(substring))
    if i2 != -1:
        second_occurrence = True

if second_occurrence:
    print(f"The second occurrence of the substring is at index {i2}.")
else:
    print("The substring does not occur twice in the string.")
