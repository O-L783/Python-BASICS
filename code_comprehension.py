#---------------------------------------------------------------------
#
# Code comprehension
#
# The following small exercise is designed to confirm
# that you understand the way computer languages evaluate
# expressions and assign values to variables.  There is no
# solution file for this question - you get the answer by
# "running" this file and seeing what it prints.  However,
# DON'T do so until you've attempted the exercise yourself!

# Challenge: Without running the program, work out what
# final value the following code segment will print.

balance = 500
print('Opening:', balance)

rate = 4
months = 6

percent = (rate * months) // 12 # 2
interest = (balance * percent) // 100 # 10

balance = balance + interest # 500 + 10
print('Closing:', balance) # 510

# After trying the exercise, read on ...
#
#
#
#
#
# Hopefully the value you calculated manually matched the
# one printed when you ran the program.  If you're still
# not sure how it works you can add some extra "print"
# statements to display the values of the intermediate
# variables such as "percent".
#
# The program performs a useful calculation.  It tells you
# what your bank balance will be if you invest $500 for
# 6 months at an interest rate of 4% per annum.
#
# To do the calculation we introduced several intermediate
# variables.  We gave these variables meaningful names to
# make the code easier to understand for the (human)
# reader.  Also note how the old value of variable
# "balance" is overwritten with a new value in the final
# assignment statement.
#
# Finally, as usual in programming, there are many other ways
# to perform the same calculation.  The code could be made
# shorter, but not necessarily clearer, by eliminating
# some of the intermediate variables such as "percent".
# Alternatively, the calculation could be done
# in more, but simpler, steps by introducing additional
# intermediate variables.  Feel free to experiment by
# modifying the code yourself.
#
#---------------------------------------------------------------------
