import random 
import sys
import alphabet
from colorama import Fore,init

init()

def validate_pass(passwd):
    """after password generate it this function analyze generate password
    if password is not required rule program regenerate password again"""
    # rule :  
    # password should have at least One Upper One lower One number
    # and One symbol
    upper = 0
    lower = 0
    numb = 0
    sym = 0
    for i in passwd:
        if i.isnumeric():
            numb += 1 
        elif i.isupper():
            upper += 1
        elif i.isupper():
            lower += 1
        elif ord(i) >= 48 and ord(i) <= 58:
            sym +=1           

    if not upper or not sym or not upper or not lower or not numb:
        return True
    return False    



def get_letter(lent):
    ret_value = []

    sym = alphabet.symbols
    a_low = alphabet.a_lower
    a_upp = alphabet.a_upper
    num = alphabet.numbers
    rand_list = [sym, a_low, a_upp, num]
    
    for i in range(lent):
        # randomly select a list between four list
        temp = random.randint(0,3)
        # get length of list
        len_target_list = len(rand_list[temp])
        select = random.randint(0,len_target_list-1)
        ret_value.append(rand_list[temp][select])
    return ret_value


def main():
    print("passGenerator")
    
    while True:
        try:
            print('For Quit Enter Q | q')
            user = input("\nEnter length on pass you want:\ninput must between 8 to 180\n==> ")
            if (user.upper() == 'Q'):
                sys.exit(0)
            if int(user) < 8 or int(user) >180:
                continue
            length = int(user)
        except (ValueError):
            print(f'{Fore.RED}invalid input :(')
            pass
        except EOFError:
            print('Quit Mode !')
            sys.exit(0)
        else:
            break



    let = get_letter(length)
    random.shuffle(let)
    res = validate_pass(let)
    if (res == True):
        print(f'{Fore.MAGENTA}Password Generate is: ',end='')
        for letter in let:
            print(f'{Fore.GREEN}{letter}',end='')
        print('')
        sys.exit(0)
    else:
        print('We cant Generate a Good password please Enter again :)')
        main()    
main()    
