import itertools
from matplotlib import pyplot as plt
from point import Point

def find_collinear_points(points): # Find all sets of 4 collinear points from a given list of points

    collinear_sets = [] # Initialize collinear points
    for p1, p2, p3, p4 in itertools.combinations(points, 4):
        slope1 = p1.slope_to(p2)
        slope2 = p2.slope_to(p3)
        slope3 = p3.slope_to(p4)
        if slope1 == slope2 == slope3: # Check if all slopes are equal (points are collinear)
            collinear_sets.append([p1, p2, p3, p4]) # Add the collinear set
    return collinear_sets

def plot_points(points, collinear_sets):
# Plot all points and lines connecting sets of collinear points.
    x_coords = [p.x for p in points]
    y_coords = [p.y for p in points]
    plt.plot(x_coords, y_coords, "ro", label="Points") # Plot all points as red circles

    for collinear_set in collinear_sets: # Plot each collinear set as a line
        x_coords = [p.x for p in collinear_set]
        y_coords = [p.y for p in collinear_set]
        f_points = ", ".join(f"({p.x}, {p.y})" for p in collinear_set) # f_points is the correct format of collinear_set
        plt.plot(x_coords, y_coords, label=f"Line: {f_points}")
# Configure the plot
    plt.legend()
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Collinear Points Visualization")
    plt.grid(True)
    plt.show()

def main(input_file): # Read input from a file, find collinear points, and visualize the results.

    with open(input_file, "r") as file:
        lines = file.readlines()
        points = []
        for line in lines[1:]: # skip the first line
            x, y = map(float, line.split())
            points.append(Point(x, y))

    collinear_sets = find_collinear_points(points) # Find all collinear sets of 4 points

    for collinear_set in collinear_sets:
        f_points = ", ".join(f"({p.x}, {p.y})" for p in collinear_set) # f_points is the correct format of collinear_set
        print(f"Line: {f_points}")

    plot_points(points, collinear_sets)

if __name__ == "__main__":
    main("points1.txt")
