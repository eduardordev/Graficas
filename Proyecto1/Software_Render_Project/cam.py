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

def simple_shading_rocket(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(255, 0, 0)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def simple_shading_mew(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(249, 219, 227)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def simple_shading_chair(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(230, 227, 165)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

def simple_shading_carpet(render, **kwargs):
    w, v, u = kwargs['bar']
    nA, nB, nC = kwargs['varying_normales']
    A, B, C = kwargs['triangle']

    tcolor = color(255, 245, 134)
    
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    
    intensity = w*iA + v*iB + u*iC
    
    return tcolor * intensity

pi = 3.14

r = Renderer(1000, 1000)
r.lookAt(V3(0, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
    
r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/dragonite.obj', (0.3, 0.2, 0), (0.08, 0.2, 0.05), (0, -pi/4, 0))
r.active_shader = simple_shading
r.draw_arrays('TRIANGLES')

r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/tv.obj', (0.5, -0.4, 0), (0.25, 0.6, 0.1), (0, -pi/4, 0))
r.active_shader = simple_shadingtv
r.draw_arrays('TRIANGLES')

r.current_texture = None
r.light = V3(-0.3, -0.3, 0.4)
r.load('./models/rocket.obj', (-0.5, -0.4, 0), (0.1, 0.6, 0.1), (0, pi/3, 0))
r.active_shader = simple_shading_rocket
r.draw_arrays('TRIANGLES')

r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/mew.obj', (0.6, 0.2, 0), (0.08, 0.2, 0.05), (0, -pi/4, 0))
r.active_shader = simple_shading_mew
r.draw_arrays('TRIANGLES')

r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/armchair.obj', (0, 0, 0), (0.1, 0.6, 0.1), (0, pi/3, 0))
r.active_shader = simple_shading_chair
r.draw_arrays('TRIANGLES')

r.current_texture = None
r.light = V3(0.3, 0.3, 0.4)
r.load('./models/armchair.obj', (0, 0, -0.6), (0.1, 0.6, 0.1), (0, pi/4, 0))
r.active_shader = simple_shading_carpet
r.draw_arrays('TRIANGLES')

r.render()
