from .objects import Ray, Sphere, Triangle
import numpy as np


def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    r=sphere._radius
    c=sphere._centre
    o=ray._origin
    u=ray._direction
    oc = o - c
    del_1=np.dot(u._vector,oc._vector)
    del_2=np.linalg.norm(oc._vector)**2 - r**2
    del_total=del_1**2 - del_2

    return del_total>=0 

    

def _intersect_ray_with_triangle(ray, triangle):
    ...
