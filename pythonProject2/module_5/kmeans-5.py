import math

from module_5.kmeans import patients, centroids

f = open("points1-1.txt", "r")

file = f.readlines()
iterations = int(file[0].strip())
N = int(file[1].strip())
k = int(file[2].strip())

patients = []
clusters = []
previous_cluster = []
centroids = []
