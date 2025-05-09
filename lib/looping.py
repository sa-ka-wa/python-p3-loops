#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count_down = 10
    while count_down > 0:
        print(count_down)
        count_down -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    int_list = [1, 2, 3, 4, 5]
    for i in range(len(int_list)):
        int_list[i] = int_list[i] ** 2
    return int_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    pass
