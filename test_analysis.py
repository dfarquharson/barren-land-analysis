from pprint import pprint
import analysis
import random
import ast


def random_matrix(x, y):
    return [[random.randint(0, 1) for i in range(x)] for i in range(y)]


def dump(matrix, filename='dump.matrix'):
    with open(filename, 'w') as f:
        pprint(matrix, f)


def test_dump():
    m = random_matrix(5, 5)
    dump(m)
    with open('dump.matrix', 'r') as f:
        data = ast.literal_eval(f.read())
    assert m == data


def test_lookup():
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]
    assert m[1][1] == 5
    assert m[1][2] == 6
    assert m[2][1] == 8


def test_create_matrix():
    m = analysis.create_matrix(4, 6)
    assert m == [[1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1]]
    return m


def test_blank_area():
    m = analysis.create_matrix(5, 5)
    analysis.blank_area((0, 3), (4, 4), m)
    assert m == [[1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    return m


def test_split():
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((0, 3), (9, 6), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [30, 30]
    return m


def test_hshape():
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((1, 1), (2, 8), m)
    analysis.blank_area((1, 4), (8, 5), m)
    analysis.blank_area((7, 1), (8, 8), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [60]
    return m


def test_corners():
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((0, 3), (9, 6), m)
    analysis.blank_area((3, 0), (6, 9), m)
    assert analysis.value(m) == 36
    assert analysis.area_of_shapes(m) == [9, 9, 9, 9]
    return m


def test_archipelago():
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((8, 0), (9, 8), m)
    analysis.blank_area((0, 9), (7, 9), m)
    analysis.blank_area((0, 2), (7, 7), m)
    analysis.blank_area((0, 8), (6, 8), m)
    analysis.blank_area((2, 0), (7, 1), m)
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
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((1, 1), (8, 1), m)
    analysis.blank_area((1, 1), (1, 8), m)
    analysis.blank_area((8, 1), (8, 8), m)
    analysis.blank_area((1, 8), (8, 8), m)
    analysis.blank_area((1, 3), (8, 3), m)
    analysis.blank_area((1, 5), (8, 5), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [6, 6, 12, 36]
    return m


def test_vertical_lines():
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((1, 1), (8, 1), m)
    analysis.blank_area((1, 1), (1, 8), m)
    analysis.blank_area((3, 1), (3, 8), m)
    analysis.blank_area((5, 1), (5, 8), m)
    analysis.blank_area((8, 1), (8, 8), m)
    analysis.blank_area((1, 8), (8, 8), m)
    assert analysis.value(m) == 60
    assert analysis.area_of_shapes(m) == [6, 6, 12, 36]
    return m


def test_subsquare():
    m = analysis.create_matrix(10, 10)
    analysis.blank_area((1, 1), (2, 8), m)
    analysis.blank_area((7, 1), (8, 8), m)
    analysis.blank_area((1, 1), (8, 2), m)
    analysis.blank_area((1, 7), (8, 8), m)
    assert analysis.value(m) == 52
    assert analysis.area_of_shapes(m) == [16, 36]
    return m


def test_given_split():
    m = analysis.create_matrix(400, 600)
    analysis.blank_area((0, 292), (399, 307), m)
    assert analysis.value(m) == 233600
    assert analysis.area_of_shapes(m) == [116800, 116800]
    return m


def test_given_subshape():
    m = analysis.create_matrix(400, 600)
    analysis.blank_area((48, 192), (351, 207), m)
    analysis.blank_area((48, 392), (351, 407), m)
    analysis.blank_area((120, 52), (135, 547), m)
    analysis.blank_area((260, 52), (275, 547), m)
    assert analysis.value(m) == 215424
    assert analysis.area_of_shapes(m) == [22816, 192608]
    return m


def test_value():
    m = [[1, 1, 0],
         [0, 0, 0],
         [1, 0, 1]]
    assert analysis.value(m) == 4
    return m


def test_max_possible():
    m = test_value()
    assert analysis.max_possible(m) == 9
    return m


def test_inverse():
    m = random_matrix(5, 5)
    assert m == analysis.inverse(analysis.inverse(m))
    assert analysis.inverse(
        [[1, 0, 1], [0, 1, 0]]) == \
        [[0, 1, 0], [1, 0, 1]]
    return m


def test_transpose():
    assert test_vertical_lines() == analysis.transpose(test_horizontal_lines())
    m = random_matrix(4, 4)
    assert analysis.transpose(analysis.transpose(m)) == m
    assert analysis.transpose(
        [[2, 3],
         [4, 6],
         [6, 9]]) == \
        [[2, 4, 6],
         [3, 6, 9]]
