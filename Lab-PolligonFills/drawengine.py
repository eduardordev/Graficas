#UNIVERSIDAD DEL VALLE DE GUATEMALA
#EDUARDO RAMÍREZ HERRERA
#19946
#GRAFICAS POR COMPUTADORA
from os import write
import struct
import math
from queue import Queue

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
    def __init__(self):
        self.current_color = WHITE
        self.clear_color = BLACK
        self.framebuffer = None

    def glCreateWindow(self,width, height):
        self.width= width
        self.height=height
        self.glClear()
        self.glViewport(0,0,self.width,self.height)

    def glClear(self):
        self.framebuffer= [[self.clear_color for y in range(
            self.height)] 
            for x in range(self.width)]

    def glClearColor(self,r, g, b):
        self.clear_color=color(r,g,b)
    
    def glColor(self, r, g, b):
        r=int(r*255)
        g=int(g*255)
        b=int(b*255)
        self.current_color = color(r,g,b)

    #Normalized Device Coordinates coverter
    def NDC(self, x_viewport, y_viewport):
        xw = int((x_viewport + 1) * (self.vwidth  / 2) + self.viewportx)
        yw = int((y_viewport + 1) * (self.vheight / 2) + self.viewporty)
        return xw, yw

    def glViewport(self, x, y, width, height):
        

        self.viewportx = x
        self.viewporty = y
        self.vwidth = width
        self.vheight = height

    def glVertex(self, x_v, y_v, color=None):
        x_window, y_window = self.NDC(x_v, y_v)
        self.framebuffer[ x_window][y_window]=color or self.current_color

    def glVertex_P(self, x_v, y_v, color=None):
        
        self.framebuffer[ y_v][x_v]=color or self.current_color
    def point(self,x,y,color=None):
        x,y=self.NDC(x,y)

        self.framebuffer[y][x]  = color or self.current_color

    def Line(self,x0,y0,x1,y1,color=None):
        if(x0==x1 and y0==y1):
            #self.point(x0,y0)
            x0,y0=self.NDC(x0,y0)
            self.glVertex_P(x0,y0)
            return

        x0,y0=self.NDC(x0,y0)
        x1,y1=self.NDC(x1,y1)
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        m = dy/dx * dx

        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx
        y = y0

        # y = mx + b
        points = []
        for x in range(x0, x1):
            if steep:
                
                points.append((x , y ))
            else:
                
                points.append((y, x ))

            offset += (dy/dx) * 2 * dx 
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += 1 * 2 * dx
        for pointf in points:
            self.glVertex_P(*pointf)

    def Line2(self,x0,y0,x1,y1,color=None):
        if(x0==x1 and y0==y1):
            #self.point(x0,y0)
           
            self.glVertex_P(x0,y0)
            return

        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        m = dy/dx * dx

        offset = 0 * 2 * dx
        threshold = 0.5 * 2 * dx
        y = y0

        # y = mx + b
        points = []
        for x in range(x0, x1+1):
            if steep:
                
                points.append((x , y ))
            else:
                
                points.append((y, x ))

            offset += (dy/dx) * 2 * dx 
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += 1 * 2 * dx

        for pointf in points:
            self.glVertex_P(*pointf)
          
    def borde(self,lstPoints):

        for i in range(len(lstPoints)):
            self.Line(lstPoints[i][0]*0.001, lstPoints[i][1]*0.001, lstPoints[(i+1)%len(lstPoints)][0]*0.001, lstPoints[(i+1)%len(lstPoints)][1]*0.001)
    
    def bordeX(self,listFig):
        for fig in  listFig:
            for i in range(len(fig)):
                #self.Line(fig[i][0]*0.001, fig[i][1]*0.001, fig[(i+1)%len(fig)][0]*0.001, fig[(i+1)%len(fig)][1]*0.001)
                self.Line2(fig[i][0], fig[i][1], fig[(i+1)%len(fig)][0], fig[(i+1)%len(fig)][1])

    def fill(self,x,y,ncolor,old_color):
        
        n = self.width
        m = self.height
       
        if x < 0 or x >= n or y < 0 or y >= m or self.framebuffer[ y][x]!=old_color : return
           
        self.framebuffer[y][x]=ncolor
        self.fill(x+1, y,ncolor,old_color)
        self.fill(x-1, y,ncolor,old_color)
        #self.fill(x, y+1,ncolor,old_color)
        self.fill(x, y-1,ncolor,old_color)
         

    def fill_all(self,x,y,ncolor):
        
        old_color = self.framebuffer[y][x]
        if ncolor == BLACK:
            
            return
        self.fill(x,y,ncolor,old_color)

    def fili(self,x,y,nColor):
        #i,j = self.NDC(x*0.001,y*0.001)
        color1 = WHITE
        n = self.width
        m = self.height
        
        inicio = self.framebuffer[y][x]
        
        if inicio !=color1 and inicio !=nColor:
        
            self.glVertex_P(x,y,nColor)
            self.fili(x+1,y,nColor)
            self.fili(x-1,y,nColor)
            self.fili(x,y+1,nColor)
            self.fili(x,y-1,nColor)

    def fill2(self,x,y,nColor):
        n = self.width
        m = self.height
        old_color = self.framebuffer[y][x]
        if old_color == nColor: return
        queue = Queue()
        queue.put((x, y))
        while not queue.empty():
            i, j = queue.get()
            if i < 0 or i >= n or j < 0 or j >= m or self.framebuffer[j][i] != old_color:
                continue
            else:
                self.glVertex_P(i,j,nColor)
                queue.put((i+1, j))
                queue.put((i-1, j))
                queue.put((i, j+1))
                queue.put((i, j-1))

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
                f.write(self.framebuffer[x][y])


        f.close()

    def glFinish(self,name):
        
        self.Write(name+'.bmp')
       
r= Render()
r.glCreateWindow(900,900)
#r.glViewport(100,100,400,400)
fg1=((165, 380) ,(185, 360) ,(180, 330) ,(207, 345), (233, 330), (230, 360), (250, 380), (220, 385) ,(205, 410) ,(193, 383))
fg2=((321, 335), (288, 286), (339, 251) ,(374, 302))
fg3=((377, 249),(411, 197) ,(436, 249))
fg4=((413, 177), (448, 159), (502, 88) ,(553, 53) ,(535, 36) ,(676, 37) ,(660, 52),(750, 145), (761, 179), (672, 192) ,(659, 214) ,(615, 214) ,(632, 230) ,(580, 230),(597, 215), (552, 214), (517, 144) ,(466, 180))
fg5=((682, 175), (708, 120), (735, 148) ,(739, 170))
lista = [fg1,fg2,fg3,fg4,fg5]
r.bordeX(lista)

new_color = color(174, 214, 241)
new_color1 = color(218, 247, 166)
new_color2 = color(255, 195, 0)
new_color3 = color(255, 87, 51)

r.fill2(225,405,new_color)
r.fill2(290,330,new_color1)
r.fill2(380,200,new_color2)
r.fill2(150,600,new_color3)
r.fill2(150,700,color(255,0,0))

r.glFinish('out_pols')
