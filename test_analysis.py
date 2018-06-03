import analysis


def test_split():
    m = analysis.make(10, 10)
    analysis.blank((0, 3), (9, 6), m)
    assert analysis.total(m) == 60
    assert analysis.num_shapes(m) == 2
    assert analysis.area_of_shapes(m) == [30, 30]
    return m


def test_hshape():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (2, 8), m)
    analysis.blank((1, 4), (8, 5), m)
    analysis.blank((7, 1), (8, 8), m)
    assert analysis.total(m) == 60
    assert analysis.num_shapes(m) == 1
    assert analysis.area_of_shapes(m) == [60]
    return m


def test_figure_eight():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (8, 1), m)
    analysis.blank((1, 1), (1, 8), m)
    analysis.blank((8, 1), (8, 8), m)
    analysis.blank((1, 8), (8, 8), m)
    analysis.blank((1, 3), (8, 3), m)
    analysis.blank((1, 5), (8, 5), m)
    assert analysis.total(m) == 60
    # assert analysis.num_shapes(m) == 4
    # assert analysis.area_of_shapes(m) == [6, 6, 12, 36]
    return m


def test_subsquare():
    m = analysis.make(10, 10)
    analysis.blank((1, 1), (2, 8), m)
    analysis.blank((7, 1), (8, 8), m)
    analysis.blank((1, 1), (8, 2), m)
    analysis.blank((1, 7), (8, 8), m)
    assert analysis.total(m) == 52
    # assert analysis.num_shapes(m) == 2
    # assert analysis.area_of_shapes(m) == [16, 36]
    return m


def test_given_split():
    m = analysis.make(400, 600)
    analysis.blank((0, 292), (399, 307), m)
    assert analysis.total(m) == 233600
    # assert analysis.num_shapes(m) == 2
    # assert analysis.area_of_shapes(m) == [116800, 116800]
    return m


def test_given_subshape():
    m = analysis.make(400, 600)
    analysis.blank((48, 192), (351, 207), m)
    analysis.blank((48, 392), (351, 407), m)
    analysis.blank((120, 52), (135, 547), m)
    analysis.blank((260, 52), (275, 547), m)
    assert analysis.total(m) == 215424
    # assert analysis.num_shapes(m) == 2
    # assert analysis.area_of_shapes(m) == [22816, 192608]
    return m
