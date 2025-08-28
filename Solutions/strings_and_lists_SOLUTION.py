#---------------------------------------------------------------------
#
# Some exercises involving sequences of values
#
# As we've seen, computer programs can manipulate text and ordered
# collections of values as well as numbers.  (Although, in reality,
# all values manipulated by a computer are really represented by
# zeros and ones!)
#
# Below are a collection of small exercises involving values of
# "string" and "list" type, designed to give you some practice with
# expressions that involve more than just numbers.
#

# Exercise: Draw a square
#
# Defined below are three string-valued variables.  Use these
# variables and Python's "print" and assignment statements to
# display a square with four asterisks on each side and blanks
# in the middle.  (There's more than one way to do this so
# try to find the shortest or most elegant way.)

one_star = '*'
two_stars = '**'
two_blanks = '  '

# Your solution goes here

top_and_bottom = two_stars * 2
middle = one_star + two_blanks + one_star

print(top_and_bottom)
print(middle)
print(middle)
print(top_and_bottom)


# An alternate use of variables and layout of the code.
pattern_one = two_stars + two_stars
pattern_two = one_star + two_blanks + one_star

pattern_output = ("\n\t" + pattern_one +
                  "\n\t" + pattern_two +
                  "\n\t" + pattern_two +
                  "\n\t" + pattern_one
                  ) # End of string

print(pattern_output)

# Exercise: Extract letters by position
#
# Below is a string-valued variable containing the alphabetic
# letters found on the top row of a QWERTY keyboard.  Use it
# to print the word 'PRETTY' by referencing the letters via
# their position.  Recall that we count from zero, so the letter
# 'E' is at position 2 in variable 'letters'.  Try to write
# the shortest expression that does this.

letters = 'QWERTYUIOP' # the top row of letters on a keyboard

# Your solution goes here

print(letters[9] + letters[3] + letters[2] + letters[4] * 2 + letters[5])


# Exercise: Where's Ringo?
#
# When the Beatles visited Australia in 1964 Ringo Starr was in
# hospital with tonsillitis, so he was replaced by drummer Jimmie
# Nicol at the start of the tour, as shown by the variable 'fab_four'
# below.  However, by the time the tour reached Melbourne Ringo
# was back on his feet and rejoined the group, replacing Jimmie.
# Write code to replace Jimmie with Ringo and then printthe
# resulting band line up.

fab_four = ['John', 'Paul', 'George', 'Jimmie']

# Your solution goes here

fab_four[3] = 'Ringo' # remember that we count from zero
print(fab_four)
