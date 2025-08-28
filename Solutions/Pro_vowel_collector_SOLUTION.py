#---------------------------------------------------------
#
# Vowel collector
#
# Define an iterative function with one parameter, a string,
# which returns just the vowels from the given string.
#
# Recall that the vowels in english are a, e, i, o and u.
#

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> vowels_only('abc') # Test 1
'a'

>>> vowels_only('My very elegant mother just sat upon nine porcupines') # Test 2
'eeeaoeuauoieouie'

>>> vowels_only('The quick brown fox jumps over the lazy dog') # Test 3
'euioouoeeao'

>>> vowels_only('aeiou') # Test 4
'aeiou'

>>> vowels_only('') # Test 5
''

>>> vowels_only('xyzzy') # Test 6
''

"""


#---------------------------------------------------------
#


# Given a string, return just the vowels
def vowels_only_1(text):

    # Initialise the string to be returned
    vowels = ''
    
    # Collect each vowel (ForEach)
    for character in text:

        # Test the character
        if character in 'aeiou':
            vowels += character

    # Return the result
    return vowels

# Given a string, return just the vowels
def vowels_only_2(text):

    # Initialise the string to be returned
    vowels = ''
    
    text_length = len(text)     # Initialise loop control to string length

    # Loop while data to test
    for loop in range(text_length):

        character = text[loop]  # Extract character from array

        # Test the character
        if character in 'aeiou':
            vowels += character

    # Return the result
    return vowels

# Given a string, return just the vowels
def vowels_only(text):

    # Initialise the string to be returned
    vowels = ''
    
    # Collect each vowel (ForEach)
#    for character in text:

    loop = len(text)    # Initialise loop control to string length
    index = 0           # Start array at beginning
    
    while loop:         # Loop while data to test

        character = text[index]     # Extract character from array

        # Test the character
        if character in 'aeiou':
            vowels += character
            #vowels = vowels + character

        loop -= 1   # Decrement the loop control var
        index += 1  # Increment the array index
        
    # Return the result
    return vowels


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
