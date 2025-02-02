import numpy as np

grades = np.array([40, 10, 50, 30, 20])
grades.sort() # sort the elements in a ndarray
print(grades)

max_grade = grades.max() # get the max value
print(max_grade)
curve = 100 - max_grade # compute curve
curved_grades = grades + curve # add curve to all grades
print(curved_grades)

# 2 ways to compute the mean
avg_grade = grades.sum()/grades.size # sum / size
print(avg_grade == grades.mean()) # figure out if they are equal

print(grades <= 30) # ndarray supports __le__ "less than or equal to" method
print(grades > 30)  # ndarray supports __gt__ "greater than"          method
