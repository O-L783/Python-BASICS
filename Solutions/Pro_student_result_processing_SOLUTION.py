#---------------------------------------------------------
#
# Student results
#
# Below is a series of operations to perform on calculating
# student's results
#---------------------------------------------------------
#

student_results = 'Tom 7 9 11, Jun 12 6 5, Rhianna 8 11 8, Ariana 5 12 7, Lee 8 10 5, Brianna 9 9 10, Chris 6 5 7, Stu 7 6 6'
formatted_results = [['Tom', [7, 9, 11]], ['Jun', [12, 6, 5]],
                     ['Rhianna', [8, 11, 8]], ['Ariana', [5, 12, 7]],
                     ['Lee', [8, 10, 5]], ['Brianna', [9, 9, 10]],
                     ['Chris', [6, 5, 7]], ['Stu', [7, 6, 6]]]                    
                    
##### Task 1:
# Function that given a student list as a string, formats
# into a python list
# Parameters: A string that contains information about students
#             and their results.  Note that the string is of the
#             format - student name, followed by 3 numbers.
# Returns:    A list of lists of students and their corresponding
#             test results
def make_student_list(student_list = ""):
    """ 
    >>> make_student_list(student_results)
    [['Tom', [7, 9, 11]], ['Jun', [12, 6, 5]], ['Rhianna', [8, 11, 8]], ['Ariana', [5, 12, 7]], ['Lee', [8, 10, 5]], ['Brianna', [9, 9, 10]], ['Chris', [6, 5, 7]], ['Stu', [7, 6, 6]]]
    >>> make_student_list("")
    []
    >>> make_student_list()
    []
    """

    if student_list == "":
        return []
    student_info = []
    # split the results based on the comma separator
    results = student_list.split(",")
    for line in results:
        # remove any leading or trailing spaces and split into
        # separate items
        entries = (line.strip()).split(" ")
        student_info.append([entries[0], [int(entries[1]), \
                       int(entries[2]), int(entries[3])]])
        
    return student_info


##### Task 2:
# Function that given a formatted student list and a student
# name, calculates the total marks for that student
# Parameters: 
#               a formatted student list as a list of lists, such as returned
#                       by the make_student_list function above
#               a string, representing the student's name
# Returns:      A number representing the total marks for that student or -1
#               if not present
def calculate_total_grade(formatted_student_list = [], name = ""):
    """ 
    >>> calculate_total_grade(formatted_results, "Tom")
    27
    >>> calculate_total_grade(formatted_results, "Brianna")
    28
    >>> calculate_total_grade(formatted_results, "John")
    -1
    >>> calculate_total_grade(formatted_results, "")
    -1
    >>> calculate_total_grade(formatted_results)
    -1
    >>> calculate_total_grade([])
    -1
    >>> calculate_total_grade()
    -1
    """
    
    if formatted_student_list == [] or name == "":
        return -1

    for entry in formatted_student_list:
        # Found a match
        if entry[0] == name:
            total = entry[1][0] + entry[1][1] + entry[1][2]
            return total
    # No matches found
    return -1
    
##### Task 3:
# Function that given a formatted student list returns the name of the student
# with the highest total score
# Parameters:   A formatted student list as a list of lists, such as returned
#               by the make_student_list function above
# Returns:      A name representing the student with the highest total marks
def highest_scoring_student(formatted_student_list = []):
    """ 
    >>> highest_scoring_student(formatted_results)
    'Brianna'
    >>> highest_scoring_student([])
    ''
    >>> highest_scoring_student()
    ''
    """
    if formatted_student_list == []:
        return ""
    highest_score = -1
    name = ""
    for entry in formatted_student_list:
        score = entry[1][0] + entry[1][1] + entry[1][2]
        # The highest score so far
        if score > highest_score:
            highest_score = score
            name = entry[0]
    return name


    
##### Task 4:
# Function that retrieves a list of any at-risk students.  At-risk students
# are determined to be any student that has a mark of 6 or less in any
# assessment
# Parameters:   A formatted student list as a list of lists, such as returned
#               by the make_student_list function above
# Returns:      A list of names of students determined to be "at-risk"
def at_risk_students(formatted_student_list = []):
    """ 
    >>> at_risk_students(formatted_results)
    ['Jun', 'Ariana', 'Lee', 'Chris', 'Stu']
    >>> at_risk_students([])
    []
    >>> at_risk_students()
    []
    """
    if formatted_student_list == []:
        return []
    
    at_risk_score = 6
    names = []
    for entry in formatted_student_list:
        # Of the three tests are any deemed at-risk
        if entry[1][0] <= at_risk_score or \
           entry[1][1] <= at_risk_score or \
           entry[1][2] <= at_risk_score:
            names.append(entry[0])
    return names


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
