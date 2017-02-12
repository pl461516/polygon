import sys

import math

def get_area(vertices):
    """
    Gets area of a polygon described by list of vertices
    using "shoelace" algorithm.

    :param vertices: List of 2-dimensional points - (x,y) tuples.
    :return: Area of a polygon
    """
    area = 0.0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def get_list_of_points(coordinates):
    """
    Transforms list of numbers into
    list of pairs of numbers (tuples)

    :param coordinates: List of coordinates values
    :return: List of pairs.
    """
    vertices = []
    for i in range(0, len(coordinates), 2):
        vertices.append((coordinates[i], coordinates[i + 1]))
    return vertices

def sort_vertices(vertices):
    """
    Sorts all vertices in counter-clockwise order.

    :param vertices: List of vertices
    :return: Sorted list of vertices
    """
    n = len(vertices)
    center_x = float(sum(x for x, y in vertices)) / n
    center_y = float(sum(y for x, y in vertices)) / n
    corners_with_angles = []
    for x, y in vertices:
        angle = (math.atan2(y - center_y, x - center_x) + 2.0 * math.pi) % (2.0 * math.pi)
        corners_with_angles.append((x, y, angle))
    corners_with_angles.sort(key=lambda tup: tup[2])
    return corners_with_angles

if __name__ == "__main__":
    if len(sys.argv[1:]) % 2 == 1:
        print("Parameters number error!")
    elif len(sys.argv[1:]) == 0:
        print("No parameters!")
    else:
        float_coordinates = [float(n) for n in sys.argv[1:]]
        vertices = sort_vertices(get_list_of_points(float_coordinates))
        print(get_area(vertices))