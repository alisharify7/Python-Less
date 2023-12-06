user = 0
while(True):
    try:
        user = int(input("Enter height: "))
    except ValueError:
        continue

    if (user > 0 and user < 9):
        break

for row in range(1, (user + 1)):
    user -= 1
    print(" " * user, end="")
    print("#" * row)

exit()
