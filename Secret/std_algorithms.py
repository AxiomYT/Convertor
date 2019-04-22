'''
    Here are 4 standard algorithm functions to include
    in your solution.
    The code is not commented, you will need to add
    internal comments to explain how they work.
    
    Aurelien Ammeloot, Fife College, February 2017
'''

# First algorithm
def find_max(number_list):
    largest = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] > largest:
            largest = number_list[index]
    print("The largest value is", largest)

# Second algorithm
def find_min(number_list):
    smallest = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] < smallest:
            smallest = number_list[index]
    print("The smallest value is", smallest)

# Third algorithm
def count_occurrences(value, value_list):
    count = 0
    for index in range(len(value_list)):
        if value_list[index] == value:
            count += 1
    print(value, "appears in the list", count, "time(s)")

# Fourth algorithm
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

# End of standard algorithms

'''
    The code below is just a main function and additional
    boilerplate I added for testing purposes of testing.
    You may ignore it for your assessment.
    However if you run this script you can see the
    fuctions are working.
'''

def test():
    find_max([5, 7, 10, 3, 2])
    find_min([5, 7, 10, 3, 2])
    count_occurrences("Aurelien", ["Aurelien", "Fiona",
                                   "Jim", "Stewart",
                                   "Aurelien"])
    count_occurrences(16, [16, 18, 20, 19, 16, 20, 32, 16])
    linear_search("Jim", ["Aurelien", "Fiona",
                                   "Jim", "Stewart",
                                   "Aurelien"])
    linear_search(19, [16, 18, 20, 19, 16, 20, 32, 16])

if __name__ == "__main__":
    test()

