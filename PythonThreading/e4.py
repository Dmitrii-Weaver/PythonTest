# Write a Python program to calculate the factorial of a number using multiple threads.

import threading


def factorial_of_a_anumber(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def calculate_factorial(n):
    print(
        f"\nCalculating factorial of {n} in thread {threading.current_thread().name}")
    result = factorial_of_a_anumber(n)
    print(
        f"Factorial of {n} is {result} in thread {threading.current_thread().name}")


n = 12

thread1 = threading.Thread(target=calculate_factorial, args=(n,))
thread2 = threading.Thread(target=calculate_factorial, args=(n,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
