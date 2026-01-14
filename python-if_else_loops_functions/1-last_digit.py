#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = int(str(number)[-1])
if number < 0:
    lastD *= -1
if lastD > 5:
    print(f"Last digit of {number} is {lastD} and is greater than 5")
elif lastD == 0:
    print(f"Last digit of {number} is {lastD} and is 0")
elif lastD < 6 and not 0:
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
