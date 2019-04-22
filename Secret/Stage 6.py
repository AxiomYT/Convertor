#----------------------------------------#
         # STANDARD ALGORITHIMS #
#----------------------------------------#

# Finds the entry in the array that is largest and prints it
def find_max(number_list):
    largest = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] > largest:
            largest = number_list[index]
    print("The largest value is", largest)

# Finds the smallest entry in the array and then prints it
def find_min(number_list):
    smallest = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] < smallest:
            smallest = number_list[index]
    print("The smallest value is", smallest)

# Finds out how many times a certain value has been entered into the array, then prints it.
def count_occurrences(value, value_list):
    count = 0
    for index in range(len(value_list)):
        if value_list[index] == value:
            count += 1
    print(value, "appears in the list", count, "time(s)")

# Finds the location in the array where a requested number is and then prints whether it found it or not and where.
def linear_search(value, value_list):
    position = 0
    found = False
    for index in range(len(value_list)):
        if value_list[index] == value:
            position = index
            found = True
        if found:
            break
    if found:
        print(value, "was found at index", position)
    else:
        print(value, "was not found")

#----------------------------------------#
       # PERCENTAGE & TOTAL SCORE #
#----------------------------------------#

# The percentage function calculates the percentage from both scores added together
def percentage(courseworkmark, exammark):
    totalscore = courseworkmark + exammark
    percentage1 = (totalscore / 150 * 100)

# Returns final percentage to the grade function
    grade(percentage1)
    return totalscore, percentage1

#----------------------------------------#
	       # GRADE #
#----------------------------------------#

# The grade function calculates the grade from percentage from the previous percentage function
def grade(percentage):

    grade1 = 0
    
    if ((percentage >= 70) and (percentage <= 100)):
        grade1 = 1
    elif (percentage >= 60) and (percentage <= 69.9):
        grade1 = 2
    elif (percentage >= 50) and (percentage <= 59.9):
        grade1 = 3
    elif (percentage >= 45) and (percentage <= 49.9):
        grade1 = 4
    elif ((percentage < 45) and (percentage >= 0)):
        grade1 = 5
    elif (percentage != 100) or (percentage < 0):
        print(percentage)
        print("Error in input, please try again.")
        raise SystemExit
# Returns grade in numbers between 1 - 5 to output function
    output(grade1, totalscore, percentage)

#----------------------------------------#
	       # OUTPUT #
#----------------------------------------#

# Recieves grade and dignifies a value to each number recieved from the grade function     
def output(output1, totalscore, percentage):

# Outputs final result and then exits
    if output1 == 1:
        print("\nWith a percentage score of", round(percentage, 2), "%","You're performing at an A grade. \n")
        raise SystemExit
    elif output1 == 2:
        print("\nWith a percentage score of", round(percentage, 2), "%","You're performing at a B grade. \n")
        raise SystemExit
    elif output1 == 3:
        print("\nWith a percentage score of", round(percentage, 2), "%","You're performing at a C grade. \n")
        raise SystemExit
    elif output1 == 4:
        print("\nWith a percentage score of", round(percentage, 2), "%","You're performing at a D grade. \n")
        raise SystemExit
    elif output1 == 5:
        print("\nWith a percentage score of", round(percentage, 2), "%","You're performing at a D grade. \n")
        raise SystemExit

#----------------------------------------#
		# BODY #
#----------------------------------------#

# Declaring Variables
total = 150
grade2 = 0
courseworkmark = 0
exammark = 0
output1 = 0
grade1 = 0
totalscore = 0
percentage1 = 0.0

# Programme begins asing for user information
courseworkmark = int(input("Enter your mark for your coursework \n"))
exammark = int(input("Enter your mark for your Examination \n"))

# This input is then checked to see if it's valid - if it is, it shall continue, on the counterpoise - it shall exit
if ((courseworkmark <= 60) and (courseworkmark >= 0)):
    if ((exammark <= 90) and (exammark >= 0)):

# If the user input is within valid parameters - then the programme shall pass both mark scores to the percentage function   
        percentage(courseworkmark, exammark)
    else:
        print("Entered scores are outwith the maximum allowed marks.\n")
        raise SystemExit
elif (isnan(courseworkmark)):
    print("Entered scores are outwith the maximum allowed marks.\n")
    raise SystemExit
