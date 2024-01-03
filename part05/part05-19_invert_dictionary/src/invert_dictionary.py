# Write your solution here

def invert(dictionary: dict) -> None:
    my_dict = dictionary.copy()
    dictionary.clear()
    for key, value in my_dict.items():
        dictionary[value] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)    
