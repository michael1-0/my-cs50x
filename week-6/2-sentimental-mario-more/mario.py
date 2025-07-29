# TODO
while True:
    height = (input("Height: "))

    try:
        height = int(height)
        if height <= 0 or height >= 9:
            print("INVALID: enter a number 1-8")

        else:
            break

    except ValueError:
        print("INVALID: enter a number 1-8")
        print()

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end='')

    for j in range(i + 1):
        print("#", end='')

    print("  ", end='')

    for j in range(i + 1):
        print("#", end='')

    print()
