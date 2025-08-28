
# Debugging
# Below is a function that attempt to check a given character and
# return True if the character is a consonant (an alphabetic character
# that is not a vowel) and false otherwise.
# Examples of consonants are "b", "C", "f" etc.
# The vowels are "AEIOU" either uppercase or lower case.
#
# Run the provided code.
# 
# Use a debugger to step through the if condition:
#      There should be a break point set up on the if condition,
#      turn the debuger on:
#         in the shell window, choose Debug from the menu options, then select
#         debugger.
#
# Identify why the function is returning incorrect results.
#
# Fix any issues and verify.
#  

def is_consonant(char):
    if char.isalpha():
        if not (char in "aeiou" or char in "AEIOU"):
            return True
        return False
    else:
            return False


    
print(is_consonant("A")) # should print Flase
print(is_consonant("e")) # should print False
print(is_consonant("O")) # should print False
print(is_consonant("u")) # should print False
print(is_consonant("x")) # should print True
print(is_consonant("Z")) # should print True
print(is_consonant("#")) # should print False
