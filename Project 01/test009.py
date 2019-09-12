#defining a list
student_grades = [9.0, 8.5, 5.4]

#making a function to calculate the mean value of a list (sent as parameter)
def mean(theList):
    print("Calculating the mean of the list!")
    the_mean = sum(theList) / len(theList)
    return the_mean

#printing the result of calling the mean function previously created
print(mean(student_grades))