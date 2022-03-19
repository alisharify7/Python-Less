# github : alisharify
#implementation of Mario-Less problem set in python

user = 0
while(True):
    # in here we get input from user
    try:
        user = int(input("Enter height: "))
    except ValueError:
        continue
    
    # in here we check if user input is not between 1 to 8
    # with this while loop we ask again to user coprate with us
    if (user > 0 and user < 9):
        break

# if we dont + 1 to user and go from 1 to user it actually go to user - 1

for row in range(1, (user + 1)):
    # in first iterate we should print 4 space so we -1 to user
    user -= 1
    print(" " * user, end="")
    print("#" * row)

exit()
