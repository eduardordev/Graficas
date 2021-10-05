from drawengine import *

def gourad(render, **kwargs):
    w, v, u = kwargs['bar']
    tx, ty = kwargs['tex_coords']
    nA, nB, nC = kwargs['varying_normales']
    
    tcolor = render.current_texture.get_color(tx, ty)

    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def simple_shading(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(241, 180, 109)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity


def simple_shadingtv(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(23, 40, 166)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity
pi = 3.14

r = Renderer(1000, 1000)
r.lookAt(V3(0, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
    
r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/dragonite.obj', (0, 0.2, 0), (0.2, 0.5, 0.2), (0, 0, 0))
r.active_shader = simple_shading
r.draw_arrays('TRIANGLES')

r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/tv.obj', (0, -0.8, 0), (0.5, 1, 0.5), (0, 0, 0))
r.active_shader = simple_shadingtv
r.draw_arrays('TRIANGLES')

r.render()
