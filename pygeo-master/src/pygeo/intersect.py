from .objects import Point, Vector, Ray, Sphere, Triangle
import numpy as np


def intersect(first_object, second_object):
    if isinstance(first_object, Ray) and isinstance(second_object, Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)

    if isinstance(first_object, Ray) and isinstance(second_object, Triangle):
        return _intersect_ray_with_triangle(first_object,second_object)    


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
    p12 = triangle.p2 - triangle.p1
    p13 = triangle.p3 - triangle.p1 
    n = np.cross(p12._vector, p13._vector)
   
    n_dot_dir = np.dot(n, ray._direction._vector)
    if abs(n_dot_dir)<10**(-6):
        return False

    d = np.dot(n, triangle.p1._point)    
    t = np.dot(n, ray._origin._point) + d
    if t<0:
        return False
    
    # intersection point p
    p = ray._origin + Vector(t*ray._direction._vector)    

    edge1 = p - triangle.p1
    c = np.cross(p12._vector, edge1._vector)
    check = np.dot(n, c)
    if  check < 0:
        return False
    
    p23 = triangle.p3 - triangle.p2
    edge2 = p - triangle.p2
    c = np.cross(p23._vector, edge2._vector)
    check = np.dot(n, c)
    if  check < 0:
        return False

    p31 = triangle.p1 - triangle.p3
    edge3 = p - triangle.p3
    c = np.cross(p31._vector, edge3._vector)
    check = np.dot(n, c)
    if  check < 0:
        return False    
         
    return True
