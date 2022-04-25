import random
import sys

random.seed()

flag = 0
points = 0

# this function just Rrtuen Two random number in a tuple between 1 to 6
def drop_dice():
    one = random.randrange(1,7)
    two = random.randrange(1,7)
    print(f"Player Got {one} and {two}")
    print(f"Sum is {one + two}")
    return (one,two)

# this function drop Dice for first time 
def first_drop():
    flag = 1
    dice = drop_dice()
    # unpack tuple
    one,two = dice
    # if sum of Dice is 7 or 11 Player win
    if (one + two in [7,11]):
        print("Player Win in First Round!")
        sys.exit(0)
    # else if sum of dice is 12 or 3 or 2  player lose 
    elif(one+two in [12,3,2]):
        print("Player Lose! in First Round!")
        sys.exit(1)
    # else sum of dice is in [10,9,8,6,5,4] we set sum of dice to player point
    elif(one+two in [10,9,8,6,5,4]):
        points = one+two 
        print(f"POINTS is {points}")
        return True   



def main():
    # First round of game
    if (flag == 0):
        first_drop()
    # if player can pass from first round now player should 
    # drop dice until one of the condition is Come true
    while True:
        a = drop_dice()
        one , two = a
        # if player dice after first round come's 7 - player lose
        if (one + two == 7):
            print(f"Player Lose")
            sys.exit(1)
        # if player dice after first round becomes equal to points - player wins 
        elif (one + two == points):
            print("Player win! Points and Dice are same")
            sys.exit(0)


main()    
