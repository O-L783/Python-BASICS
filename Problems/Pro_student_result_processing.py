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

    pass

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
    
    pass

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

    pass

    
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

    pass

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print(testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))
