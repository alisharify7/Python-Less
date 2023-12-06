import sys

def find_pass(number):
    number = str(number).zfill(5)
    if ( (int(number[4]) + int(number[2]) == 14) and 
    ( (int(number[1]) * 2 ) - 1  == int(number[0]) ) and 
    ( (int(number[3]) - 1 ) == int(number[1]) ) and 
    ( (int(number[1]) + int(number[2]) ) == 10 ) and 
    (int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]) + int(number[4]) == 30) ):
        return True
    return False    


for num in range(0,100000):
    if (find_pass(num)):
        print(num)
        sys.exit(0)    



