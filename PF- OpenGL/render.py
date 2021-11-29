import pygame
from func import *
from obj import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glm

HEIGHT = 800
WIDTH = 800
ASPECT_RATIO = WIDTH/HEIGHT


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)

glClearColor(0.1, 0.2, 0.8, 1.0)
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
    fragColor = vec4(mycolor.x,0.5f, 1.8f,1.0f);
}
"""

cvs2 = compileShader(vertex_shader2, GL_VERTEX_SHADER)
cfs2 = compileShader(fragment_shader2, GL_FRAGMENT_SHADER)

shader2 = compileProgram(cvs2, cfs2)

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
    fragColor = vec4(0.7f ,0.9f ,mycolor.x,1.0f);
}
"""

cvs3 = compileShader(vertex_shader3, GL_VERTEX_SHADER)
cfs3 = compileShader(fragment_shader3, GL_FRAGMENT_SHADER)

shader3 = compileProgram(cvs3, cfs3)

mesh = Obj('./boomFlower.obj')

vertex_data, index_data = load_vortex(mesh)

vertex_buffer_object = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

vertex_array_object = glGenVertexArrays(1)
glBindVertexArray(vertex_array_object)
glVertexAttribPointer(
    0,  
    3,  
    GL_FLOAT,  
    GL_FALSE,  
    4 * 9,  
    ctypes.c_void_p(0)
)
glEnableVertexAttribArray(0)

element_buffer_object = glGenBuffers(1)
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer_object)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes,
             index_data, GL_STATIC_DRAW)

glVertexAttribPointer(
    1,  
    3,  
    GL_FLOAT,  
    GL_FALSE,  
    4 * 9,  
    ctypes.c_void_p(4 * 3)
)
glEnableVertexAttribArray(1)
