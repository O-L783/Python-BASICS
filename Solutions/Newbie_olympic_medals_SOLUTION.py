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



# initialise a max number of gold tally
number_gold = -1
country = ""
# for each entry in olympic_medal_table
for entry in olympic_medal_table:
    # if new max found, update tally and keep country
    if entry[1][0] > number_gold:
        number_gold = entry[1][0]
        country = entry[0]
print("The country that has won the most Gold Medals:", country)
print()


# Task 2
# print the name of the country that has won the most medals in total



# initialise a tally counter
num_medals = -1
country = ""
# for each line in table
for entry in olympic_medal_table:
    # add up all medals
    # if new maz found, update tally and keep country
    if sum(entry[1]) > num_medals:
        num_medals = sum(entry[1])
        country = entry[0]
print("The country that has won the most total medals:", country)
print()

# Task 3
# In many cases there is a weighting to the type of medal won
# For example two gold medals would be worth more than 5 bronze medals
# There are many weighting systems used eg 3:2:1 (3 points for each gold
# medal, two points for each silver medal and one point for each bronze
# medal).  Other weighting systems are commonly used.  For this exercise
# we will use the weighting system 5:3:1.  Using this system, calculate
# which country has won the most medals



gold = 5
silver = 3
bronze = 1

num_medals = -1
country = ""
for entry in olympic_medal_table:
    # sum up the weighted medal count
    medal_total = gold * entry[1][0] + silver * entry[1][1] + \
                  bronze * entry[1][2]
    # new max found
    if medal_total > num_medals:
        num_medals = medal_total
        country = entry[0]
print("The country that has the highest weighted medal count", country)
print()

# task 4
# Display in table format the olympic medal table.  For example
# Country          Gold    Silver  Bronze
# Great Britain    14      22      29
# Greece            1       1       6
# Switzerland       1       2       5



# Check settings for length of tab, default is 4
tab_length = 4
print("Country\t\tGold\tSilver\tBronze")
for country, medals in olympic_medal_table:
    print(country, "\t", end = "")
    # if country name is short, add tab to ensure spacing
    if len(country) < tab_length * 2 - 1:
        print("\t", end = '')

    
    gold = medals[0]
    silver = medals[1]
    bronze = medals[2]
    # format numbers using right justification to line up numbers
    print(str(gold).rjust(3) + "\t" + str(silver).rjust(4) + "\t" + \
          str(bronze).rjust(4))
    

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



