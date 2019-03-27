import basic_functions


def test_u(n):
    x = basic_functions.u(-1)
    assert x == 0
    x = basic_functions.u(0)
    assert x == 1
    x = basic_functions.u(1)
    assert x == 1


def test_dirac(n):
    x = basic_functions.dirac(-1)
    assert x == 0
    x = basic_functions.dirac(0)
    assert x == 1
    x = basic_functions.dirac(1)
    assert x == 0


def test_v(n):
    x = basic_functions.v(-1)
    assert x == 0
    x = basic_functions.v(0)
    assert x == 0
    x = basic_functions.v(1)
    assert x == 1
    x = basic_functions.v(20)
    assert x == 20