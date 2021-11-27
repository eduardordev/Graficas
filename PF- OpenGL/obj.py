import struct


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.tvertices = []
        self.normales = []
        self.faces = []
        self.read()

    def read(self):
        maximo_y = 1
        maximo_x = 1
        maximo_z = 1
        for line in self.lines:        
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    prefix = ''            
                if prefix == 'v':
                    vert = list(map(float, value.lstrip(' ').rstrip(' ').split(' ')))
                    self.vertices.append(vert)
                    
                    if vert[0]>maximo_x:
                        maximo_x = vert[0]

                    if vert[1]>maximo_y:
                        maximo_y = vert[1]

                    if vert[2]>maximo_z:
                        maximo_z = vert[2]
                        
                elif prefix == 'vt':
                    self.tvertices.append(
                        list(map(float, value.lstrip(' ').rstrip(' ').split(' '))))
                elif prefix == 'vn':
                    self.normales.append(list(map(float, value.lstrip(' ').rstrip(' ').split(' '))))
                elif prefix == 'f':
                    faces = value.split(' ')
                    if(len(faces)==3):
                        self.faces.append([list(map(int, face.replace('//','/').split('/'))) for face in faces if len(face)>2])
                    else:
                        faces1 = [faces[0], faces[1], faces[2]]
                        faces2 = [faces[0], faces[2], faces[3]]
                        self.faces.append([list(map(int, face.replace('//','/').split('/'))) for face in faces1 if len(face)>2])
                        self.faces.append([list(map(int, face.replace('//','/').split('/'))) for face in faces2 if len(face)>2])

        self.vertices = [[i[0]/maximo_x, i[1]/maximo_y, i[2]/maximo_z]for i in self.vertices]
