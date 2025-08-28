#---------------------------------------------------------
#
# Your final grade
#
# QUT's default percentage cut-offs for the final grade
# awarded in a teaching unit are as follows.
#
#  Percentage   Grade
#   0 .. 24       1     Low fail
#  25 .. 39       2     Fail
#  40 .. 49       3     Marginal fail
#  50 .. 64       4     Pass
#  65 .. 74       5     Credit
#  75 .. 84       6     Distinction
#  85 .. 100      7     High distinction
#
# Notice that this is not a simple linear relationship.
# The first grade covers 25 percentage marks, the
# second 15, the third 10, and so on.  Therefore, to
# write some code to translate percentage marks into
# grades we will need to use one or more conditional
# statements.
#
# Below are some unit tests for a function called
# "final_grade" which accepts a percentage as its sole
# parameter and returns the corresponding grade.  Your
# job is to write the function which passes all these
# tests.  Note in the final two tests that if an
# invalid percentage is provided then the function
# returns -1, which cannot be a valid result, to flag
# the error.
#
# Also note that in cases where the final mark includes
# a fraction of a percent the mark is rounded off
# to the nearest whole number.
#
# The tests below tell us how your function is expected to
# behave when called.  After you've written your function,
# confirm that it works correctly by (a) running this module
# so that your function is defined and then (b) copying
# each of the function calls in the set of tests into the
# shell to see if the right answer is returned.  Obviously
# if you don't get the expected answers then you'll need
# to modify your code until you do.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  Of course, you should pass
# all the tests in order to complete this exercise.
#
# Footnote: Although the ranges above are the default
# cut-offs, there is no guarantee they will used by a
# particular teaching unit in a particular semester. The
# Faculty can always choose to change the cut-offs at the
# end of the semester.
#

# Part two challenge
# Comment out the last three lines of the file, the part that makes the
# automated tests run.
# Add your own code to prompt the user to input a value from the Shell window
# and call the tested function to compute the GPA value.
# Print the returned value back to the program user.

#---------------------------------------------------------
# These are the tests your function must pass.
#                       
""" 
>>> final_grade(85)     # Test 1. Normal case - high distinction, borderline
7

>>> final_grade(80)     # Test 2. Normal case - distinction
6

>>> final_grade(74)     # Test 3. Normal case - borderline credit
5

>>> final_grade(49.9)   # Test 4. Normal case - borderline pass, floating point
4

>>> final_grade(49.1)   # Test 5. Normal case - marginal fail
3

>>> final_grade(24.3)   # Test 6. Normal case - low fail
1

>>> final_grade(10)     # Test 7. Normal case - low fail
1

>>> final_grade(0)      # Test 8. Boundary case - no evidence
1

>>> final_grade(-1)     # Test 9. Invalid case - mark too low
-1

>>> final_grade(110)    # Test 10. Invalid case - mark too high
-1

>>> final_grade(39.49)  # Test 11. Normal case - fail
2

>>> final_grade(99.95)  # Test 12. Normal case - high distinction, rounds to upper limit
7

"""

#---------------------------------------------------------
# A function which, when given a percentage, returns
# the corresponding grade.
#

##### DEFINE YOUR final_grade FUNCTION HERE
pass


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
