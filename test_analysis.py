import analysis
import random


def random_matrix(x, y):
    return [[random.randint(0, 1) for i in range(x)] for i in range(y)]


def dump(matrix, filename='dump.matrix'):
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(','.join(map(str, row)) + '\n')


def test_recursionlimit():
    import sys
    sys.setrecursionlimit(2000)
    assert sys.getrecursionlimit() == 2000


def test_split():
    m = analysis.make(10, 10)
    analysis.blank((0, 3), (9, 6), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [30, 30]
    return m


def test_hshape():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (2, 8), m)
    analysis.blank((1, 4), (8, 5), m)
    analysis.blank((7, 1), (8, 8), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [60]
    return m


def test_corners():
    m = analysis.make(10, 10)
    analysis.blank((0, 3), (9, 6), m)
    analysis.blank((3, 0), (6, 9), m)
    assert analysis.value(m) == 36
    assert analysis.area_of_shapes(m) == [9, 9, 9, 9]
    return m


def test_archipelago():
    m = analysis.make(10, 10)
    analysis.blank((8, 0), (9, 8), m)
    analysis.blank((0, 9), (7, 9), m)
    analysis.blank((0, 2), (7, 7), m)
    analysis.blank((0, 8), (6, 8), m)
    analysis.blank((2, 0), (7, 1), m)
    assert analysis.value(m) == 7
    assert analysis.area_of_shapes(m) == [1, 2, 4]
    return m


def test_small_archipelago():
    m = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1]]
    assert analysis.value(m) == 6
    assert analysis.area_of_shapes(m) == [1, 1, 4]
    return m


def test_horizontal_lines():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (8, 1), m)
    analysis.blank((1, 1), (1, 8), m)
    analysis.blank((8, 1), (8, 8), m)
    analysis.blank((1, 8), (8, 8), m)
    analysis.blank((1, 3), (8, 3), m)
    analysis.blank((1, 5), (8, 5), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [6, 6, 12, 36]
    return m


def test_vertical_lines():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (8, 1), m)
    analysis.blank((1, 1), (1, 8), m)
    analysis.blank((3, 1), (3, 8), m)
    analysis.blank((5, 1), (5, 8), m)
    analysis.blank((8, 1), (8, 8), m)
    analysis.blank((1, 8), (8, 8), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [6, 6, 12, 36]
    return m


def test_subsquare():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (2, 8), m)
    analysis.blank((7, 1), (8, 8), m)
    analysis.blank((1, 1), (8, 2), m)
    analysis.blank((1, 7), (8, 8), m)
    assert analysis.value(m) == 52
    assert analysis.area_of_shapes(m) == [16, 36]
    return m


def test_given_split():
    m = analysis.make(400, 600)
    analysis.blank((0, 292), (399, 307), m)
    assert analysis.value(m) == 233600
    # assert analysis.area_of_shapes(m) == [116800, 116800]
    return m


def test_given_subshape():
    m = analysis.make(400, 600)
    analysis.blank((48, 192), (351, 207), m)
    analysis.blank((48, 392), (351, 407), m)
    analysis.blank((120, 52), (135, 547), m)
    analysis.blank((260, 52), (275, 547), m)
    assert analysis.value(m) == 215424
    # assert analysis.area_of_shapes(m) == [22816, 192608]
    return m


def test_invert():
    m = random_matrix(5, 5)
    assert m == analysis.invert(analysis.invert(m))


def test_compress_corners():
    m = analysis.compress(test_corners())
    assert analysis.value(m) == 36
    assert analysis.area_of_shapes(m) == [9, 9, 9, 9]
    assert m == [[9, 0, 9],
                 [0, 0, 0],
                 [9, 0, 9]]


def test_compress_horizontal_lines():
    m = analysis.compress(test_horizontal_lines())
    # assert analysis.value(m) == 60
    # assert analysis.area_of_shapes(m) == [6, 6, 12, 36]
    assert m == [[1, 1, 6, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 0, 6, 0, 1],
                 [1, 0, 0, 0, 1],
                 [1, 0, 6, 0, 1],
                 [1, 0, 0, 0, 1],
                 [2, 0, 12, 0, 2],
                 [1, 1, 6, 1, 1]]
    return m


def test_compress_given_split():
    m = analysis.compress(test_given_split())
    assert analysis.value(m) == 233600
    assert analysis.area_of_shapes(m) == [116800, 116800]
    assert m == [[116800],
                 [0],
                 [116800]]


def test_compress_given_subshape():
    m = analysis.compress(test_given_subshape())
    # assert analysis.value(m) == 215424
    # assert analysis.area_of_shapes(m) == [22816, 192608]
    # assert m == [23232,
                 # 22816,


def test_transpose():
    assert test_vertical_lines() == analysis.transpose(test_horizontal_lines())


def facloop(n, acc=1):
    while n > 1:
        (n, acc) = (n - 1, acc * n)
    return acc


def facrec(n):
    if n < 2:
        return 1
    else:
        return n * facrec(n - 1)


def test_fac():
    assert facrec(5) == facloop(5) == 120
    assert len(str(facloop(120))) == 199
