import numpy as np
from collections import namedtuple
from math import sin, cos


V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])

def load_vertices(model):
    vertices_objeto = []
    for face in model.faces:
        for v in range(len(face)):
            vertex = model.vertices[face[v][0] - 1]
            vertices_objeto.extend(vertex)
            tvertex = model.tvertices[face[v][1] - 1]
            vertices_objeto.extend(tvertex)
            normal = model.normales[face[v][2] - 1]
            vertices_objeto.extend(normal)
    
    
    vertices_objeto = np.array(vertices_objeto, dtype = np.float32)

    index_data = np.array([[vertex[0] - 1 for vertex in face] for face in model.faces], dtype=np.uint32).flatten()
    #retrun lista con vertices mejoradas
    return vertices_objeto,index_data

def rotationMatrix(point):
    rotate = V3(*point)

    a = rotate.x
    rotateX = [
        [1, 0, 0, 0],
        [0, cos(a), -sin(a), 0],
        [0, sin(a), cos(a), 0],
        [0, 0, 0, 1],
    ]

    b = rotate.y
    rotateY = [
        [cos(b), 0, sin(b), 0],
        [0, 1, 0, 0],
        [-sin(b), 0, cos(b), 0],
        [0, 0, 0, 1],
    ]

    c = rotate.z
    rotateZ = [
        [cos(c), -sin(c), 0, 0],
        [sin(c), cos(c), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]

    return mulMatrix(rotateX, mulMatrix(rotateY, rotateZ))

def mulMatrix(A, B):
    newMatrix = []

    # Filas de A
    for i in range(len(A)):
        lista = []
        
        # Obtengo la filas de B
        for j in range(len(B[0])):
            actualRes = 0
            # Obtengo la columna de B
            columnB = [row[j] for row in B]
        
            rowA = A[i]
            for k in range(len(rowA)):
                actualRes += A[i][k] * columnB[k]

            # Luego de multiplicar todos los elementos de A con B,
            # meter ese resultado a la matriz resultante
            lista.append(actualRes)
        newMatrix.append(lista)

    return newMatrix