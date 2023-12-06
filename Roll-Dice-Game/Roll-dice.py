import random
import sys

random.seed()

flag = 0
points = 0

def drop_dice():
    one = random.randrange(1,7)
    two = random.randrange(1,7)
    print(f"Player Got {one} and {two}")
    print(f"Sum is {one + two}")
    return (one,two)

def first_drop():
    flag = 1
    dice = drop_dice()
    one,two = dice
    if (one + two in [7,11]):
        print("Player Win in First Round!")
        sys.exit(0)
    elif(one+two in [12,3,2]):
        print("Player Lose! in First Round!")
        sys.exit(1)
    elif(one+two in [10,9,8,6,5,4]):
        points = one+two 
        print(f"POINTS is {points}")
        return True   



def main():
    if (flag == 0):
        first_drop()
    while True:
        a = drop_dice()
        one , two = a
        if (one + two == 7):
            print(f"Player Lose")
            sys.exit(1)
        elif (one + two == points):
            print("Player win! Points and Dice are same")
            sys.exit(0)


main()    
