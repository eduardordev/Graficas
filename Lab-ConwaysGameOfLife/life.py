import random
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)

isAlive = 255
isDead = 0


class Life(object):
    def __init__(self, screen):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen

    def clear(self):
        self.screen.fill((0, 0, 0))

    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_gen = self.screen.copy()
        


    def render(self):
        for px_x in range(self.width):
            for px_y in range(self.height):
                cell = self.prev_gen.get_at((px_x, px_y))[0]
                neighbors = []
                alive_px = 0
                dead_px = 0

                try:
                    n1 = self.prev_gen.get_at((px_x+1, px_y))
                    neighbors.append(n1)  
                except:
                    pass

                try:
                    n2 = self.prev_gen.get_at((px_x-1, px_y))
                    neighbors.append(n2)
                except:
                    pass

                try:
                    n3 = self.prev_gen.get_at((px_x, px_y+1))
                    neighbors.append(n3)
                except:
                    pass

                try:
                    n4 = self.prev_gen.get_at((px_x, px_y-1))
                    neighbors.append(n4)
                except:
                    pass

                try:
                    n5 = self.prev_gen.get_at((px_x+1, px_y+1))
                    neighbors.append(n5)
                except:
                    pass

                try:
                    n6 = self.prev_gen.get_at((px_x+1, px_y-1))
                    neighbors.append(n6)
                except:
                    pass

                try:
                    n7 = self.prev_gen.get_at((px_x-1, px_y+1))
                    neighbors.append(n7)
                except:
                    pass

                try:
                    n8 = self.prev_gen.get_at((px_x-1, px_y-1))
                    neighbors.append(n8)
                    
                except:
                    pass
                
                
                for nb in neighbors:
                    
                    if nb[0] == 0:
                        dead_px += 1
                    else:
                        alive_px += 1
                
                

                if alive_px < 2 and cell == isAlive:
                    self.pixel(px_x, px_y, BLACK)

                if (alive_px == 2 or alive_px == 3) and cell == isAlive:
                    self.pixel(px_x, px_y, WHITE)

                if alive_px > 3 and cell == isAlive:
                    self.pixel(px_x, px_y, BLACK)

                if alive_px == 3 and cell == isDead:
                    self.pixel(px_x, px_y, WHITE)


pygame.init()
screen = pygame.display.set_mode((200, 200))

r = Life(screen)

pixels = random.randint(1,10000)

for i in range(pixels):
    
    px = random.randint(1,200)
    py = random.randint(1,200)

    print(px,py)
    r.pixel(px,py,WHITE)

#Lineas simples

r.pixel(80,49,WHITE)
r.pixel(80,50,WHITE)
r.pixel(80,51,WHITE)

r.pixel(40,79,WHITE)
r.pixel(40,80,WHITE)
r.pixel(40,81,WHITE)

r.pixel(140,179,WHITE)
r.pixel(140,180,WHITE)
r.pixel(140,181,WHITE)

#Forma loca

r.pixel(25,65,WHITE)
r.pixel(26,66,WHITE)
r.pixel(27,66,WHITE)

r.pixel(28,65,WHITE)
r.pixel(26,64,WHITE)
r.pixel(27,64,WHITE)

r.pixel(24,64,WHITE)
r.pixel(24,63,WHITE)

r.pixel(24,66,WHITE)
r.pixel(24,67,WHITE)

r.pixel(23,63,WHITE)
r.pixel(23,67,WHITE)

r.pixel(23,68,WHITE)
r.pixel(23,62,WHITE)

r.pixel(22,68,WHITE)
r.pixel(22,62,WHITE)

r.pixel(21,69,WHITE)
r.pixel(21,61,WHITE)

r.pixel(20,68,WHITE)
r.pixel(20,62,WHITE)

r.pixel(19,68,WHITE)
r.pixel(19,62,WHITE)
r.pixel(19,67,WHITE)
r.pixel(19,63,WHITE)
r.pixel(19,66,WHITE)
r.pixel(19,64,WHITE)

#Forma loca 1

r.pixel(125,165,WHITE)
r.pixel(126,166,WHITE)
r.pixel(127,166,WHITE)

