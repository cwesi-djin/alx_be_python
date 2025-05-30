length = int(input("Enter the size of the pattern: "))
row = 0

while row < length:
    for column in range(length):
        print("*", end="")
    print()
    row += 1