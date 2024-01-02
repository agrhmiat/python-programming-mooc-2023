# Copy here code of line function from previous exercise

def line(integer, string):
    if string == "":
        char = "*"
    else:
        char = string[0]
    print(char * integer)

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
