import itertools
import matplotlib.pyplot as plt
from point import Point


def find_collinear_points(points):
    """
    Find all sets of exactly 4 collinear points using a brute-force approach.
    """
    collinear_sets = []
    for p1, p2, p3, p4 in itertools.combinations(points, 4):  # Generate all 4-point combinations
        slope1 = p1.slope_to(p2)
        slope2 = p2.slope_to(p3)
        slope3 = p3.slope_to(p4)
        if slope1 == slope2 == slope3:  # Check if slopes are the same
            collinear_sets.append([p1, p2, p3, p4])
    return collinear_sets


def plot_points(points, collinear_sets):
    """
    Visualize the points and the lines connecting the collinear sets using PyPlot.
    """
    # Plot all points as red circles
    x_coords = [p.x for p in points]
    y_coords = [p.y for p in points]
    plt.plot(x_coords, y_coords, "ro", label="Points")

    # Plot lines for collinear sets
    for collinear_set in collinear_sets:
        x_coords = [p.x for p in collinear_set]
        y_coords = [p.y for p in collinear_set]
        plt.plot(x_coords, y_coords, label=f"Line: {collinear_set}")

    plt.legend()
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Collinear Points Visualization")
    plt.grid(True)
    plt.show()


def main(input_file):
    """
    Main function to read points, find collinear sets, and visualize them.
    """
    # Read input file
    with open(input_file, "r") as file:
        lines = file.readlines()
        points = []
        for line in lines[1:]:  # Skip the first line (number of points)
            x, y = map(float, line.split())
            points.append(Point(x, y))

    # Find collinear points
    collinear_sets = find_collinear_points(points)

    # Print results
    print(f"Input File: {input_file}")
    for collinear_set in collinear_sets:
        print(f"Line: {collinear_set}")

    # Visualize results
    plot_points(points, collinear_sets)


if __name__ == "__main__":
    # Replace 'points1.txt' with your input file
    main("points2.txt")