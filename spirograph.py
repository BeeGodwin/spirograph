from math import sin, cos, degrees, radians, pi


class Circle:

    def __init__(self, rad, is_active=False, angle=0, point=0):
        self.radius = rad
        self.active = is_active  # if True, this circle draws a line
        self.angle = angle
        self.point = point  # expressed as a percentage of self.radius
        self.x = 0
        self.y = 0
        self.children = []

    def inc_angle(self, deg):
        self.angle += deg
        for child in self.children:
            child.inc_angle(-(self.radius / child.radius) * deg)
            self.set_child_position()

    def set_child_position(self):
        norm_x, norm_y = normalised_vector(self.angle)
        for child in self.children:
            radius = self.radius - child.radius
            ch_x = self.x + norm_x * radius
            ch_y = self.y + norm_y * radius
            child.set_position(ch_x, ch_y)
            # set the child's position, using self.angle, self.radius, and self.x , y.


    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_point_position(self):
        """Computes the point position from self.x, self.y, self.angle,
        and self.point."""
        norm_x, norm_y = normalised_vector(self.angle)
        point_rad = self.radius * self.point / 100
        norm_x *= point_rad
        norm_y *= point_rad
        return norm_x + self.x, norm_y + self.y

    def add_child(self, child):
        self.children.append(child)


def normalised_vector(deg):
    """given an angle in degrees, where 0 is up, return a
    normalised vector as the 2-tuple (x,y)."""
    vec_x = sin(radians(deg))
    vec_y = -cos(radians(deg))
    return round(vec_x, 3), round(vec_y, 3)
