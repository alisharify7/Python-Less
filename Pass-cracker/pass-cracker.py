import sys

# solve this question with list in python
""" معمای ریاضیاتی پیدا کردن رمز گاوصندوق

سینا پین‌کد ۵ رقمی گاوصندوق خود را فراموش کرده است. با این حال، اطلاعاتی درباره اعداد پین‌کد خود دارد
 جمع رقم‌های پنجم و سوم پین‌کد برابر با چهارده است
 رقم اول، یک واحد از دوبرابر رقم‌ دوم کمتر است
 رقم چهارم، یک واحد از رقم دوم بیشتر است.
 جمع رقم‌های دوم و سوم برابر با ده است
 حاصل‌جمع رقم‌های پین‌کد برابر با ۳۰ است

 

با توجه به این اطلاعات، پین‌کد سینا را تعیین کنید  """

def find_pass(number):
    # convert number to string to be can access to each element in it!
    # and with zfill function we force string to be 5 element 
    number = str(number).zfill(5)

    # in here we check the rules and if rules ok return true
    # and with int() type casting we convert string to a number to casting
    # math on it     
    if ( (int(number[4]) + int(number[2]) == 14) and 
    ( (int(number[1]) * 2 ) - 1  == int(number[0]) ) and 
    ( (int(number[3]) - 1 ) == int(number[1]) ) and 
    ( (int(number[1]) + int(number[2]) ) == 10 ) and 
    (int(number[0]) + int(number[1]) + int(number[2]) + int(number[3]) + int(number[4]) == 30) ):
        return True

    return False    
    



# from here we send from 0 to 99_999 to find pass function
for num in range(0,100000):
    # if find pass return true so we found passcode
    if (find_pass(num)):
        print(num)
        sys.exit(0)    



