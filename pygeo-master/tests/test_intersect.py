from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle
y=Sphere((0,0,0),10)
x=Ray((0,0,0),(-4/5,-3/5,0))

t=Triangle((1,0,0),(0,1,0),(0,0,1))

print(intersect(x,t))

# intersect


# _intersect_ray_with_sphere


# _intersect_ray_with_triangle
