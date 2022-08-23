#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            continue
        elif i % 15 == 0:
            print('FizzBuzz')
            continue
        else:
            print("{:d}".format(i), end="")
        i += 1
