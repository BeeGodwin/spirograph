import spirograph
from spirograph import Circle


def test_create_circle():
    c = Circle(100)
    assert c.radius == 100
    assert not c.active
    assert c.angle == 0
    c_1 = Circle(100, is_active=True, angle=180, point=50)
    assert c_1.radius == 100
    assert c_1.active
    assert c_1.angle == 180
    assert c_1.point == 50


def test_inc_angle():
    c = Circle(100, is_active=True, point=50)
    c.inc_angle(1)
    assert c.angle == 1


def test_set_position():
    c = Circle(100)
    assert c.x == 0
    assert c.y == 0
    c.set_position(100, 100)
    assert c.x == 100
    assert c.y == 100


def test_get_point_position():
    c = Circle(100, is_active=True, point=50)
    point_x, point_y = c.get_point_position()
    assert point_x == 0
    assert point_y == 50
    c.inc_angle(90)
    point_x, point_y = c.get_point_position()
    assert point_x == 50
    assert point_y == 0
    c.inc_angle(90)
    point_x, point_y = c.get_point_position()
    assert point_x == 0
    assert point_y == -50
    c.inc_angle(90)
    point_x, point_y = c.get_point_position()
    assert point_x == -50
    assert point_y == 0


def test_normalised_vector():
    assert spirograph.normalised_vector(0) == (0, 1)
    assert spirograph.normalised_vector(90) == (1, 0)
    assert spirograph.normalised_vector(180) == (0, -1)
    assert spirograph.normalised_vector(270) == (-1, 0)
