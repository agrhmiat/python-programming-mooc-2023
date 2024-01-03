# Write your solution here

def search(people: dict) -> None:
    name = input("name: ")
    if name not in people:
        print("no number")
    else:
        print(f"{people[name]}")

def add(people: dict) -> None:
    name = input("name: ")
    number = input("number: ")
    people[name] = number
    print("ok!")

def main() -> None:
    people = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            break
        elif command == 2:
            add(people)
        elif command == 1:
            search(people)
    print("quitting...")

main()
