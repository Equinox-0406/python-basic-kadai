import random

var = random.randint(0,100)

if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
elif var % 5 == 0:
    print("Buzz")
elif var % 3 == 0:
    print("Fizz")
else:
    print(var)