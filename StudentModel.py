#Student Model

#Sean McCLary
#Jacob Nissley
#Levi Peachey-Stoner

"""
from random import randint
from math import numpy


students = []
studentCount = 100
mean = 75
std = 10

dist = numpy.random.normal(mean,std,studentCount)

for i in range(studentCount):
    student = []
    lower = randint(dist[i] - 5, dist[i] + 5)
    upper = randint(dist[i+1] - 5, dist[i+1] + 5)
    for j in range(classCount ):
        student.append(randint(lower,upper))
    students.append(student)


'''I couldnt get numpy to load on my laptop, and i
didnt test most of this. But hopefully you see what im trying to do
The jist of it is to make a list of x values(in this case 100) with
normally distributed values, which we then use randint to get grades for j amount
of classes and can develop the list of students with a list of grades to rank.
'''
"""


import numpy


students = []
studentCount = 100
classCount = 5
mean = 75
std = 10
class_mean = 75
class_std = 10

skill = numpy.random.normal(mean, std, studentCount)
class_difficulty = numpy.random.normal(class_mean, class_std, classCount)

for i in range(studentCount):
    
    student = []
    
    for j in range(classCount):
        grade = numpy.random.normal(class_difficulty[j], std)
        grade = int(numpy.clip(grade, skill[i], 100))
        student.append(grade)
    students.append(student)


def class_difficulty(students):

    class_count = len(students[0])
    student_count = len(students)
    difficulty_scores = []

    for i in range(class_count):
        
        total_grade = 0
        
        for student in students:
            total_grade += student[i]
        average_grade = total_grade / student_count
        difficulty_scores.append(average_grade)

    return difficulty_scores


def calculate_smarts(students, class_difficulty):

    student_count = len(students)
    smarts_scores = []

    for student in students:
        
        total_performance = 0
        
        for i in range(len(student)):
            performance = student[i] / class_difficulty[i]
            total_performance += performance
        average_performance = total_performance / len(student)
        smarts_scores.append(average_performance)

    return smarts_scores


def calculate_percentile(smarts_scores):

    sorted_smarts_scores = sorted(smarts_scores)

    percentile_ranks = []

    for smarts_score in smarts_scores:
        count_lower = sum(1 for score in sorted_smarts_scores if score <= smarts_score)
        percentile_rank = (count_lower / len(smarts_scores)) * 100
        percentile_ranks.append(percentile_rank)

    return percentile_ranks

def compare(percentile_ranks,students):
    x = []
    for i in range(len(students)):
        x.append([percentile_ranks[i],students[i]])
    return(x)



#print(students)
#print(class_difficulty(students))
percentile_ranks = calculate_percentile(calculate_smarts(students,class_difficulty(students)))
print(compare(percentile_ranks,students))
#print(percentile_ranks)


"""
This works as intended, it generates a student body, along with the classes they attend.
The skill of each student and the difficulty of each class is normally distributed.
It using only the data generated it creates averages for each of the classes and compares
the scores of each student to this average to find how well they did in it. Using this data
the students could be assigned a percentile on how well they did compared to their classmates
taking into accound how difficult each class was.

We did not get around to finding how accurite it would be if the data was more limited,
if we were only given the letter grade, with or without + and -.
In order to find if you could accuritely assess people you would compare the calculated
percentile to the percentile we calculated above, a certain amount of error would be acceptable
but if there was a significant difference we would be able to say that this would not be
enough information to fairly assess people.
"""
