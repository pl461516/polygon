import sys

def get_area(vertices):
    area = 0.0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def get_list_of_points(coordinates):
    vertices = []
    for i in range(0, len(coordinates), 2):
        vertices.append((coordinates[i], coordinates[i + 1]))
    return vertices

if __name__ == "__main__":
    if len(sys.argv[1:]) % 2 == 1:
        print("Parameters number error!")
    else:
        # coordinates = [2, 4, 3, 7, 6, 10, 7, 15, 132, 34]
        float_coordinates = [float(n) for n in sys.argv[1:]]
        vertices = get_list_of_points(float_coordinates)
        print(get_area(vertices))
        # print(get_area(sys.argv[1:]))