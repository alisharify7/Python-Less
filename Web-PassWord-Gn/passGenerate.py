import random 
import alphabet


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
        return 'True'
    return 'False'    



def get_letter(lent):
    ret_value = []
    """Generate password with Random index and all letters
    And Return it in list form"""
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


def gnt(argument):

    try:        
        length = int(argument)
    except ValueError:
        return "PLease Positive Number"    
    if length > 180 or length < 8:
        return 'Between 8 - 180'    
    let = get_letter(length)
    random.shuffle(let)
    
    res = ''
    for each in let:
        res+=each
    return res    
 
    