from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Point, Vector, Ray, Sphere, Triangle
import numpy as np

r=Ray((10,10,5),(0,0,-1))
t=Triangle((0,0,0),(10,0,0),(5,10,0))
print(_intersect_ray_with_triangle(r,t))


# intersect


# _intersect_ray_with_sphere - testing for 2d cases confirm for all cases
#inputs for non intersecting ray and sphere
x=Ray((0,10,0),(0,-1,0))
y=Sphere((10,0,0),5)

def test_non_intersecting_ray_sphere_return_false():
    assert _intersect_ray_with_sphere(x,y) is False
#inputs for ray and sphere intersecting at 2 points
x1=Ray((0,10,0),(0,-1,0))
y1=Sphere((0,0,0),5)
#The two expected intersecting points
p1=Point((0,-5,0))
p2=Point((0,5,0))

def test_intersecting_ray_sphere_at_two_points_return_true():
    x=_intersect_ray_with_sphere(x1,y1)
    diff1=x[0]-p1
    diff2=x[1]-p2
    d1=abs(np.linalg.norm(diff1._vector))
    d2=abs(np.linalg.norm(diff2._vector))
    assert (d1<10**(-5) and d2<10**(-5)) == True is True   
#inputs for ray and sphere intersecting at 1 point
x2=Ray((0,10,0),(0,-1,0))
y2=Sphere((5,0,0),5)
#The expected intersecting point
p=Point((0,0,0))

def test_intersecting_ray_sphere_at_one_point_return_true():
    x=_intersect_ray_with_sphere(x2,y2)
    diff=x-p
    d=abs(np.linalg.norm(diff._vector))
    assert (d<10**(-5)) == True is True     


# _intersect_ray_with_triangle

#input for intersecting ray and triangle
r=Ray((5,2,5),(0,0,-1))
t=Triangle((0,0,0),(10,0,0),(5,10,0))
#The expected intersecting point
pt = Point((5,2,0))

def test_intersecting_ray_triangle_return_true():
    xt = _intersect_ray_with_triangle(r,t)
    difft = xt-pt
    dt=abs(np.linalg.norm(difft._vector))
    assert (dt<10**(-5)) == True is True 

#input for intersecting ray and triangle
r1=Ray((10,10,5),(0,0,-1))
t1=Triangle((0,0,0),(10,0,0),(5,10,0))  

def test_non_intersecting_ray_triangle_return_false():
    assert _intersect_ray_with_triangle(r1,t1) is False