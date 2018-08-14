from OSOL.Extremum.Tools.Encoders import CustomEncoder
from OSOL.Extremum.Numerical_Objects.Interval import *

import json
import pytest


i1 = Interval(-1.0, 2.0)
i2 = Interval(-4.0, 3.0)
i3 = Interval(1.0, 2.0)
i4 = Interval(5.0, 5.1)
i5 = Interval(-6.0, -5.0)
i6 = Interval(-2.0, 0.0)
i7 = Interval(0.0, 3.0)


def test_to_string():
    assert str(i1) == '[-1.0; 2.0]'
    assert str(i4) == '[5.0; 5.1]'
    assert str(i6) == '[-2.0; 0.0]'


def test_from_dict():
    assert i1.approximately_equals_to(Interval.from_dict({'lower_bound': i1.left, 'upper_bound': i1.right}))
    assert i5.approximately_equals_to(Interval.from_dict({'lower_bound': i5.left, 'upper_bound': i5.right}))
    assert i7.approximately_equals_to(Interval.from_dict({'lower_bound': i7.left, 'upper_bound': i7.right}))


def test_from_dump():
    assert i1.approximately_equals_to(Interval.from_json(json.loads(json.dumps(i1, cls=CustomEncoder))))
    assert i5.approximately_equals_to(Interval.from_json(json.loads(json.dumps(i5, cls=CustomEncoder))))
    assert i7.approximately_equals_to(Interval.from_json(json.loads(json.dumps(i7, cls=CustomEncoder))))


def test_middle_point():
    assert i1.middle_point == 0.5
    assert i3.middle_point == 1.5
    assert i7.middle_point == 1.5


def test_width():
    assert i1.width == 3.0
    assert i3.width == 1.0
    assert i7.width == 3.0


def test_radius():
    assert i1.radius == 1.5
    assert i3.radius == 0.5
    assert i7.radius == 1.5


def test_approximate_equality():
    assert i1.approximately_equals_to(i1 + Interval.from_value(1e-7))
    assert not Interval(-math.inf, 0.0).approximately_equals_to(Interval(-math.inf, math.nan))


def test_equality():
    assert i1 == i1
    assert Interval(2.0, 2.0) == 2.0


def test_inequality():
    assert i1 != i2
    assert not (Interval(2.0, 2.0) != 2.0)


def test_lt():
    assert i2 < i1
    assert i6 < i7


def test_le():
    assert i2 <= i1
    assert i2 <= Interval(-4.0, 2.0)


def assert_gt():
    assert i1 > i2
    assert i7 > i6


def assert_ge():
    assert i1 >= i2
    assert Interval(-4.0, 2.0) >= i2


def test_addition():
    assert (i1 + 2).approximately_equals_to(Interval(1.0, 4.0))
    assert (2.0 + i1).approximately_equals_to(Interval(1.0, 4.0))
    assert (i1 + i2).approximately_equals_to(Interval(-5.0, 5.0))
    assert (i2 + i3).approximately_equals_to(Interval(-3.0, 5.0))
    assert (i5 + i4).approximately_equals_to(Interval(-1.0, 0.1))


def test_subtraction():
    assert (i1 - 1).approximately_equals_to(Interval(-2.0, 1.0))
    assert (1.0 - i1).approximately_equals_to(Interval(-1.0, 2.0))
    assert (i1 - i2).approximately_equals_to(Interval(-4.0, 6.0))
    assert (i2 - i3).approximately_equals_to(Interval(-6.0, 2.0))
    assert (i5 - i4).approximately_equals_to(Interval(-11.1, -10.0))


def test_multiplication():
    assert (i1 * (-1)).approximately_equals_to(Interval(-2.0, 1.0))
    assert ((-1.0) * i1).approximately_equals_to(Interval(-2.0, 1.0))
    assert (i1 * i2).approximately_equals_to(Interval(-8.0, 6.0))
    assert (i2 * i3).approximately_equals_to(Interval(-8.0, 6.0))
    assert (i5 * i4).approximately_equals_to(Interval(-30.6, -25.0))


