from materials import *
from raytracing import *

r = Raytracer(400, 400)
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
    Cube(V3(-1, 0.75, -9.25), 0.5, orange1),
    Cube(V3(-0.5, 0.75, -9.25), 0.5, orange),
    Cube(V3(0, 0.75, -9.25), 0.5, orange),
    Cube(V3(0.5, 0.75, -9.25), 0.5, orange1),
    Cube(V3(-1, 1.25, -9.25), 0.5, orange2),
    Cube(V3(0.5, 1.25, -9.25), 0.5, orange2),
    Cube(V3(-1, 1.75, -9.25), 0.5, orange3),
    Cube(V3(0.5, 1.75, -9.25), 0.5, orange3),

    #eye left
    Cube(V3(0.5, 0.25, -9.25), 0.5, skin),
    Cube(V3(1, 0.25, -9.25), 0.5, skin),
    Cube(V3(1, 0.75, -9.25), 0.5, skin),

    #eye right
    Cube(V3(-1, 0.25, -9.25), 0.5, skin),
    Cube(V3(-1.5, 0.25, -9.25), 0.5, skin),
    Cube(V3(-1.5, 0.75, -9.25), 0.5, skin),

    #mouth
    Cube(V3(-0.5, 0.25, -9.25), 0.25, skin1),
    Cube(V3(-0.25, 0.25, -9.25), 0.25, skin1),
    Cube(V3(0, 0.75, -9.25), 0.25, skin1),
    Cube(V3(0.25, 0.75, -9.25), 0.25, skin1),

]

r.render()
r.write('r')

print('done')