#this program solves the IFB104 week 5 example of lists of lists in 4 different manners. There are many more ways this can be solved!
#the problem is as follows:
#Input: on a single line, a list of animals is provided.
#For each animal, its name is provided, followed by its height (in cm) and weight (in kg).
#The list is provided on a single line, with values separated by spaces. For example:
#unicorn 120 190 mouse 8 0.2 dragon 300 100
#Output: A list of lists, with each list having the name of the animal, and a list of measures.
#For example: [['unicorn', ['120', '190’]],…]

#this version of the program is not interactive, so the example text is copied into the input_text variable. 

input_text = "unicorn 120 190 mouse 8 0.2 dragon 300 1000" 
list_elements = input_text.split() #this creates a list where each word or number in the test is an element. 

#Approach 1: the program processes each word/number in the list one by one,
#it uses the indices to go through the elements, and does a different thing depending on the value of the index. 
formatted_list = []
for element_index in range(len(list_elements)): #at each iteration, element_index has a number 1 greated than the previous. 
    if element_index%3 == 0: #every 3 element in the list is an animal, so if the index is divisible by 3, the element is an animal
        formatted_list.append([list_elements[element_index]])#this adds a new list at the end of the formatted_list,
        #which only contains the value of the element at the corresponding index in list_element
    elif element_index%3 == 1:
        formatted_list[-1].append([list_elements[element_index]])#this adds a new element to the last list in the formatted_list
        #the new element is also a list, and it contains the value of the element at the corresponding index in list_element
    else:
        formatted_list[-1][1].append(list_elements[element_index])#this adds a new element to the second element of the last list
        #in the formatted list: this second element is also a list. The new element the value of the element at the corresponding
        #index in list_element
print (formatted_list)

#Approach 2: the program processes each word in the list one by one and
#it uses the indices to go through the words.
#it uses a variable (new_index) to calculate the indices for the word and measures for each word. 
formatted_list = []
new_index = 0 #this index points to the position of the animal currently under consideration
#at the start, it points to 1st animal in the list_elements. 
for counter in range(len(list_elements)//3): #counter is not used here, it only guarantees that there are as
    #many iterations as there are words (animals). Every 3 elements in the list is a word, so the total number
    #is the length of the list divided by 3
    formatted_list.append([list_elements[new_index], [list_elements[new_index+1], list_elements[new_index+2]]])#here we directly
    #add the new list with the values for the new animal: name, height and weight, at the end of the formatted list.
    #They are respectively at the current and 2 following positions
    new_index +=3 #the new_index is now set to the position of the next word in list_element. 
print (formatted_list)

#Approach 3: this approach is similar to Approach 2, but it uses the index pointing to the current animal
#to determine iterations rather than fixing the number. It is more elegant, but heavier to process
#because of comparisons at every iteration. 
formatted_list = []
new_index = 0 #this index points to the position of the animal currently under consideration
#at the start, it points to 1st animal in the list_elements. 
while new_index < len(list_elements):#the loop continues so long as the current position is still within the list. 
    formatted_list.append([list_elements[new_index], [list_elements[new_index+1], list_elements[new_index+2]]])#here we directly
    #add the new list with the values for the new animal: name, height and weight, at the end of the formatted list.
    new_index +=3#the new_index is now set to the position of the next word in list_element. 
print (formatted_list)

#Approach 4: this approach uses a regular expression to first create a list of all the triplets "animal height weight"
#then processes them one by one. Each is split and the 3 elements of the resulting list directly added as a new element
#to the formatted_list
from re import findall
formatted_list = []
list_elements = findall('[a-z]+ [0-9\.]+ [0-9\.]+',input_text) #creates a list of all the triplets "animal height weight"
for triplet in list_elements:
    elements=triplet.split() #creates a list with [animal, height, weight] at each iteration
    formatted_list.append([elements[0], [elements[1], elements[2]]]) #directly adds the new list with the 3 elements
    #as a new element at the end of the formatted_list
print (formatted_list)
