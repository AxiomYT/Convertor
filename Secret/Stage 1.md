#----------------------------------------#
			 # PERCENTAGE #
#----------------------------------------#

DEFINE percentage (Inputting courseworkmark and exammark)
	totalscore is courseworkmark + exammark
	percentage is totalscore * 100 / 150

SEND percentage TO main programme
SEND percentage TO grade function

#----------------------------------------#
			   # GRADE #
#----------------------------------------#

DEFINE grade (Inputting percentage from percentage function)
	gradelocal = percentage

	IF percentage is greater than or equal to 70%
		grade = 1
	ELIF percentage is greater than or equal to 60% and below 69%
		grade = 2
	ELIF percentage is greater than or equal to 50% and below 59% 
		grade = 3
	ELIF percentage is greater than or equal to 45% and below 49%
		grade = 4
	ELIF percentage is Below 45%
		grade = 5
	ELIF percentage is not over 100 or below 0
		DISPLAY "Error in input, please try again."
		exit

RETURN grade TO main programme

#----------------------------------------#
			    # BODY #
#----------------------------------------#

total is 150

RECIEVE courseworkmark AND exammark FROM KEYBOARD

IF courseworkmark is under 60 and over 0, and exammark is under 90 and over 0
	SEND courseworkmark AND exammark TO percentage function
ELIF courseworkmark or exammark is outwith parameters
	print("Entered scores are outwith the maximum allowed marks.\n")
	raise SystemExit

if grade is 1
	DISPLAY "With a score of" totalscore " "you're' performing at an A grade."
if grade is 2
	DISPLAY "With a score of" totalscore " "you're' performing at a B grade."
if grade is 3
	DISPLAY "With a score of" totalscore " "you're' performing at a C grade."
if grade is 4
	DISPLAY "With a score of" totalscore " "you're' performing at a D grade."
if grade is 5
	DISPLAY "With a score of" totalscore " "you're' performing at a D grade."