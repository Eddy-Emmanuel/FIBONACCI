"""
The Fibonacci sequence is a famous mathematical pattern credited to Italian mathematician Fibonacci in the 13th century 
(though others had discovered it even earlier). 
The sequence begins with 0 and 1, and the next number is always the sum of the previous two numbers. 
The sequence continues forever:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 . . .
"""

import time
from tqdm import tqdm

def timer_decorator(func):
    def timer_function(*arg, **kwarg):
        start_time = time.time()
        function = func(*arg, **kwarg)
        end_time = time.time()
        print("Runtime: {}".format(end_time - start_time))
        return function
    return timer_function

@timer_decorator
def Fibonacci_2_steps(x):
    # Conditions that must be met before printing the sequence
    if x <= 0:
        print("Enter a number greater than zero.")
        return
    elif x == 1:
        print("Fibonacci sequence: 0")
        return
    elif x == 2:
        print("Fibonacci sequence: 0, 1")
        return

    # Initialize the first two numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence with 2 steps
    for _ in tqdm(range(2, x)):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    # Print the sequence
    print("Fibonacci sequence:", ", ".join(map(str, fib_sequence)))

@timer_decorator
def Fibonacci_3_steps(x):
    # Conditions that must be met before printing the sequence
    if x <= 0:
        print("Enter a number greater than zero")
        return
    elif x == 1:
        print("Fibonacci sequence: 0")
        return
    elif x == 2:
        print("Fibonacci sequence: 0, 1")
        return

    fib_sequence = [0, 1, 1]
    
    print("Fibonacci sequence: 0, 1, ", end="")

    for _ in tqdm(range(3, x + 1)):
        next_number = fib_sequence[-1] + fib_sequence[-2] + fib_sequence[-3]
        fib_sequence.append(next_number)

    print("Fibonacci sequence:", ", ".join(map(str, fib_sequence)))
            

if __name__ == "__main__":
    Fibonacci_3_steps(50)





    