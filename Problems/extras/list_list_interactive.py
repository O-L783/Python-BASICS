#this module demonstrates the IFB104 week 5 example
#it uses only one of the approaches presented in the accompanying demo (list_list.py)
#and adds the function, interaction and test. 

#the problem is as follows:
#Input: on a single line, a list of animals is provided.
#For each animal, its name is provided, followed by its height (in cm) and weight (in kg).
#The list is provided on a single line, with values separated by spaces. For example:
#unicorn 120 190 mouse 8 0.2 dragon 300 100
#Output: A list of lists, with each list having the name of the animal, and a list of measures.
#For example: [['unicorn', ['120', '190’]],…]

#Task 1: Write an interactive program that asks a use to enter the list
#and then provides the formatted version, using a function for the formatting. 

#Task 2 :Write unit tests for the function. 


"""
This is the "list_list demo formatting" module.

The module supplies one function, make_list_list().  For example,

>>> make_list_list("unicorn 120 190 mouse 8 0.2 dragon 300 1000")
[['unicorn', ['120', '190']], ['mouse', ['8', '0.2']], ['dragon', ['300', '1000']]]

>>> make_list_list("")
[]
"""

#this functions takes a string formatted as repeated animal height weight values and
#returns a list of list that formats the values a submists with [animal, [height, weight]]
def make_list_list(input_text):
    formatted_list = []
    list_elements = input_text.split() #this creates a list where each word or number in the test is an element. 
    new_index = 0 #this index points to the position of the animal currently under consideration
#at the start, it points to 1st animal in the list_elements. 
    while new_index < len(list_elements):
        formatted_list.append([list_elements[new_index], [list_elements[new_index+1], list_elements[new_index+2]]])#here we directly
    #add the new list with the values for the new animal: name, height and weight, at the end of the formatted list.
    new_index +=3#the new_index is now set to the position of the next word in list_element. 
        new_index +=3
    return formatted_list

if __name__ == '__main__':        
    read_input = input('Hello, please enter the list you want to format:') 
    formatted_output = make_list_list(read_input)
    print('this is your formatted list: ', formatted_output)
    #this is running the unit tests
    from doctest import testmod
    doctest.testmod()