r.pixel(128,165,WHITE)
r.pixel(126,164,WHITE)
r.pixel(127,164,WHITE)

r.pixel(124,164,WHITE)
r.pixel(124,163,WHITE)

r.pixel(124,166,WHITE)
r.pixel(124,167,WHITE)

r.pixel(123,163,WHITE)
r.pixel(123,167,WHITE)

r.pixel(123,168,WHITE)
r.pixel(123,162,WHITE)

r.pixel(122,168,WHITE)
r.pixel(122,162,WHITE)

r.pixel(121,169,WHITE)
r.pixel(121,161,WHITE)

r.pixel(120,168,WHITE)
r.pixel(120,162,WHITE)

r.pixel(119,168,WHITE)
r.pixel(119,162,WHITE)
r.pixel(119,167,WHITE)
r.pixel(119,163,WHITE)
r.pixel(119,166,WHITE)
r.pixel(119,164,WHITE)

#cubo loco

r.pixel(85, 35,WHITE)
r.pixel(86,35,WHITE)
r.pixel(87,35,WHITE)

r.pixel(84,36,WHITE)
r.pixel(83,35,WHITE)

r.pixel(84,34,WHITE)
r.pixel(84,33,WHITE)
r.pixel(84,32,WHITE)

r.pixel(83,31,WHITE)
r.pixel(84,30,WHITE)

#cubo loco

r.pixel(165, 115,WHITE)
r.pixel(166,115,WHITE)
r.pixel(167,115,WHITE)

r.pixel(164,116,WHITE)
r.pixel(163,115,WHITE)

r.pixel(164,114,WHITE)
r.pixel(164,113,WHITE)
r.pixel(164,112,WHITE)

r.pixel(163,111,WHITE)
r.pixel(164,110,WHITE)


#adn loco

r.pixel(45,142, WHITE)
r.pixel(45,143, WHITE)
r.pixel(46,143, WHITE)

r.pixel(45,150, WHITE)
r.pixel(46,150, WHITE)
r.pixel(45,151, WHITE)

r.pixel(47,144, WHITE)
r.pixel(47,145, WHITE)
r.pixel(48,145, WHITE)

r.pixel(47,148, WHITE)
r.pixel(48,148, WHITE)
r.pixel(47,149, WHITE)

r.pixel(49,146, WHITE)
r.pixel(49,147, WHITE)
r.pixel(50,146, WHITE)
r.pixel(50,147, WHITE)

r.pixel(51,144, WHITE)
r.pixel(51,145, WHITE)
r.pixel(52,144, WHITE)
r.pixel(52,145, WHITE)

r.pixel(51,148, WHITE)
r.pixel(51,149, WHITE)
r.pixel(52,148, WHITE)
r.pixel(52,149, WHITE)

r.pixel(53,143, WHITE)
r.pixel(54,143, WHITE)

r.pixel(53,146, WHITE)
r.pixel(53,147, WHITE)
r.pixel(54,146, WHITE)
r.pixel(54,147, WHITE)

r.pixel(53,150, WHITE)
r.pixel(54,150, WHITE)

r.pixel(55,144, WHITE)
r.pixel(55,145, WHITE)
r.pixel(56,144, WHITE)
r.pixel(56,145, WHITE)

r.pixel(55,148, WHITE)
r.pixel(55,149, WHITE)
r.pixel(56,148, WHITE)
r.pixel(56,149, WHITE)

r.pixel(57,146, WHITE)
r.pixel(57,147, WHITE)
r.pixel(58,146, WHITE)
r.pixel(58,147, WHITE)

r.pixel(60,144, WHITE)
r.pixel(59,145, WHITE)
r.pixel(60,145, WHITE)

r.pixel(59,148, WHITE)
r.pixel(60,148, WHITE)
r.pixel(60,149, WHITE)

r.pixel(62,142, WHITE)
r.pixel(61,143, WHITE)
r.pixel(62,143, WHITE)

r.pixel(61,150, WHITE)
r.pixel(62,150, WHITE)
r.pixel(62,151, WHITE)





while True:
  r.copy()
  r.clear()
  r.render()
  pygame.display.flip()