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


#  Last week we saw that we could create expressions using
#  "built-in" operators such as "+", "*", etc.  However, many
#  more operations are available as named "functions" (and some
#  known as "methods").  This demonstration illustrates some of
#  the many operations available on strings.


#----------
# Recap from last week - Recall that strings can
# be used in expressions in various ways:

"Hello" + ' ' + 'World'   # print("Hello" + ' ' + 'World')

'Ho, ' * 3 + 'Merry' + ' Christmas!'

quote = "'Goodbye', she exclaimed"

quote[12] + quote[13] + quote[18] * 2 + quote[2]



#----------
# We can easily find out how long a string is using the built-in
# length function:

len('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

len('xyz' + 'zy')

len('AAA\nBBB\nCCC')  # produces an interesting answer


#----------
# The Python Library Reference lists many helpful methods we
# can apply to strings:

'Who put the bomp in the bomp-de-bomp-de-bomp?'.count('bomp')

'Who put the bomp in the bomp-de-bomp-de-bomp?'.find('bomp')

'Who put the ram in the ram-a-lam-a-ding-dong?'.find('bomp')

'Who put the bomp in the bomp-de-bomp-de-bomp?'.replace('bomp', 'bip')


#----------
# It doesn't matter whether these operators are applied to
# specific string values, as shown above, or string-valued
# variables:

lyric = 'I love to love you, baby'

lyric[0]

lyric.find('baby')

lyric.count('love')

lyric.replace('love', 'hate')


#----------
# Another way to replace values in strings is to use "f-strings"
# in which the names of variables can appear in braces:

emote = 'love'

idol = 'baby'

f'I {emote} to {emote} you, {idol}'

f'Braces can appear in f-strings by doubling them: {{...}}'


#----------
# Keep in mind that if you want to save the result of
# evaluating a string-valued expression then you need to
# assign the value to a variable.  Python strings are
# "immutable" which means that the "replace" function
# above returned a new string value, but did not change the
# value of variable "lyric".  The following statement
# does a similar word replacement and saves the result:

new_lyric = lyric.replace('love', 'like')





#----------
# Lyrics quoted from "Who Put the Bomp?" by Barry Mann and
# Gerry Goffin (1961) and "Love to Love You Baby" (1975) by
# Giorgio Moroder, Pete Bellotte and Donna Summer

