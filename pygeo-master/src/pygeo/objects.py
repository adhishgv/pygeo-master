import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""

    def __init__(self, origin, direction):
        self._origin= Point(origin)
        self._direction= Vector(direction)

    def __repr__(self):
        return f"Point(%s) is the origin and Point(%s) is the direction of the ray" % (self._origin,self._direction)

    def __eq__(self, other):
        if isinstance(other, Ray):
            return self._origin == other._origin and self._direction == other._direction
        return False    

class Sphere:
    """A sphere."""

    def __init__(self, centre, radius):
       self._centre= Point(centre)
       self._radius= float(radius)

    def __repr__(self):
        return f"Point(%s) is the centre and {self._radius} is the radius of the sphere" % (self._centre)

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return self._centre == other._centre and self._radius == other._radius
        return False


class Triangle:
    """A triangle."""

    ...
