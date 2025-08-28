#---------------------------------------------------------
#
# Both parts A and B will need to be completed to pass all the tests.
#
# **********  Part A  ************
# A String Manipulation Functions
#
# For Part A you will create three functions for manipulating
# text strings.  These functions will be used in Part B.
#
# Hint: You will find some very helpful string methods for
# this exercise in the Python Standard Library
# reference manual.
#
# The tests below tell us how your functions are expected to
# behave when called.  After you've written your functions,
# confirm that they work correctly by (a) running this module
# so that your functions are defined and then (b) copying
# each of the function calls in the set of tests into the
# shell to see if the right answer is returned.  Obviously
# if you don't get the expected answers then you'll need
# to modify your code until you do.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  Of course, you should pass
# all the tests in order to complete this exercise.  Note
# that the tests for Part B have been commented out.  You
# will need to uncomment these when you have implemented
# Part B.
#



#---------------------------------------------------------
# These are the tests your three Part A functions must pass.  We
# have included a number of tests for each of the three
# functions you have to write.
#
""" 
Part 1: Tests for the convert_to_upper function

>>> convert_to_upper('what') # Test A1 - normal case (all lower case chars)
'WHAT'

>>> convert_to_upper('WHY') # Test A2 - normal case (all upper case chars)
'WHY'

>>> convert_to_upper('Which, Who, When') # Test A3 - normal case (mixed case chars)
'WHICH, WHO, WHEN'

>>> convert_to_upper('') # Test A4 - boundary case (empty string)
''


Part 2: Tests for the remove_spaces function

>>> remove_spaces('H E L P !!') # Test B1 - normal case (multiple spaces)
'HELP!!'

>>> remove_spaces('  The End   ') # Test B2 - normal case (leading and trailing spaces)
'TheEnd'

>>> remove_spaces('ThisOneIsOkAsIs') # Test B3 - boundary case (no spaces)
'ThisOneIsOkAsIs'

>>> remove_spaces('') # Test B4 - boundary case (empty string)
''

>>> remove_spaces('    ') # Test B5 - boundary case (only spaces)
''


Part 3: Tests for the replace_stops function

>>> replace_stops('Stop.') # Test C1 - normal case (one occurrence)
'StopSTOP'

>>> replace_stops('Need help. Reply urgently.') # Test C2 - normal case (two occurrences)
'Need helpSTOP Reply urgentlySTOP'

>>> replace_stops('...') # Test C3 - unusual case (nothing but full stops)
'STOPSTOPSTOP'

>>> replace_stops('Hello world, how are you today?') # Test C4 - boundary case (no full stops)
'Hello world, how are you today?'

**** These will need to be uncommented for part B ***
*****************************************************

>>> telegram('Urgent Message.  Please Read.') # Test 1 - normal case
'URGENTMESSAGESTOPPLEASEREADSTOP'

>>> telegram('Do not stop.') # Test 2 - normal case
'DONOTSTOPSTOP'

>>> telegram('Return home. Explain later.') # Test 3 - normal case
'RETURNHOMESTOPEXPLAINLATERSTOP'

>>> telegram('URGENTMESSAGEPLEASEREAD') # Test 4 - all caps, no spaces
'URGENTMESSAGEPLEASEREAD'

>>> telegram('UrgentMessagePleaseRead') # Test 5 - mixed case, no spaces
'URGENTMESSAGEPLEASEREAD'

>>> telegram(' . . . ') # Test 6 - unusual case: only stops and spaces
'STOPSTOPSTOP'

>>> telegram('') # Test 7 - boundary case: empty string
''

"""


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all alphabetic characters in upper case.
# (Hint: This can be done trivially using Python's
# built-in "upper" method for strings.)

#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all blank spaces removed.
# (Hint: This can be done easily using Python's built-in
# "replace" method for strings.)

#---------------------------------------------------------
# Define a function which, when given a string, returns
# it with all occurrences of full stops '.'
# replaced with the word 'STOP'.



#### DEFINE YOUR remove_spaces FUNCTION HERE

def convert_to_upper(convert):
    result = convert.upper()
    return result

def remove_spaces(empty_space):
    result_2 = empty_space.replace(' ', '')
    return result_2

def replace_stops(string):
    result_3 = string.replace('.', 'STOP')
    return result_3


#---------------------------------------------------------
#---------------------------------------------------------
#
# **********  Part B  ************
# Telegrams
#
# Define a function with one parameter, a string representing
# a message.  Your function is to return that message in capital
# letters, with every full-stop replaced with "STOP", and 
# all spaces removed, so that it looks like an old-fashioned
# telegram.  (Telegrams were sent on equipment that could transmit
# upper-case letters only.  The operator would cut the words
# from a ticker-tape strip and paste them onto a piece of paper
# to create the telegram for delivery to the recipient.)
#
# As an exercise in reuse of functions, you must do this using
# your solution to Part A above.  Use your previously defined
# functions "replace_stops", "remove_spaces" and "convert_to_upper"
# to implement your "telegram" function.
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


#---------------------------------------------------------
# Define a function which, when given a string, returns
# it in telegram format, i.e., all in caps, with full-stops
# replaced with the word "STOP" and spaces removed.
#

#### DEFINE YOUR telegram FUNCTION HERE
def telegram(message):
    
    return convert_to_upper(replace_stops(remove_spaces(message)))

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.


if __name__ == '__main__':
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))


