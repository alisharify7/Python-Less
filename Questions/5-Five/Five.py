import sys

def is_even(number):
    if (number % 2 == 0):
        return True
    return False    



n = int(input("Enter numbr: "))
if (n < 0):
    print("Number must be positive :(")
    sys.exit(1)

while (True):
    print(f"Number is {n}")
    if (n == 1):
        print(f"End number is {n}")
        sys.exit(0)

    if (is_even(n)):
        n //= 2
        continue

    n *= 3
    n += 1     



