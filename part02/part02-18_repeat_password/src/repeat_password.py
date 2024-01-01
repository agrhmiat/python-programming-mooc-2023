# Write your solution here

passwd = input("Password: ")

while True:
    repasswd = input("Repeat password: ")
    if repasswd == passwd:
        break
    print("They do not match!")
print("User account created!")
