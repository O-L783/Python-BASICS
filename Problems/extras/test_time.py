#---------------------------------------------------------------------
#
# Demonstration timing execution
#
# This example shows how running the same function multiple times can
# help knowing in one way of coding it is faster than another.
#
# The function in this example only runs tests on a number that is 
# provided, and returns
# - 1 for numbers between 0 and 5
# - 2 for numbers between 5 and 10
# - 0 for numbers higher than 10
#
# All numbers above 0 are equally likely to be tested, so the chance
# of returning 0 is much higher than retrning 1 or 2
#
# The numbers this function is covering range from 0 to very large
# As a result, it is more likely that a number given to the function
# is higher than 10 than for it to be lower.
# The function is implemented in 2 ways that give the same result
# - the first approach first tests if the number is lower than 10
#   then tests if it is lower than 5.
# - the second approach first tests the most likely: if the
#   number is higher or equal to 10.
#   when that is not the case, then it tests if it is lower than 5

#---------------------------------------------------------------------
#
# Importing the module time to measure how long the code takes to run
import time


#---------------------------------------------------------------------
#
# First version of the function, where we test if the number is small
# first
def test_condition_small_first(number):
    if number < 10:
        if number < 5:
            return 1
        else:
            return 2
    else:
        return 0

#---------------------------------------------------------------------
#
# First version of the function, where we test if the number is large
# first       
def test_condition_large_first(number):
    if number >= 10:
        return 0
    else:
        if number < 5:
            return 1
        else:
            return 2


#---------------------------------------------------------------------
#
#Printing the difference in system's time between before and after
#running the tests 100,000 times with the first function
start = time.time()# Reading the system's time before the tests 
for try_number in range(100000):
    test_condition_small_first(try_number)
end = time.time() # Reading the system's time after the tests 

print(f"Execution time fixed values small first: {end - start:.4f} seconds")


#---------------------------------------------------------------------
#
#Printing the difference in system's time between before and after
#running the tests 100,000 times with the second function
start = time.time()# Reading the system's time before the tests 
for try_number in range(100000):
    test_condition_large_first(try_number)
end = time.time()# Reading the system's time after the tests 

print(f"Execution time fixed values large first: {end - start:.4f} seconds")





