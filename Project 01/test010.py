def mean(myList):
    if type(myList) == dict:
        the_mean = sum(myList.values()) / len(myList)
    else:
        the_mean = sum(myList) / len(myList)

    return the_mean

student_grades = {"Jim": 10.0, "Tom": 14.5, "Jack": 3.4}
print(mean(student_grades))