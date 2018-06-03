def make(x, y):
    return [[1] * x for i in range(y)]


def blank(botleft, topright, matrix):
    for i in range(botleft[1], topright[1] + 1):
        for j in range(botleft[0], topright[0] + 1):
            matrix[i][j] = 0


def total(matrix):
    return sum(map(sum, matrix))


def dump(matrix, filename='dump.matrix'):
    with open(filename, 'w') as f:
        for line in matrix:
            f.write(','.join(map(str, line)) + '\n')


def num_shapes(matrix):
    return 1


def area_of_shapes(matrix):
    return [total(matrix)]
