f = open("points_oh.txt","r")
file = f.readlines() # here file is a list, list has no strip() or split()
# print(type(file))

points = []
n = []
slope = set()
p = 0.0

for line in file: # line is the content of the file list. line is string
    line = line.strip() # you can strip the string
    line = line.split(",") # you can split the string, and make multiple lists
#     print(line)  # here line you get multiple lists with two strings in it
# print(type(line[0])) # you can see the 0 line in the list is a string
#     print(line)
    points.append((float(line[0]),float(line[1]))) # Here you should pay more attention
print(points)

for i in range(len(points)):
    m = (points[i][0]+1,points[i][1]) # here you get the content: tuple of number
    n.append(m) # for list n, we use append to form a list
    # print(m)
print(n)

for i in range(1,len(n)): # here you should add a 1, since it's from the second i
    q=((n[0][1]-n[i][1]) / (n[0][0]-n[i][0])) # careful about the parenthesis
    # print(n[i])
    slope.add(q) # slope.add(q) for the slope=set() to form a set
    # print(q)
    # print(type(q))
print(slope)
for i in range(len(slope)):
    # print(slope[0]) # set is not subscriptable
    if q > p:
        p = q
print(q)
print(f"\n\nMax.slope: {q}")
print(f"There were {len(slope)} distinct slopes: {slope}")