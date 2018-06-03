from pprint import pprint


def make(x, y):
    return [[1] * x for i in range(y)]


def blank(botleft, topright, matrix):
    for i in range(botleft[1], topright[1] + 1):
        for j in range(botleft[0], topright[0] + 1):
            matrix[i][j] = 0


def value(matrix):
    return sum(map(sum, matrix))


def max_possible(matrix):
    return sum(map(len, matrix))


def area_of_shapes(matrix):
    # question: are shapes purely edge sharing, or also vertex sharing?
    #           diagonals, or just parallels and perpendiculars?
    min_x, max_x = 0, len(matrix[0]) - 1
    min_y, max_y = 0, len(matrix) - 1
    visited = [[False] * len(x) for x in matrix]
    shape_areas = []

    def find_neighbors(x, y):
        if not visited[x][y]:
            visited[x][y] = True
            if matrix[x][y] == 1:
                shape_areas[-1] += 1
                if x < max_x:
                    find_neighbors(x + 1, y)
                if x > min_x:
                    find_neighbors(x - 1, y)
                if y < max_y:
                    find_neighbors(x, y + 1)
                if y > min_y:
                    find_neighbors(x, y - 1)

    for row in enumerate(matrix):
        for cell in enumerate(row[1]):
            if not visited[row[0]][cell[0]]:
                if cell[1] == 1:
                    shape_areas.append(0)
                    find_neighbors(row[0], cell[0])
                visited[row[0]][cell[0]] = True

    return sorted(shape_areas)


def invert(matrix):
    return [[0 if cell == 1 else 1 for cell in row] for row in matrix]
