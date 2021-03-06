# Adhish guli Virupaksha - 65032

from .objects import Point, Vector, Ray, Sphere, Triangle
import numpy as np


def intersect(first_object, second_object):
    if isinstance(first_object, Ray) and isinstance(second_object, Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)

    if isinstance(first_object, Ray) and isinstance(second_object, Triangle):
        return _intersect_ray_with_triangle(first_object,second_object) 

    if isinstance(first_object, Sphere) and isinstance(second_object, Ray):
        return _intersect_ray_with_sphere(second_object,first_object) 

    if isinstance(first_object, Triangle) and isinstance(second_object, Ray):
        return _intersect_ray_with_triangle(second_object,first_object)

    return False              


def _intersect_ray_with_sphere(ray, sphere):
    r=sphere._radius
    c=sphere._centre
    o=ray._origin
    u=ray._direction
    # criteria for intersection
    oc = o - c
    del_1=np.dot(u._vector,oc._vector)
    del_2=np.linalg.norm(oc._vector)**2 - r**2
    del_total=del_1**2 - del_2
    
    if del_total<0 and abs(del_total)>10**(-5):
        return False
    # intersection point(s) x
    if abs(del_total)<10**(-5):
        d = -del_1
        x = o + Vector(d*u._vector) 
        return x

    if del_total>10**(-5):
        d1 = -del_1 + np.sqrt(del_total)
        d2 = -del_1 - np.sqrt(del_total) 
        if d1>0 and d2<0:
            x = o + Vector(d1*u._vector)
            return x
        if d1<0 and d2>0:
            x = o + Vector(d2*u._vector)
            return x    
        x1 = o + Vector(d1*u._vector) 
        x2 = o + Vector(d2*u._vector) 
        x=[x1,x2]
        return x
       

    

def _intersect_ray_with_triangle(ray, triangle):
    p12 = triangle.p2 - triangle.p1
    p13 = triangle.p3 - triangle.p1 
    n = np.cross(p12._vector, p13._vector)
    
    # criteria for intersection
    n_dot_dir = np.dot(n, ray._direction._vector)
    if abs(n_dot_dir)<10**(-6):
        return False

    d = np.dot(n, triangle.p1._point)    
    t = (np.dot(n, ray._origin._point) + d)/abs(n_dot_dir)
    if t<0:
        return False
    
    # intersection point p
    p = ray._origin + Vector(t*ray._direction._vector)    
    
    # verify point is inside triangle
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
         
    return p
