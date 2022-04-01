from random import seed , randrange
import sys


def first_round_win(first,second):
    tmp = first + second
    if (tmp == 7 or tmp == 11):
        print("Player Win!")
        sys.exit(1)
    elif (tmp in [2, 3, 12]):
        print("PLAYER lose!:")    
        sys.exit(1)

    elif (tmp in [10, 9, 8, 6, 5, 4]):
        points = tmp  
        print(f"Points is {points}")

##############

def main():
    seed()
    points = 0
    first_round = 0

    while (True):
        first = randrange(1,7)
        second = randrange(1,7)
        total = first + second
        print(f"Player Rolled {first} + {second} = {total}")

        if (first_round == 0):
            first_round_win(first,second)
        first_round = 1

        if (total == 7):
            print("Player Lose Sum is 7 ")
            sys.exit(1)
        elif (total == points):
            print("you win! total and points equal")


main()