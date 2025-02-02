import math

f = open("points1-1.txt","r")
file = f.readlines()
iterations = int(file[0].strip())
N = int(file[1].strip())
k = int(file[2].strip())

patients = []
clusters = []
previous_cluster = []
centroids = []

for n in range(3,len(file)):
    file[n] = file[n].strip('\n')
    file[n] = file[n].split(',')
    patients.append([float(file[n][0]), float(file[n][1])])

for i in range(k):
    centroids.append(patients[i])

print(f"Initial COVID-19 Patients: {centroids}\n")

patients_cluster = patients[k:]

for i in range(k):
    clusters.append([])

for i in range(k):
    previous_cluster.append(0)

iteration = 0

while iteration < iterations:
    for i in range(k):
        clusters[i] = []

    for patient in patients_cluster:
        min_distance = float('inf')
        closest_centroid = -1

        closest_cluster = []

        for i in range(k):
            distance = math.sqrt((patient[0]-centroids[i][0])**2+(patient[1]-centroids[i][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_centroid = i
        clusters[closest_centroid].append(patient)


    current_cluster = []
    for i in range(k):
        current_cluster.append(len(clusters[i]))

    if current_cluster == previous_cluster:
        print(f"Iterations to achieve stability: {iteration}\n")
        break

    previous_cluster = current_cluster.copy()

    for i in range(k):
        if len(clusters[i]) > 0:
            sum_x1 = 0
            sum_y1 = 0
            for patient in clusters[i]:
                sum_x1 += patient[0]
                sum_y1 += patient[1]
            mean_x1 = (sum_x1/len(clusters[i]))
            mean_y1 = (sum_y1/len(clusters[i]))
            centroids[i]=(mean_x1,mean_y1)
    iteration += 1

print(f"Final Centroids:\n"
      f"{centroids}\n")

# use a for loop to print each cluster
for i in range(k):
    print(f"Number of patients in Cluster {i}: {len(clusters[i])}\n"
          f"{clusters[i]}\n")