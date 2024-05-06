#!/usr/bin/python3

def fizzbuzz():
    num = [x for x in range(1, 101)]
    for i in num:
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(i, end=" ")
