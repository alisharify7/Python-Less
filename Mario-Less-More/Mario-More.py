print("Height Must between 1 to 8")

try:
    x = int(input("Enter Height: "))
except ValueError:
    print(f"-{x}- is Not a Number!")
    exit()

if (x <= 0 or x > 8):
    print(f"-{x}- is Out of Range!")
    exit()

for i in range(1 ,(x + 1)):
        x -= 1
        print(" " * x, end ="")
        print("#" * i, end ="")
        print(" ", end="")
        print("#" * i)
