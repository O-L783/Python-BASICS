#-----Statement of Authorship----------------------------------------#
#
# This is an individual assessment task for QUT's teaching unit
# IFB104, "Building IT Systems", Semester 2, 2025. By submitting
# this code I agree that it represents my own work. I am aware of
# the University rule that a student must not act in a manner
# which constitutes academic dishonesty as stated and explained
# in QUT's Manual of Policies and Procedures, Section C/5.3
# "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
# Put your student number here as an integer and your name as a
# character string:
#
student_number = 12421731
student_name = 'oscar li'
#
# NB: All files submitted for this assessable task will be subjected
# to automated plagiarism analysis using a tool such as the Measure
# of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Assessment Task 1 Description----------------------------------#
#
# This assessment task tests your skills at processing large data
# sets, creating reusable code and following instructions to retrieve
# information. The incomplete Python program below is
# missing the required functions.
# In part A, you are required to complete the provided function
# so that when the program runs it passes the defined tests.
# In part B, you will add your own functions and tests to respond
# to the full client requirements, provided at the end of week 4. 
# See the instructions on Canvas for full details and submission. 
#
# Note that this assessable assignment is in multiple parts,
# simulating incremental release of instructions by a paying
# "client". This single template file will be used for all parts
# and you will submit your final solution as this single Python 3
# file only, whether or not you complete all requirements for the
# assignment.
#
# All of your code must appear in this file only.
# DO NOT CHANGE THE NAME OF THIS FILE FOR SUBMISSION to Gradescope.
# Your solution will not work if it relies on any other files.
#
#--------------------------------------------------------------------#

#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from sys import exit as abort
from doctest import testmod

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
	print('\nUnable to run: No student number supplied',
	'(must be an integer), aborting!\n')
	abort()
if not isinstance(student_name, str):
	print('\nUnable to run: No student name supplied',
	'(must be a character string), aborting!\n')
	abort()


#-----Student's Solution---------------------------------------------#
#
# Complete the assignment by completing the price_range function below
# with your own parameter definition and your own code
# you can add other functions needed to support it in this section
# All of your solution code must appear in this section.
# All of your solution code has to be within functions.
# Do NOT change any of the provided code elsewhere except as allowed 
# by the comments in the next section.
#



def price_range(book_price, book_type):
        
        """ 
        >>> price_range(2.0, "Softcover") # Test 1 - typical case, specified inputs
        'Cheap'

        >>> price_range(30.5, "Paperback") # Test 2 - typical case, specified inputs
        'Average'

        >>> price_range(80.0, "Hardback") # Test 3 - typical case, specified inputs
        'Expensive'

        >>> price_range(60.0, "Magasine") # Test 4 - specified price, unknown type
        'Expensive'

        >>> price_range(-2.0, "Softcover") # Test 5 - negative price
        'Invalid'z

        >>> price_range(12.0) # Test 6 - specified price, no type 
        'Average'

        >>> price_range() # Test 7 - no inputs specified
        'Invalid'

        """
        
        
        if 0 <= book_price < 10:
                if book_type == 'Hardback':
                        return 'Cheap'
                if book_type == 'Paperback':
                        return 'Cheap'
                if book_type == 'Softcover':
                        return 'Cheap'
                if book_type == None:
                        return 'Cheap'
                if book_type == '':
                        return 'Cheap'
                else:
                        return 'Cheap'
                

        elif 10 <= book_price < 25:
                if book_type == 'Hardback':
                        return 'Cheap'
                if book_type == 'Paperback':
                        return 'Cheap'
                if book_type == 'Softcover':
                        return 'Average'
                if book_type == None:
                        return 'Average'
                if book_type == '':
                        return 'Average'
                else:
                        return 'Average'
                

        elif 25 <= book_price < 50:
                if book_type == 'Hardback':
                        return 'Cheap'
                if book_type == 'Paperback':
                        return 'Average'
                if book_type == 'Softcover':
                        return 'Average'
                if book_type == None:
                        return 'Average'
                if book_type == '':
                        return 'Average'
                else:
                        return 'Average'
                

        elif 50 <= book_price < 80:
                if book_type == 'Hardback':
                        return 'Average'
                if book_type == 'Paperback':
                        return 'Expensive'
                if book_type == 'Softcover':
                        return 'Expensive'
                if book_type == None:
                        return 'Expensive'
                if book_type == '':
                        return 'Expensive'
                else:
                        return 'Expensive'
                

        elif book_price >= 80:
                return 'Expensive'
        elif book_price < 0:
                return 'Invalid'
        elif book_price == None:
                return 'Invalid'
        elif not '':
                return 'Invalid'
        elif book_price != 0:
                return 'Invalid'
        else:
                return 'Invalid'


#-----Main Program to Run Student's Solution-------------------------#

if __name__ == "__main__":
        
        #You can change the code in this section, however
        #only within the "if" statement.
        #in other words, any code you add has at least 1 level of indentation

        #this section is not marked. You can use it to test your functions

        print(testmod())


   
# if booktype == 'hardcover'
# return blablabla
# elif price > or < than x


# don't forget if book_type == none to check for no inputs
# if __name__ == "__main__":
#             price_range(2.0, "Softcover")
# print("This is if line 5 it means that the book should be less than $9 and a softcover")
# https://www.w3schools.com/python/python_dictionaries.asp but also look up "look up tables"

# if price == :
#     if book_type == :
#         print ("Cheap")
#     elif book_type == :
        
        












# https://stackoverflow.com/questions/26226489/how-do-you-get-python-to-detect-for-no-input
# ask yourself this: what does an empty function return?
