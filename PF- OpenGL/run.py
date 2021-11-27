from math import sin
import pygame
from func import load_vertices,rotationMatrix
import numpy as np
from obj import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glm


HEIGHT = 720
WIDTH = 1200
ASPECT_RATIO = WIDTH/HEIGHT
pygame.init()
screen = pygame.display.set_mode((1200, 720), pygame.OPENGL | pygame.DOUBLEBUF)
glClearColor(0.1, 0.2, 0.5, 1.0)
glEnable(GL_DEPTH_TEST)
clock = pygame.time.Clock()


vertex_shader = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 ccolor;
uniform mat4 theMatrix;
out vec3 mycolor;
void main() 
{
  gl_Position = theMatrix * vec4(position.x, position.y, position.z, 1);
  mycolor = ccolor;
}
"""

fragment_shader = """
#version 460
layout(location = 0) out vec4 fragColor;
uniform int clock;
in vec3 mycolor;
void main()
{
    if (mod(clock/10, 2) == 0) {
    fragColor = vec4(mycolor.xyz, 1.0f);
} else {
    fragColor = vec4(mycolor.zxy, 1.0f);
    }
}
"""

cvs = compileShader(vertex_shader, GL_VERTEX_SHADER)
cfs = compileShader(fragment_shader, GL_FRAGMENT_SHADER)

shader = compileProgram(cvs, cfs)



#segundo shaders
vertex_shader2 = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 ccolor;
uniform mat4 theMatrix;
out vec3 mycolor;
void main() 
{
  gl_Position = theMatrix * vec4(position.x, position.y, position.z, 1);
  mycolor = ccolor;
}
"""

fragment_shader2 = """
#version 460
layout(location = 0) out vec4 fragColor;
uniform int clock;
in vec3 mycolor;
void main()
{
    fragColor = vec4(mycolor.x,0.5f, 1.0f,1.0f);
}
"""

cvs2 = compileShader(vertex_shader2, GL_VERTEX_SHADER)
cfs2 = compileShader(fragment_shader2, GL_FRAGMENT_SHADER)

shader2 = compileProgram(cvs2, cfs2)

#tercer shaders
vertex_shader3 = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 ccolor;
uniform mat4 theMatrix;
out vec3 mycolor;
void main() 
{
  gl_Position = theMatrix * vec4(position.x, position.y, position.z, 1);
  mycolor = ccolor;
}
"""

fragment_shader3 = """
#version 460
layout(location = 0) out vec4 fragColor;
uniform int clock;
in vec3 mycolor;
void main()
{
    fragColor = vec4(0.7f ,0.7f ,mycolor.x,1.0f);
}
"""

cvs3 = compileShader(vertex_shader3, GL_VERTEX_SHADER)
cfs3 = compileShader(fragment_shader3, GL_FRAGMENT_SHADER)

shader3 = compileProgram(cvs3, cfs3)

mesh = Obj('./boomFlower.obj')


vertex_data, index_data = load_vertices(mesh)


vertex_buffer_object = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)
glVertexAttribPointer(
    0,  # location
    3,  # size
    GL_FLOAT,  # tipo
    GL_FALSE,  # normalizados
    4 * 9,  # stride
    ctypes.c_void_p(0)
)
glEnableVertexAttribArray(0)

element_buffer_object = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer_object)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes,
             index_data, GL_STATIC_DRAW)

glVertexAttribPointer(
    1,  # location
    3,  # size
    GL_FLOAT,  # tipo
    GL_FALSE,  # normalizados
    4 * 9,  # stride
    ctypes.c_void_p(4 * 3)
)
glEnableVertexAttribArray(1)


def render(rotateX, rotateY, rotateZ, actualShader,scaleC,translatex,translatey,translatez):
    i = glm.mat4(1)

    translate = glm.translate(i, glm.vec3(translatex,translatey,translatez))
    rotate = rotationMatrix((rotateX, rotateY, rotateZ))
    scale = glm.scale(i, glm.vec3(2*scaleC, 2*scaleC, 2*scaleC))

    model = translate * rotate * scale
    view = glm.lookAt(glm.vec3(0, 0, 35), glm.vec3(0, -1, 0), glm.vec3(0, 1, 0))
    projection = glm.perspective(glm.radians(45), ASPECT_RATIO, 0.1, 1000.0)

    theMatrix = projection * view * model

    glUniformMatrix4fv(
        glGetUniformLocation(actualShader, 'theMatrix'),
        1,
        GL_FALSE,
        glm.value_ptr(theMatrix)
    )

#gl glViewport 
glViewport(0, 0, WIDTH, HEIGHT)


rotateX = 0
rotateY = 0
rotateZ = 0
scaleC = 1
translatex = 0
translatey = 0
translatez = 0
a = 0
active_shader = shader

print('''
      Press e to scale up
      Press r to scale down
      Press z to rote z up
      Press x to rote z down
      Press w to rote y up
      Press s to rote y down
      Press d to rote x up
      Press a to rote x down
      Press arrows to move in x and y directions
      Press k to move in positive z
      Press l to move in negative z
      Press f to change shaders
      ''')
running = True
while running:
    glUseProgram(active_shader)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    render(rotateX,rotateY,rotateZ,active_shader,scaleC,translatex,translatey,translatez)
    a += 1

    glUniform1i(
        glGetUniformLocation(active_shader, 'clock'), a
    )

    glDrawArrays(GL_TRIANGLES, 0, len(mesh.faces) * 3)

    pygame.display.flip()
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                rotateZ += 0.1
            elif event.key == pygame.K_x:
                rotateZ -= 0.1
            elif event.key == pygame.K_w:
                rotateY += 0.1
            elif event.key == pygame.K_s:
                rotateY -= 0.1
            elif event.key == pygame.K_d:
                rotateX += 0.1
            elif event.key == pygame.K_a:
                rotateX -= 0.1
            elif event.key == pygame.K_e:
                scaleC += 1
            elif event.key == pygame.K_r:
                scaleC -= 1
                if scaleC == 0:
                    scaleC = 1
            elif event.key == pygame.K_UP:
                translatey += 1
                if translatey >= 13:
                    translatey = 12
            elif event.key == pygame.K_DOWN:
                translatey -= 1
                if translatey <= -13:
                    translatey = -12
            elif event.key == pygame.K_RIGHT:
                translatex += 1
                if translatex >= 24:
                    translatex = 23
            elif event.key == pygame.K_LEFT:
                translatex -= 1
                if translatex <= -24:
                    translatex = -23
                    
            elif event.key == pygame.K_k:
                translatez += 1
                if translatez >= 24:
                    translatez = 23
            elif event.key == pygame.K_l:
                translatez -= 1
                if translatez <= -24:
                    translatez = -23
                
            elif event.key == pygame.K_f:
                #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                if active_shader == shader:
                    active_shader = shader2
                elif active_shader == shader2:
                    active_shader = shader3
                elif active_shader == shader3:
                    active_shader = shader