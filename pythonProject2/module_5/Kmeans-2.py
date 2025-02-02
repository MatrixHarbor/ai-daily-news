import math
f = open("points1-1.txt", "r")
file = f.readlines()
iterations = int(file[0].strip())
N = int(file[1].strip()) # Number of total patients (N = 100)
k = int(file[2].strip()) # Number of clusters/centroids (k = 4)
# print(k)
patients = [] # 96 patients for clustering
clusters = [] # 4 patients as well as 4 centroids
previous_cluster = [0,0,0,0] #
centroids = []
x_values = []
y_values = []
distances = []

for n in range(3,len(file)): # get a list patients: 100 patients
    file[n] = file[n].strip('\n')
    file[n] = file[n].split(',')
    patients.append([float(file[n][0]), float(file[n][1])])
# print(patients) # get the patients list

# centroids = [patients[0],patients[1],patients[2],patients[3]] # initialize clusters (nested data structure)
# print(centroids)
for i in range(k): # here you should be careful: use k instead of 4 or 3
    centroids.append(patients[i])
# centroids.append(patients[0])
# centroids.append(patients[1])
# centroids.append(patients[2])
# centroids.append(patients[3])
print(f"Initial COVID-19 Patients: {centroids}\n")

patients_cluster = patients[k:]
# here I made a big mistake, I should use 96 patients, not all 100
# for i in range(len(patients_cluster)):
#     patient = patients_cluster[i]
# previous_cluster.append(0)
# previous_cluster.append(0)
# previous_cluster.append(0)
# previous_cluster.append(0)
# print(previous)
for i in range(k):
    clusters.append([])

iteration = 0
# while interation < Iterations: # while loop
#     clusters[0] = [] # clear each cluster
#     clusters[1] = []
#     clusters[2] = []
#     clusters[3] = []


while iteration < iterations:
    # clear the cluster
    clusters[0] = []
    clusters[1] = []
    clusters[2] = []
    clusters[3] = []

# Attention!!! You should be very careful that here you only need to compare the 96 patients instead of 100
    for i in range(len(patients_cluster)):
        patient = patients_cluster[i]
        # print(patient)
        distance1 = math.sqrt((patient[0]-centroids[0][0])**2+(patient[1]-centroids[0][1])**2)
        # print(distance1)
        distance2 = math.sqrt((patient[0]-centroids[1][0])**2+(patient[1]-centroids[1][1])**2)
        distance3 = math.sqrt((patient[0]-centroids[2][0])**2+(patient[1]-centroids[2][1])**2)
        distance4 = math.sqrt((patient[0]-centroids[3][0])**2+(patient[1]-centroids[3][1])**2)

        min_distance = min(distance1,distance2,distance3,distance4)
        if min_distance == distance1:
            clusters[0].append(patient)
        elif min_distance == distance2:
            clusters[1].append(patient)
        elif min_distance == distance3:
            clusters[2].append(patient)
        else:
            clusters[3].append(patient)
    # check if there are any points switching clusters
    current_cluster1 = len(clusters[0])
    current_cluster2 = len(clusters[1])
    current_cluster3 = len(clusters[2])
    current_cluster4 = len(clusters[3])

    if current_cluster1 == previous_cluster[0] and current_cluster2 == previous_cluster[1] and current_cluster3 == previous_cluster[2] and current_cluster4 == previous_cluster[3]:
        print(f"Iterations to achieve stability: {iteration}\n")
        break
    # for i in range(4):
    #     if len(clusters[i]) > 0:

    previous_cluster[0] = current_cluster1
    previous_cluster[1] = current_cluster2
    previous_cluster[2] = current_cluster3
    previous_cluster[3] = current_cluster4 # here you should update the previous cluster

    # calculate cluster mean x/y and update centroids for each cluster
    if len(clusters[0]) > 0:
        sum_x1 = 0
        sum_y1 = 0
        for patient in clusters[0]:
            sum_x1 += patient[0]
            sum_y1 += patient[1]
        mean_x1 = (sum_x1/len(clusters[0]))
        mean_y1 = (sum_y1/len(clusters[0]))
        centroids[0]=[mean_x1,mean_y1]
    if len(clusters[1]) > 0:
        sum_x2 = 0
        sum_y2 = 0
        for patient in clusters[1]:
            sum_x2 += patient[0]
            sum_y2 += patient[1]
        mean_x2 = (sum_x2/len(clusters[1]))
        mean_y2 = (sum_y2/len(clusters[1]))
        centroids[1]=[mean_x2,mean_y2]
    if len(clusters[2]) > 0:
        sum_x3 = 0
        sum_y3 = 0
        for patient in clusters[2]:
            sum_x3 += patient[0]
            sum_y3 += patient[1]
        mean_x3 = (sum_x3/len(clusters[2]))
        mean_y3 = (sum_y3/len(clusters[2]))
        centroids[2]=[mean_x3,mean_y3]
    if len(clusters[3]) > 0:
        sum_x4 = 0
        sum_y4 = 0
        for patient in clusters[3]:
            sum_x4 += patient[0]
            sum_y4 += patient[1]
        mean_x4 = (sum_x4/len(clusters[3]))
        mean_y4 = (sum_y4/len(clusters[3]))
        centroids[3]=[mean_x4,mean_y4]

    iteration = iteration + 1

print(f"Final Centroids:\n"
      f"{centroids[0]}\n"
      f"{centroids[1]}\n"
      f"{centroids[2]}\n"
      f"{centroids[3]}\n")

print(f"Number of patients in Cluster 0: {current_cluster1}\n"
      f"{clusters[0]}\n")
print(f"Number of patients in Cluster 1: {current_cluster2}\n"
      f"{clusters[1]}\n")
print(f"Number of patients in Cluster 2: {current_cluster3}\n"
      f"{clusters[2]}\n")
print(f"Number of patients in Cluster 3: {current_cluster4}\n"
      f"{clusters[3]}")
# for i in range(len(patients)):
#     patients[i] = [float(patients[i][0]), float(patients[i][1])]

# for cluster in clusters:
#     x_values.append(int(cluster[0])) # make cluster[0] a integer so that we can sum
#     y_values.append(int(cluster[1]))
#     mean_x = sum(x_values) / len(cluster)
#     mean_y = sum(y_values) / len(cluster)
#     centroids.append([mean_x,mean_y])
# print(centroids)

# for iteration in range(50):
#     for patient in patients:
#         distance = math.sqrt((patient[0]-cluster[0])**2 + (patient[1]-cluster[1])**2)
#         distances.append(distance)
#     print(distances)