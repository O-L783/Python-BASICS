#---------------------------------------------------------------------
#
#  Demonstration - More operations on sequences
#
#  Note: This file contains various expressions to be evaluated.
#  When you "run" this file in IDLE nothing will appear to happen,
#  because the expressions are evaluated but the results don't "go"
#  anywhere.  To see the value of an expression below, after
#  running the file, you can either:
#
#    a) copy the expression into IDLE's shell window and hit
#       the Enter key; or
#
#    b) put brackets around the expression below then precede
#       the expression with "print", which tells IDLE
#       to display the result, and then run the file again.


#  In week 1 we saw that we could create expressions using
#  "built-in" operators such as "+", "*", etc.  However, many
#  more operations are available as named "functions" (and some
#  known as "methods").  This demonstration illustrates some of
#  the many operations available on lists.


#----------
# Recap from week 1 - Recall that lists can
# be used in expressions in various ways:



superheroes1 = ['Superman', 'Batman']
superheroes2 = ['The Flash', 'Wonder Woman']

(superheroes1 + superheroes2)[3]


#----------
# There are many useful built-in functions for manipulating
# lists:

some_numbers = [4, 6, 2, 3, 8, 9, 7]

max(some_numbers) # returns the largest number in the list

sum(some_numbers) # returns the sum of the numbers

sorted(some_numbers)  # returns a new, sorted list


#----------
# We can save the result of evaluating a list-valued expression
# by assigning it to a variable:

temperatures = [32, 38, 37] # a list of temperatures

temperatures[0]  # returns the first temperature in the list

temperatures = temperatures + [31, 30] # add some extra values and save the result

len(temperatures)  # tells us that the list now has five values


#----------
# Unlike strings, lists are "mutable", which means that some operations
# on them will change their value "in place", without the need to
# assigning the result back to the variable:

weekdays = ['Mon', 'Tue', 'May', 'Thu', 'One', 'Fri', 'Sat']  # is not right

weekdays[2] = 'Wed'  # replaces the item at index 2

weekdays.remove('One') # gets rid of an incorrect item

weekdays.append('Sun')  # adds a new item at the end

weekdays # now returns a correct list of weekdays


#----------
# Lyrics quoted from "Who Put the Bomp?" by Barry Mann and
# Gerry Goffin (1961) and "Love to Love You Baby" (1975) by
# Giorgio Moroder, Pete Bellotte and Donna Summer

