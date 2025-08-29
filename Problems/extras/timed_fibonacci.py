############################################################
#
# Timed Fibonacci
#
# To show the inefficiency of a naive Fibonacci calculation
# using recursion, this demonstration calls a recursive
# Fibonacci function multiple times with different arguments
# and measures how long it takes.
#

# Get the function for measuring execution times
from timeit import timeit

# Define a recursive Fibonacci function (which
# is concise but inefficient because it
# calculates the same value multiple times)
def fibonacci(index):
   if index == 0 or index == 1: # Base cases
       return index
   else: # Recursive case
       return fibonacci(index - 1) + \
              fibonacci(index - 2)

# Time several invocations of the Fibonacci function (messy
# bit of code - Yuk! - but doesn't matter for our purposes
# here)
for fib_index in range(40):
    function_call = 'fibonacci(' + str(fib_index) + ')'
    print(function_call + ' = ', end = '')
    print(' and took', round(timeit('print(' + function_call + ', end =""), ', \
                      "from __main__ import fibonacci", number = 1), 4), 'seconds')
