# Write your solution here

layers = int(input("Layers: "))

for i in range(64+layers, 64, -1):
    for j in range(64+layers, 64, -1):
        if j > i:
            print(chr(j), end="")
        else:
            print(chr(i), end="")
    for k in range(66, 64+layers+1):
        if k > i:
            print(chr(k), end="")
        else:
            print(chr(i), end="")
    print()

for i in range(66, 64+layers+1):
    for j in range(64+layers, 64, -1):
        if j > i:
            print(chr(j), end="")
        else:
            print(chr(i), end="")
    for k in range(66, 64+layers+1):
        if k > i:
            print(chr(k), end="")
        else:
            print(chr(i), end="")
    print()
