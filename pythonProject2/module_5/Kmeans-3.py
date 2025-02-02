import math
f = open("points2-1.txt", "r")
file = f.readlines()
iterations = int(file[0].strip())
N = int(file[1].strip()) # Number of total patients (N = 100)
k = int(file[2].strip()) # Number of clusters/centroids (k = 4)
# print(k)
patients = [] # 96 patients for clustering
clusters = [] # 4 patients as well as 4 centroids
previous_cluster = [] #
centroids = []
# x_values = []
# y_values = []
# distances = []

for n in range(3,len(file)): # get a list patients: 100 patients
    file[n] = file[n].strip('\n')
    file[n] = file[n].split(',')
    patients.append([float(file[n][0]), float(file[n][1])])
# print(patients) # get the patients list

# centroids = [patients[0],patients[1],patients[2],patients[3]] # initialize clusters (nested data structure)
# print(centroids)
for i in range(k): # here you should be careful: use k instead of 4 or 3
    centroids.append(patients[i])

print(f"Initial COVID-19 Patients: {centroids}\n")

patients_cluster = patients[k:]

# initialize clusters and previous cluster with k empty lists
for i in range(k):
    clusters.append([])

for i in range(k):
    previous_cluster.append(0)

iteration = 0

while iteration < iterations:
    # clear the cluster
    for i in range(k):
        clusters[i] = []

    for patient in patients_cluster:
        min_distance = float('inf')
        closest_centroid = -1

# Attention!!! You should be very careful that here you only need to compare the 96 patients instead of 100
        for i in range(k):
            distance = math.sqrt((patient[0]-centroids[i][0])**2+(patient[1]-centroids[i][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_cluster = i

        clusters[closest_cluster].append(patient)

    current_cluster = []
    for i in range(k):
        current_cluster.append(len(clusters[i]))

    if current_cluster == previous_cluster:
        print(f"Iterations to achieve stability: {iteration}\n")
        break
# here I made a big mistake. I should use the copy() to update previous cluster to the current sizes
    previous_cluster = current_cluster.copy()

# update the centroids
    for i in range(k):
        if len(clusters[i]) > 0:
            sum_x1 = 0
            sum_y1 = 0
            for patient in clusters[i]:
                sum_x1 += patient[0]
                sum_y1 += patient[1]
            mean_x1 = (sum_x1/len(clusters[i]))
            mean_y1 = (sum_y1/len(clusters[i]))
            centroids[i]=[mean_x1,mean_y1]

    iteration = iteration + 1

print(f"Final Centroids:\n"
      f"{centroids}\n")
for i in range(k):
    print(f"Number of patients in Cluster {i}: {len(clusters[i])}\n"
          f"{clusters[i]}\n")
