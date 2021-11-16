from materials import *
from raytracing import *
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

r = Raytracer(200, 200)
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
    Cube(V3(-0.6, 1.7, -9.25), 0.25, skin1),
    Cube(V3(-0.30, 1.7, -9.25), 0.25, skin1),
    Cube(V3(-0.10, 1.7, -9.25), 0.25, skin1),
    Cube(V3(0, 1.7, -9.25), 0.25, skin1),
    Cube(V3(0.15, 1.7, -9.25), 0.25, skin1),

    Cube(V3(-0.5, 2.05, -9.25), 0.5, orange7),
    Cube(V3(0, 2.05, -9.25), 0.5, orange7),

    #face

    Cube(V3(-0.5, 0.25, -9.25), 0.5, orange4),
    Cube(V3(0, 0.25, -9.25), 0.5, orange4),

    Cube(V3(-1.5, 1.25, -9.25), 0.5, orange4),
    Cube(V3(1, 1.25, -9.25), 0.5, orange4),

    Cube(V3(-1.5, 1.75, -9.25), 0.5, orange5),
    Cube(V3(1, 1.75, -9.25), 0.5, orange5),

    Cube(V3(-1, -1.25, -9.25), 0.5, orange8),
    Cube(V3(-1.5, -0.75, -9.25), 0.5, orange8),
    Cube(V3(-2, -1.25, -9.25), 0.5, orange8),
    Cube(V3(-2, -0.75, -9.25), 0.5, orange8),
    Cube(V3(-2, -0.25, -9.25), 0.5, orange8),
    Cube(V3(-2, 1.25, -9.25), 0.5, orange5),
    Cube(V3(-2, 1.75, -9.25), 0.5, orange6),
    Cube(V3(-2, 2.25, -9.25), 0.5, orange3),
    Cube(V3(-1.5, 2.25, -9.25), 0.5, orange6),
    Cube(V3(-1, 2.25, -9.25), 0.5, orange6),
    Cube(V3(-0.5, 2.25, -9.25), 0.5, orange6),
    Cube(V3(0, 2.25, -9.25), 0.5, orange6),
    Cube(V3(0.5, 2.25, -9.25), 0.5, orange6),
    Cube(V3(1, 2.25, -9.25), 0.5, orange6),
    Cube(V3(1.5, 2.25, -9.25), 0.5, orange3),
    Cube(V3(1.5, 1.75, -9.25), 0.5, orange6),
    Cube(V3(1.5, 1.25, -9.25), 0.5, orange5),
    Cube(V3(1.5, -0.25, -9.25), 0.5, orange8),
    Cube(V3(1.5, -1.25, -9.25), 0.5, orange8),
    Cube(V3(1.5, -0.75, -9.25), 0.5, orange8),
    Cube(V3(1, -1.25, -9.25), 0.5, orange8),
    Cube(V3(0.5, -0.75, -9.25), 0.5, orange8),
    

]

r.render()
r.write('r')

print('done')