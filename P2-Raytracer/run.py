from materials import *
from raytracing import *

r = Raytracer(1000, 1000)
r.light=Light(position=V3(10,10,10),intensity=1.5,color=WHITE)

'''
scene_triangles = []
triangles_vertex = r.Load('./tree.obj', (0, 0, -5), (2, 2, 2))
for triangle_vertex in triangles_vertex:
    scene_triangles.append(Triangle(triangle_vertex, rubber))
r.scene = scene_triangles
r.scene.append(Cube(V3(-2, 0.75, -9.25), 0.5, rubber))
'''

r.scene = [
    Cube(V3(-0.5, 0.75, -9.25), 0.5, wood),

]

r.render()
r.write('r')

print('done')