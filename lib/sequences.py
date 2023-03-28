#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_list = [0, 1]
        for i in range(2, length):
            next_fib = fib_list[i-1] + fib_list[i-2]
            fib_list.append(next_fib)
        print(fib_list)

print_fibonacci(10)