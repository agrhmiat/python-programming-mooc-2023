# Copy here code of line function from previous exercise

def line(integer, string):
    if string == "":
        char = "*"
    else:
        char = string[0]
    print(char * integer)

def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")
