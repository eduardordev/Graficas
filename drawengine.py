from os import write
import struct

#escribir en bytes
def char(c):
    return struct.pack('=c',c.encode('ascii'))

#escribir en bytes
def word(w):
    #short
    return struct.pack('=h',w)

#escribir en bytes
def dword(w):
    #long
    return struct.pack('=l',w)


def color(r,g,b):
    return bytes([b,g,r])


BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Renderer(object):

    #Constructor
    def __init__(self, width, height):
        self.current_color = WHITE
        self.clear_color = BLACK
        self.glCreateWindow(width, height)
        
    def glCreateWindow(self, width, height):
        self.width= width
        self.height=height
        self.framebuffer = [
                [BLACK for x in range(self.width)]
                for y in range(self.height)
            ]
    
    def glViewport(self, x, y, width, height):
        self.viewportx = x
        self.viewporty = y
        self.vwidth = width
        self.vheight = height

    def glClear(self):
        self.fill_pixels = [[self.clear_color for y in range(
            self.height)] 
            for x in range(self.width)]

    def glClearColor(self, r, g, b):
        self.clear_color=color(r,g,b)    

    def glColor(self, r, g, b):
        self.current_color = color(r,g,b)

    def glPoint(self,x,y,color=None):
        self.framebuffer[y][x]  = color or self.current_color

    def glFinish(self, filename):
        with open(filename, "bw") as f:
        #file header 14 bytes
            f.write(char('B'))
            f.write(char('M'))
            f.write(dword(14 + 40 + 3 *(self.width * self.height)))
            f.write(dword(0))
            f.write(dword(14 + 40))

            #info header 40 bytes
            f.write(dword(40))
            f.write(dword(self.width))
            f.write(dword(self.height))
            f.write(word(1))
            f.write(word(24))
            f.write(dword(0))
            f.write(dword( 3 *(self.width * self.height)))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #bitmap
            for y in range(self.height):
                for x in range(self.width):
                    f.write(self.framebuffer[y][x])


width = 1024
height = 768

rend = Renderer(width, height)

rend.glClearColor(255,255,255)
rend.glClear()

rend.glColor(0,0,0)

rend.glPoint(512,384,color(255,255,255))
rend.glPoint(512,389,color(255,255,255))
rend.glPoint(512,379,color(255,255,255))
rend.glPoint(512,394,color(255,255,255))
rend.glPoint(512,374,color(255,255,255))
rend.glPoint(512,399,color(255,255,255))
rend.glViewport(100, 100, 400, 400)

rend.glFinish("point.bmp")