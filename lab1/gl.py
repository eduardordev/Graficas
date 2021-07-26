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

class Render(object):
    def __init__(self,width,height):
        self.width= width
        self.height=height
        self.current_color = WHITE
        self.Clear()
  
    def Clear(self):
        self.framebuffer = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

    def Write(self,filename):
        f = open(filename, 'bw')
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


        f.close()

    def render(self):
        self.Write('a.bmp')

    def point(self,x,y,color=None):
        self.framebuffer[y][x]  = color or self.current_color

r = Render(1024,768)

r.point(300,200,color(255,255,255))


r.render()