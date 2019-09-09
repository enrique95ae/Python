student_scores_list = [9.9, 9.0, 3.4]
student_scores_dictionary = {"Jack": 9.9, "John": 9.0, "Jim": 3.4}


##calculating the average grade in the list
mysum = sum(student_scores_list)
num_of_students = len(student_scores_list)
average = mysum / num_of_students

print(average)


##calculating the average grade in the dictionary
mysum = sum(student_scores_dictionary.values())
num_of_students = len(student_scores_dictionary)
average = mysum / num_of_students

print(average)