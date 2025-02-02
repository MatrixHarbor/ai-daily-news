max_slope = 0.0
points = []
slopes = set()
# open points.txt for reading
f = open("points_oh.txt", "r")
for line in f.readlines():
# remove newlines, split on commas
    point = line.strip().split(",")
# use a tuple to store the numeric point values (x, y)
    points.append((float(point[0]), float(point[1])))
# print points for verification
print(points)
# update x value for each point
# MUST create new tuples because they are immutable
for i in range(len(points)):
    points[i] = (points[i][0] + 1.0, points[i][1])
# print points for verification
print(points)
# compute slope between first point and all other points
for i in range(1, len(points)):
# compute the slope: (y-y')/(x-x')
    m = (points[0][1] - points[i][1]) / (points[0][0] - points[i][0])
    # print the slope
    print(m)
    # add the new slope to a set
    slopes.add(m)
    # update max slope if new slope is greater than previous max
    if m > max_slope:
        max_slope = m
# print outputs
print(f"\n\nMax. slope: {max_slope}")
print(f"There were {len(slopes)} distinct slopes: {slopes}")