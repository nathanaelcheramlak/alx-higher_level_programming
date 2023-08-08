#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
list = []
for i in str(number):
    list.append(i)
last_digit = list[-1]
if (int(last_digit) > 5):
    if (list[0] == '-'):
        print(f'Last digit of {number} is -{last_digit} and is less than 6 and not 0')
    else:
        print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif (int(last_digit) < 5):
    if (list[0] == '-'):
        print(f'Last digit of {number} is -{last_digit} and is less than 6 and not 0')
    else:
        print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is 0 and is 0')