def test_division():
    assert (i1 / 2).approximately_equals_to(Interval(-0.5, 1.0))
    assert (2.0 / i1).approximately_equals_to(Interval(-math.inf, math.inf))
    assert (i1 / i2).approximately_equals_to(Interval(-math.inf, math.inf))
    assert (i2 / i3).approximately_equals_to(Interval(-4.0, 3.0))
    assert (i1 / i5).approximately_equals_to(Interval(-0.4, 0.2))
    assert (i3 / i6).approximately_equals_to(Interval(-math.inf, -0.5))
    assert (i5 / i7).approximately_equals_to(Interval(-math.inf, -5.0 / 3.0))


def test_power():
    assert (i1 ** 2.0).approximately_equals_to(Interval(0.0, 4.0))
    assert (i2 ** 3.0).approximately_equals_to(Interval(-64.0, 27.0))
    assert Interval.from_value(i5 ** 0.0).approximately_equals_to(Interval(1.0, 1.0))


def test_negate():
    assert (-i1).approximately_equals_to(Interval(-2.0, 1.0))
    assert (-i5).approximately_equals_to(Interval(5.0, 6.0))
    assert (-i6).approximately_equals_to(Interval(0.0, 2.0))


def test_sin():
    assert sin(i1).approximately_equals_to(Interval(math.sin(-1.0), 1.0))
    assert sin(i2).approximately_equals_to(Interval(-1.0, 1.0))
    assert sin(i3).approximately_equals_to(Interval(math.sin(1.0), 1.0))
    assert sin(i6).approximately_equals_to(Interval(-1.0, 0.0))


def test_cos():
    assert cos(i1).approximately_equals_to(Interval(math.cos(2.0), 1.0))
    assert cos(i2).approximately_equals_to(Interval(-1.0, 1.0))
    assert cos(i3).approximately_equals_to(Interval(math.cos(2.0), math.cos(1.0)))
    assert cos(i6).approximately_equals_to(Interval(math.cos(-2.0), 1.0))


def test_abs():
    assert abs(i1).approximately_equals_to(Interval(0.0, 2.0))
    assert abs(i2).approximately_equals_to(Interval(0.0, 4.0))
    assert abs(i3).approximately_equals_to(Interval(1.0, 2.0))
    assert abs(i4).approximately_equals_to(Interval(5.0, 5.1))
    assert abs(i5).approximately_equals_to(Interval(5.0, 6.0))
    assert abs(i6).approximately_equals_to(Interval(0.0, 2.0))
    assert abs(i7).approximately_equals_to(Interval(0.0, 3.0))


def test_exp():
    assert exp(i1).approximately_equals_to(Interval(math.exp(-1.0), math.exp(2.0)))
    assert exp(i2).approximately_equals_to(Interval(math.exp(-4.0), math.exp(3.0)))
    assert exp(i3).approximately_equals_to(Interval(math.exp(1.0), math.exp(2.0)))


def test_sqrt():
    assert sqrt(i1).approximately_equals_to(Interval(0.0, math.sqrt(2.0)))
    assert sqrt(i3).approximately_equals_to(Interval(math.sqrt(1.0), math.sqrt(2.0)))
    with pytest.raises(Exception):
        sqrt(i5)


def test_log():
    assert log(i1).approximately_equals_to(Interval(-math.inf, math.log(2.0)))
    assert log(i2).approximately_equals_to(Interval(-math.inf, math.log(3.0)))
    assert log(i3).approximately_equals_to(Interval(math.log(1.0), math.log(2.0)))
    assert log(i4).approximately_equals_to(Interval(math.log(5.0), math.log(5.1)))
    with pytest.raises(Exception):
        log(i5)
    with pytest.raises(Exception):
        log(i6)
    assert log(i7).approximately_equals_to(Interval(-math.inf, math.log(3.0)))


def test_constrain():
    assert i1.constrain(1.5, 3.0).approximately_equals_to(Interval(1.5, 2.0))
    assert Interval.from_value(i4.constrain(1.5, 3.0)).approximately_equals_to(Interval(3.0, 3.0))
    assert i7.constrain(-10, 3.0).approximately_equals_to(i7)


def test_splitting():
    assert i1.bisect()[0] == Interval(-1.0, 0.5)
    assert i1.bisect()[1] == Interval(0.5, 2.0)
    assert i1.split([1.0, 2.0])[0] == Interval(-1.0, 0.0)
    assert i1.split([1.0, 2.0])[1] == Interval(0.0, 2.0)