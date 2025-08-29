#---------------------------------------------------------------------
#
# Demonstration - Speak up!
#
# This is a small example of developing code to satisfy unit tests.
# Assume we want a function which emphasises some given text
# by capitalising it and adding an exclamation mark.
#



# 1. First we prepare a function to do the job
def speak_up(text):
    # 2. Then we write some examples showing what
    #    we want the function to do 

    '''
    These are the tests our function must pass ...

    Test 1
    >>> speak_up('Hello')
    'HELLO!'

    Test 2
    >>> speak_up('What did you say?')
    'WHAT DID YOU SAY?!'

    Test 3
    >>> speak_up("I'm very shy")
    "I'M VERY SHY!"

    '''
    # 3. Then we write the actual job the function does
    return text.upper() + '!'

# 4. Then we add code to run the tests automatically
from doctest import testmod
print(testmod())

# 5. We can also run the code at the same time
print(speak_up('What did you say?'))
