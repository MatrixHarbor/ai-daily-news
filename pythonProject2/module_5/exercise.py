from os.path import split
max_slope = 0.0
points = []
slope = set()
f = open("points_oh.txt", "r")
file = f.readlines()
for line in file:
    line = line.strip()
    line = line.split(",")
    points.append((float(line[0]),float(line[1])))
print(points)

for i in range(len(points)):
    points[i] = (points[i][0]+1.0, points[i][1] )
print(points)

for i in range(1,len(points)):
    m = ( (points[0][1]-points[i][1]) / (points[0][0]-points[i][0]))
    print(m)
    # print(type(m))
    slope.add(m)
    if m > max_slope:
        max_slope = m
print(f"\n\nMax.slope: {max_slope}")
print(f"There were {len(slope)} distinct slopes: {slope}")
# print(type(slope))
    # print(points[i][0])
    # print(type(points[i]))
# points = []
# for line in range(len(file)):
    # line = line.strip()
    # line = line.split(",")
    # point = (float(line[0]), float(line[1]))
    # points.append(point)
    # print(line[0])

# print(type(line))
# print(len(line))

# print(points)