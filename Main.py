# practicing python built-in functions
import math

money = 13.99
print(math.floor(abs(money)))

if 210 > 100:
    print(True)

a = "Get That Money"
b = 354

print(a)
print(b)

money = 9

def get_that_money():
    if money > 100:
        print('You got that money 🤩')
    else:
        print('you didnt get that money!!!')

def make_sure_its_even():
    if money % 2 == 0:
        print('and its even 👀')
    elif money % 1 == 0:
        print('youre an oddball man... 🫡')

make_sure_its_even()
get_that_money()
