import uuid


def create_matrix(x, y):
    ''' Creates a matrix of given dimensions x and y

    Example:
    >>> m = create_matrix(2, 3)
    >>> assert m == [[1, 1],
    ...              [1, 1],
    ...              [1, 1]]
    '''
    return [[1] * x for i in range(y)]


def blank_area(botleft, topright, matrix):
    ''' Creates a rectangular blank area in the given matrix based
    on coordinates provided:

    botleft: (x, y)
    topright: (x, y)

    Example:
    >>> m = create_matrix(5, 6)
    >>> blank_area((0, 3), (3, 4), m)
    >>> assert m == [[1, 1, 1, 1, 1],
    ...              [1, 1, 1, 1, 1],
    ...              [1, 1, 1, 1, 1],
    ...              [0, 0, 0, 0, 1],
    ...              [0, 0, 0, 0, 1],
    ...              [1, 1, 1, 1, 1]]
    '''
    for i in range(botleft[1], topright[1] + 1):
        for j in range(botleft[0], topright[0] + 1):
            matrix[i][j] = 0


def area_of_shapes(matrix):
    ''' Returns sorted list of the areas of contiguous 'shapes'
    in the given matrix.

    Example:
    >>> m = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    >>> assert area_of_shapes(m) == [1, 3]
    '''
    # question: are shapes purely edge sharing, or also vertex sharing?
    #           diagonals, or just parallels and perpendiculars?
    min_x, max_x = 0, len(matrix) - 1
    min_y, max_y = 0, len(matrix[0]) - 1
    visited = [[False] * len(x) for x in matrix]
    shape_areas = dict()

    def find_neighbors(original_x, original_y):
        shape_uuid = uuid.uuid4()
        coord_stack = [(original_x, original_y)]
        while len(coord_stack) > 0:
            x, y = coord_stack.pop()
            if not visited[x][y]:
                visited[x][y] = True
                val = matrix[x][y]
                if val > 0:
                    if shape_uuid in shape_areas:
                        shape_areas[shape_uuid] += val
                    else:
                        shape_areas[shape_uuid] = val
                    if x < max_x:
                        coord_stack.append((x + 1, y))
                    if x > min_x:
                        coord_stack.append((x - 1, y))
                    if y < max_y:
                        coord_stack.append((x, y + 1))
                    if y > min_y:
                        coord_stack.append((x, y - 1))

    for row in enumerate(matrix):
        for cell in enumerate(row[1]):
            find_neighbors(row[0], cell[0])

    return sorted(shape_areas.values())


def value(matrix):
    '''Calculates the total value of the given matrix.

    Example:
    >>> m = create_matrix(2, 3)
    >>> assert value(m) == 6
    '''
    return sum(map(sum, matrix))


def max_possible(matrix):
    '''Calculates the total possible value of the given matrix.

    Example:
    >>> m = [[1, 0, 1],
    ...      [0, 1, 0],
    ...      [1, 0, 1]]
    >>> assert max_possible(m) == 9
    >>> assert value(m) == 5
    '''
    return sum(map(len, matrix))


def inverse(matrix):
    '''Inverts the given matrix.

    Example:
    >>> m = [[1, 0, 1],
    ...      [0, 1, 0],
    ...      [1, 0, 1]]
    >>> assert inverse(m) == [[0, 1, 0],
    ...                       [1, 0, 1],
    ...                       [0, 1, 0]]
    >>> assert inverse(inverse(m)) == m
    '''
    return [[0 if cell == 1 else 1 for cell in row] for row in matrix]


def transpose(matrix):
    '''Transposes the given matrix.

    Example:
    >>> m = [[1, 2],
    ...      [3, 4],
    ...      [5, 6]]
    >>> assert transpose(m) == [[1, 3, 5],
    ...                         [2, 4, 6]]
    '''
    return list(map(list, zip(*matrix)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
