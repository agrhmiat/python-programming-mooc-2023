# Write your solution here

def line(integer, string):
    if string == "":
        char = "*"
    else:
        char = string[0]
    print(char * integer)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "") 
