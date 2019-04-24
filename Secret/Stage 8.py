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

def acounter(counter):
    print(counter)
    
# The percentage function calculates the percentage from both scores added together
def percentage(courseworkmark, exammark):
    percentage1 = 0
    totalscore = int(courseworkmark) + int(exammark)
    percentage1 = ((totalscore / 150) * (100))
# Returns final percentage to the grade function
    grade(percentage1)

#----------------------------------------#
	       # GRADE #
#----------------------------------------#

# The grade function calculates the grade from percentage from the previous percentage function
def grade(percentage1):
    grade1 = 0
    
    if ((percentage1 >= 70) and (percentage1 <= 100)):
        grade1 = 1
    elif (percentage1 >= 60) and (percentage1 <= 69.9):
        grade1 = 2
    elif (percentage1 >= 50) and (percentage1 <= 59.9):
        grade1 = 3
    elif (percentage1 >= 45) and (percentage1 <= 49.9):
        grade1 = 4
    elif ((percentage1 < 45) and (percentage1 >= 0)):
        grade1 = 5
    elif (percentage1 != 100) or (percentage1 < 0):
        print(percentage1)
        print("Error in input, please try again.")
        raise SystemExit
        acounter(counter)
# Returns grade in numbers between 1 - 5 to output function
    output(grade1, totalscore, percentage1)

#----------------------------------------#
	       # OUTPUT #
#----------------------------------------#
# Recieves grade and dignifies a value to each number recieved from the grade function     
def output(output1, totalscore, percentage1):
    counter = 0
# Outputs final result and then exits
    if output1 == 1:
        print("{} - With a percentage score of {}% You're performing at an A grade. \n".format(contents[0], round(percentage1, 2)))
        counter += 1
        print(counter)

        if counter == 4:
            print("sans")
        
        acounter(counter)
    elif output1 == 2:
        print("{} - With a percentage score of {}% You're performing at an B grade. \n".format(contents[0], round(percentage1, 2)))
    elif output1 == 3:
        print("{} - With a percentage score of {}% You're performing at an C grade. \n".format(contents[0], round(percentage1, 2)))
    elif output1 == 4:
        print("{} - With a percentage score of {}% You're performing at an D grade. \n".format(contents[0], round(percentage1, 2)))
    elif output1 == 5:
        print("{} - With a percentage score of {}% You're performing at an F grade. \n".format(contents[0], round(percentage1, 2)))

    return counter

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
percentage1 = 0
x = 0

# Programme begins with the opening of the file
f = open('results.txt',"r")
# Programme then reads said file
fl = f.readlines()
# Programme then closes the file after assigning contents to an array
f.close()
# Repeats until all lines are read
for x in fl:
# As file is in comma deliminated format, strips commas between variables
    contents = x.strip("'")
    contents = x.strip("\n")
    contents = x.split(",")
# Removes new lines from mark contents (without this number is returned as something like 90\n)
    courseworkmark = int(contents[2].strip("\n"))
# Assigns the coursework mark section of the source file to the courseworkmark variable
    exammark = int(contents[2])
# Sends courseworkmark and exammark variables to percentage function
    percentage(int(courseworkmark), int(exammark))

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
