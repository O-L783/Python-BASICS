#---------------------------------------------------------------------
#
# The variable olympic_medal_table is a list of medals won for a
# selected group of countries at the last Olympic Games - Paris
# (source Wikipedia)
#
# The list consists of entries for country,
#   [number of gold medals, number of silver medals, number of bronze medals]
# For example in our table Greece has 1 Gold Medal, 1 Silver Medal and
# 6 Bronze Medals.
#
# NB  This is only a partial table, showing the result of a small group of
# countries.  Your solutions CANNOT be hard-wired but must work for any
# table of this format.
#
# The full list of countries with associated olympic medals is included at
# the end of this file if you prefer to work with the full list.
# 
# Below is a series of small tasks to process this list of medals.


olympic_medal_table = [["France", [16, 26, 22]],
 ["Great Britain", [14, 22, 29]],
 ["Greece", [1, 1, 6]],
 ["Switzerland", [1, 2, 5]],
 ["Albania", [0, 0, 2]],
 ["Argentina", [1, 1, 1]],
 ["Armenia", [0, 3, 1]],
 ["Australia", [18, 19, 16]],
 ["Botswana", [1, 1, 0]],
 ["Pakistan", [1, 0, 1]],
 ["Colombia", [0, 3, 1]],
 ["Morocco", [1, 0, 1]],
 ["Peru", [0, 0, 1]],
 ["Portugal", [1, 2, 1]],
 ["Singapore", [0, 0, 1]],
 ["Ecuador", [1, 2, 2]],
 ["Malaysia", [0, 0, 2]],
 ["Austria", [2, 0, 3]],
 ["New Zealand", [10, 7, 3]],
 ["India", [0, 1, 5]]]

 
 
# Task 1
# print the name of the country that has won the most Gold Medals.
# For a challenge print the top 3 countries

pass



# Task 2
# print the name of the country that has won the most medals in total

pass



# Task 3
# In many cases there is a weighting to the type of medal won
# For example two gold medals would be worth more than 5 bronze medals
# There are many weighting systems used eg 3:2:1 (3 points for each gold
# medal, two points for each silver medal and one point for each bronze
# medal).  Other weighting systems are commonly used.  For this exercise
# we will use the weighting system 5:3:1.  Using this system, calculate
# which country has won the most medals

pass



# task 4
# Display in table format the olympic medal table.  For example
# Country          Gold    Silver  Bronze
# Great Britain    14      22      29
# Greece            1       1       6
# Switzerland       1       2       5

pass


    

# This is the full list of countries with gold, silver and bronze
# medal counts
olympic_table =[['Ireland', [4, 0, 3]],
                ['Austria', [2, 0, 3]],
                ['Czech Republic', [3, 0, 2]],
                ['Hong Kong', [2, 0, 2]],
                ['Philippines', [2, 0, 2]],
                ['Algeria', [2, 0, 1]],
                ['Dominican Republic', [1, 0, 2]],
                ['Indonesia', [2, 0, 1]],
                ['Tajikistan', [0, 0, 3]],
                ['Albania', [0, 0, 2]],
                ['Grenada', [0, 0, 2]],
                ['Guatemala', [1, 0, 1]],
                ['Malaysia', [0, 0, 2]],
                ['Morocco', [1, 0, 1]],
                ['Puerto Rico', [0, 0, 2]],
                ['Cape Verde', [0, 0, 1]],
                ['Dominica', [1, 0, 0]],
                ['Ivory Coast', [0, 0, 1]],
                ['Pakistan', [1, 0, 0]],
                ['Peru', [0, 0, 1]],
                ['Qatar', [0, 0, 1]],
                ['Refugee Olympic Team', [0, 0, 1]],
                ['Singapore', [0, 0, 1]],
                ['Slovakia', [0, 0, 1]],
                ['Zambia', [0, 0, 1]],
                ['Belgium', [3, 1, 6]],
                ['Cuba', [2, 1, 6]],
                ['Greece', [1, 1, 6]],
                ['Norway', [4, 1, 3]],
                ['Bulgaria', [3, 1, 3]],
                ['India', [0, 1, 5]],
                ['Serbia', [3, 1, 1]],
                ['Bahrain', [2, 1, 1]],
                ['Moldova', [0, 1, 3]],
                ['Argentina', [1, 1, 1]],
                ['Egypt', [1, 1, 1]],
                ['Slovenia', [2, 1, 0]],
                ['Tunisia', [1, 1, 1]],
                ['Botswana', [1, 1, 0]],
                ['Chile', [1, 1, 0]],
                ['Kosovo', [0, 1, 1]],
                ['Saint Lucia', [1, 1, 0]],
                ['Uganda', [1, 1, 0]],
                ['Cyprus', [0, 1, 0]],
                ['Fiji', [0, 1, 0]],
                ['Jordan', [0, 1, 0]],
                ['Mongolia', [0, 1, 0]],
                ['Panama', [0, 1, 0]],
                ['Uzbekistan', [8, 2, 3]],
                ['Kenya', [4, 2, 5]],
                ['Denmark', [2, 2, 5]],
                ['Switzerland', [1, 2, 5]],
                ['Azerbaijan', [2, 2, 3]],
                ['Croatia', [2, 2, 3]],
                ['Kyrgyzstan', [0, 2, 4]],
                ['North Korea', [0, 2, 4]],
                ['Ecuador', [1, 2, 2]],
                ['Lithuania', [0, 2, 2]],
                ['Portugal', [1, 2, 1]],
                ['Turkey', [0, 3, 5]],
                ['Georgia', [3, 3, 1]],
                ['Kazakhstan', [1, 3, 3]],
                ['Jamaica', [1, 3, 2]],
                ['South Africa', [1, 3, 2]],
                ['Thailand', [1, 3, 2]],
                ['Mexico', [0, 3, 2]],
                ['Armenia', [0, 3, 1]],
                ['Colombia', [0, 3, 1]],
                ['Ethiopia', [1, 3, 0]],
                ['Spain', [5, 4, 9]],
                ['Sweden', [4, 4, 3]],
                ['Poland', [1, 4, 5]],
                ['Ukraine', [3, 5, 4]],
                ['Israel', [1, 5, 1]],
                ['Iran', [3, 6, 3]],
                ['Netherlands', [15, 7, 12]],
                ['Canada', [9, 7, 11]],
                ['Brazil', [3, 7, 10]],
                ['New Zealand', [10, 7, 3]],
                ['Hungary', [6, 7, 6]],
                ['South Korea', [13, 9, 10]],
                ['Japan', [20, 12, 13]],
                ['Italy', [12, 13, 15]],
                ['Germany', [12, 13, 8]],
                ['Australia', [18, 19, 16]],
                ['Great Britain', [14, 22, 29]],
                ['China', [40, 27, 24]]]



