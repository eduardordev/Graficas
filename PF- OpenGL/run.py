from math import sin
from func import *
import numpy as np
from render import *


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
    
    CONTROLES:

      Press c to scale up
      Press v to scale down
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

executing = True
while executing:
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

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            running = False
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_z:
                rotateZ += 0.1
            elif action.key == pygame.K_x:
                rotateZ -= 0.1
            elif action.key == pygame.K_w:
                rotateY += 0.1
            elif action.key == pygame.K_s:
                rotateY -= 0.1
            elif action.key == pygame.K_d:
                rotateX += 0.1
            elif action.key == pygame.K_a:
                rotateX -= 0.1
            elif action.key == pygame.K_c:
                scaleC += 1
            elif action.key == pygame.K_v:
                scaleC -= 1
                if scaleC == 0:
                    scaleC = 1
            elif action.key == pygame.K_UP:
                translatey += 1
                if translatey >= 13:
                    translatey = 12
            elif action.key == pygame.K_DOWN:
                translatey -= 1
                if translatey <= -13:
                    translatey = -12
            elif action.key == pygame.K_RIGHT:
                translatex += 1
                if translatex >= 24:
                    translatex = 23
            elif action.key == pygame.K_LEFT:
                translatex -= 1
                if translatex <= -24:
                    translatex = -23
                    
            elif action.key == pygame.K_k:
                translatez += 1
                if translatez >= 24:
                    translatez = 23
            elif action.key == pygame.K_l:
                translatez -= 1
                if translatez <= -24:
                    translatez = -23
                
            elif action.key == pygame.K_f:
                #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                if active_shader == shader:
                    active_shader = shader2
                elif active_shader == shader2:
                    active_shader = shader3
                elif active_shader == shader3:
                    active_shader = shader