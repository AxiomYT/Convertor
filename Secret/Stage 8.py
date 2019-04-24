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

counter = 0

def acounter(counter):
    print(counter)
    
# The percentage function calculates the percentage from both scores added together
def percentage(courseworkmark, exammark):
    totalscore = int(courseworkmark) + int(exammark)
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
        print(contents[0],"- With a percentage score of", round(percentage, 2), "%","You're performing at an A grade. \n")
        counter +=1
    elif output1 == 2:
        print(contents[0],"- With a percentage score of", round(percentage, 2), "%","You're performing at a B grade. \n")
    elif output1 == 3:
        print(contents[0],"- With a percentage score of", round(percentage, 2), "%","You're performing at a C grade. \n")
    elif output1 == 4:
        print(contents[0],"- With a percentage score of", round(percentage, 2), "%","You're performing at a D grade. \n")
    elif output1 == 5:
        print(contents[0],"- With a percentage score of", round(percentage, 2), "%","You're performing at a D grade. \n")

    acounter(counter)
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
x = 0

# Programme begins with the opening of the file
f = open('results.txt',"r")
# Programme then reads said file
fl = f.readlines()
# Programme then closes the file after assigning contents to an array
f.close()
# Repeats until the counter variable (x) is under 15
for x in fl:
# As file is in comma deliminated format, strips commas between variables
    contents = x.split(",")
# Removes new lines from mark contents (without this number is returned as something like 90\n)
    courseworkmark = int(contents[1].strip("\n"))
# Assigns the coursework mark section of the source file to the courseworkmark variable
    exammark = int(contents[2])
# Sends courseworkmark and exammark variables to percentage function
    percentage(int(courseworkmark), exammark)

# This input is then checked to see if it's valid - if it is, it shall continue, on the counterpoise - it shall exit
if int(int(courseworkmark) <= 60) and (int(int(courseworkmark)) >= 0):
    if ((exammark <= 90) and (exammark >= 0)):

# If the user input is within valid parameters - then the programme shall pass both mark scores to the percentage function   
        percentage(int(courseworkmark), exammark)
    else:
        print("Entered scores are outwith the maximum allowed marks.\n")
        raise SystemExit
elif (isnan(int(courseworkmark))):
    print("Entered scores are outwith the maximum allowed marks.\n")
    raise SystemExit
