from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle
y=Sphere((0,0,0),10)
x=Ray((20,20,20),(4/5,3/5,0))
del_1=_intersect_ray_with_sphere(x,y)
print(del_1)

# intersect


# _intersect_ray_with_sphere


# _intersect_ray_with_triangle
