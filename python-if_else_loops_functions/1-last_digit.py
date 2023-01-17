#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number % 10) > 5:
    print(f"last digit of {number} is {number % 10} and is greater than 5")
elif ((number % 10) == 0):
    print(f"last digit of {number } is and {number % 10}")
elif ((number % 10) < 6 and (number % 10 != 0)):
    if (number < 0):
        number *= -1
        print(
            f"last digit of {-1*number} is {number%10} and is less than 6 and not 0")
    print(
        f"last digit of {number} is {number%10} and is less than 6 and not 0")
