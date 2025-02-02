import math
f = open("points1-1.txt", "r") # you can change file between points1-1.txt and points2-1.txt
# f = open("points2-1.txt", "r")
file = f.readlines()
iterations = int(file[0].strip())
N = int(file[1].strip()) # Number of total patients (N = 100)
k = int(file[2].strip()) # Number of clusters/centroids (k = 4)
# print(k)
patients = [] # 96 patients for clustering
clusters = [] # 4 patients as well as 4 centroids
previous_cluster = [] #
centroids = []


for n in range(3,len(file)): # get a list patients: 100 patients
    file[n] = file[n].strip('\n')
    file[n] = file[n].split(',')
    patients.append([float(file[n][0]), float(file[n][1])])
# print(patients) # get the patients list

# centroids = [patients[0],patients[1],patients[2],patients[3]] # initialize centroids (nested data structure)
# print(centroids)
for i in range(k): # here you should be careful: use k instead of 4 or 3
    centroids.append(patients[i]) # initialize centroids

print(f"Initial COVID-19 Patients: {centroids}\n")

patients_cluster = patients[k:] # careful that you only need to compare other patients

# initialize clusters and previous cluster with k empty lists
for i in range(k):
    clusters.append([])

for i in range(k):
    previous_cluster.append(0)

iteration = 0 # initialize iteration

while iteration < iterations:
    # clear the cluster
    for i in range(k):
        clusters[i] = []
    # assign patients to the closest centroid
    for patient in patients_cluster:
        min_distance = float('inf') # start from a very large value
        closest_centroid = -1

# Attention!!! You should be very careful that here you only need to compare the 96 patients instead of 100
        closest_cluster = []
        # calculate the distance using Euclidean distance and find the closet centroid
        for i in range(k):
            distance = math.sqrt((patient[0]-centroids[i][0])**2+(patient[1]-centroids[i][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_cluster = i
        # append the patient to the correct cluster (closest one)
        clusters[closest_cluster].append(patient)

    # calculate the current cluster sizes
    current_cluster = []
    for i in range(k): # attention: use for loop to represent k clusters
        current_cluster.append(len(clusters[i]))
    # check the convergence: whether the cluster is still changing or not
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

# use a for loop to print each cluster
for i in range(k):
    print(f"Number of patients in Cluster {i}: {len(clusters[i])}\n"
          f"{clusters[i]}\n")
