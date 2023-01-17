#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number)
if (number % 10) < 6 and (number % 10) != 0:
    print(f"last digit of {number} is greater than 5")
elif ((number % 10) == 0):
    print(f"last digit of {number} is 0")
elif (number % 10) > 5:
    print(f"last digit of {number} is less than 6 and not 0")
