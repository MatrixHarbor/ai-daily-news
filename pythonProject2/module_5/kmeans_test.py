import math
f = open("points1-1.txt", "r")
file = f.readlines()
Iteration = file[0] #
N = file[1] # Number of total patients (N = 100)
k = file[2] # Number of clusters/centroids (k = 4)
# print(k)
patients = [] # 96 patients for clustering
clusters = [] # 4 patients as well as 4 centroids
previous = [] #
centroids = []

# for n in range(3,7):
#     file[n] = file[n].strip('\n')
#     file[n] = file[n].split(',')
#     clusters.append((int(file[0]),int(file[1])))
#     # print(file[n])
# # print(clusters[0])
# print(clusters)
# for initial_patient in range(len(clusters)):
#     x1 = clusters[0][0]
#     y1 = clusters[0][1]
#     x2 = clusters[1][0]
#     y2 = clusters[1][1]

for n in range(7,len(file)):
    file[n] = file[n].strip('\n')
    file[n] = file[n].split(',')
    print(file[n])
# print(patients)

# for patient in range(len(patients)):
#     x0 = patients[patient][0]
#     y0 = patients[patient][1]
#     distance1 = ((int.x0-int.x1)**2 + (y0-y1)**2)**0.5
#     print(distance1)