# Write your solution here

def list_of_stars(my_list: list) -> None:
    for num in my_list:
        print("*" * num)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
