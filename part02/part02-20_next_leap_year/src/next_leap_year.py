# Write your solution here

year = int(input("Year: "))

leap_year = False
start_year = year + 1

while True:
    if start_year % 100 == 0:
        if start_year % 400 == 0:
            leap_year = True
    elif start_year % 4 == 0:
        leap_year = True
    if leap_year:
        break
    else:
        start_year += 1

print(f"The next leap year after {year} is {start_year}")
