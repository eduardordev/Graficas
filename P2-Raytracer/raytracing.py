from libreria import *
from random import random
from math import pi,tan
from formas import *
from obj import *

MAX_RECURSION_DEPTH = 3
class Raytracer(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.current_color= WHITE
        self.background_color= BLACK
        self.scene=[]
        self.light= None
        self.clear()
    
    def clear(self):
        self.framebuffer=[
            [BLACK for _ in range(self.width)]
            for _ in range(self.height)
        ]
    
    def point(self, x, y, color=None):
        try:
            self.framebuffer[y][x] = color or self.current_color
        except:
            pass
        
    def cast_ray(self, origin, direction,recursion=0):
        material, intersect = self.scene_intersect(origin, direction)

        if material is None or recursion >= MAX_RECURSION_DEPTH:
            return self.background_color
        
        light_dir = norm(sub(self.light.position, intersect.point))
        #shadow ray
        offset_normal = mul(intersect.normal,1.1) #shadow bias
        shadow_origin= suma(intersect.point,offset_normal) if dot(light_dir,intersect.normal) > 0 else sub(intersect.point,offset_normal)
        
        shadow_material,shadow_intersect= self.scene_intersect(shadow_origin,light_dir)
        if shadow_material is None:
            shadow_intensity = 0
        else:
            shadow_intensity = 0.9
        
        
        if material.albedo[2]>0:
            reverse_direction = mul(direction,-1)
            reflect_direction = reflect(reverse_direction,intersect.normal)
            reflect_origin = suma(intersect.point,offset_normal) if dot(reflect_direction,intersect.normal) > 0 else sub(intersect.point,offset_normal)
            
            reflect_color=self.cast_ray(reflect_origin,reflect_direction, recursion + 1)
        else:
            reflect_color = BLACK
            
            
        if material.albedo[3]>0:
            refract_direction = refract(direction,intersect.normal,material.refractive_index)
            if refract_direction is None:
                refraction_color = BLACK
            else :
                refract_origin = suma(intersect.point,offset_normal) if dot(refract_direction,intersect.normal) > 0 else sub(intersect.point,offset_normal)
            
                refraction_color=self.cast_ray(refract_origin,refract_direction, recursion + 1)
        else:
            refraction_color = BLACK
            
            
        diffuse_intensity = self.light.intensity * max(0, dot(light_dir, intersect.normal)) * (1-shadow_intensity)
        
        if shadow_intensity > 0:
            specular_intensity = 0
        else:
            specular_reflection =reflect(light_dir,intersect.normal)
            specular_intensity = self.light.intensity * (max(0,dot(specular_reflection,direction))**material.spec)
            
        
        
        diffuse = material.diffuse * diffuse_intensity * material.albedo[0]
        specular = self.light.color * specular_intensity * material.albedo[1]
        reflection=  reflect_color * material.albedo[2]
        refraction = refraction_color * material.albedo[3]
        
        if material.texture and intersect.text_coords is not None:
            text_color = material.texture.get_color(intersect.text_coords[0], intersect.text_coords[1])
            diffuse = text_color * 255
        c = diffuse + specular + reflection + refraction
        return c

    def scene_intersect(self,origin,direction):
        zbuffer=float('inf')
        material=None
        intersect=None
        for obj in self.scene:
            r_intersect= obj.ray_intersects(origin,direction)
            if r_intersect:
                if r_intersect.distance < zbuffer:
                    zbuffer = r_intersect.distance
                    material= obj.material
                    intersect=r_intersect
        return material,intersect
    def Load(self, filename, translate, scale):
        model = Obj(filename)        
        triangles_vertex = []
        
        for face in model.faces:
            f1 = face[0][0] - 1
            f2 = face[1][0] - 1
            f3 = face[2][0] - 1
            
            A = Transform(model.vertices[f1], translate, scale)
            B = Transform(model.vertices[f2], translate, scale)
            C = Transform(model.vertices[f3], translate, scale)
            triangles_vertex.append([A, B, C])
            
        return triangles_vertex
    def render(self):
        #form of view
        fov = pi/2
        
        #aspect ratio
        ar = (self.width/self.height)
        for y in range(self.height):
            for x in range(self.width):
                if random()> 0.5:
                    
                    i= 2 * ((x + 0.5) / self.width) - 1 * ar * tan(fov/2)
                    j= 1-2 * ((y + 0.5) / self.height) * tan(fov/2)
                    
                    direction= norm(V3(i,j,-1))
                    col=self.cast_ray(V3(0,0,0),direction)
                    self.point(x, y, color=col)
                

    def write(self,filename):
        WriteBMP(filename+'.bmp',self.width,self.height,self.framebuffer)