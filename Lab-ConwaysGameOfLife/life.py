import pygame
import random

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
                cell = self.prev_gen.get_at((px_x, px_y))
                neighbors = []
                alive_px = 0
                dead_px = 0

                try:
                    n1 = self.prev_gen.get_at(px_x+1, px_y)
                    neighbors.append(n1)
                except:
                    pass

                try:
                    n2 = self.prev_gen.get_at(px_x-1, px_y)
                    neighbors.append(n2)
                except:
                    pass

                try:
                    n3 = self.prev_gen.get_at(px_x, px_y+1)
                    neighbors.append(n3)
                except:
                    pass

                try:
                    n4 = self.prev_gen.get_at(px_x, px_y-1)
                    neighbors.append(n4)
                except:
                    pass

                try:
                    n5 = self.prev_gen.get_at(px_x+1, px_y+1)
                    neighbors.append(n5)
                except:
                    pass

                try:
                    n6 = self.prev_gen.get_at(px_x+1, px_y-1)
                    neighbors.append(n6)
                except:
                    pass

                try:
                    n7 = self.prev_gen.get_at(px_x-1, px_y+1)
                    neighbors.append(n7)
                except:
                    pass

                try:
                    n8 = self.prev_gen.get_at(px_x-1, px_y-1)
                    neighbors.append(n8)
                except:
                    pass

                for nb in neighbors:
                    if nb[0] == 0:
                        dead_px += 1
                    else:
                        alive_px += 1

                if alive_px < 2 and cell[0] == isAlive:
                    self.pixel(px_x, px_y, BLACK)

                if alive_px >= 2 or alive_px <= 3 and cell[0] == isAlive:
                    self.pixel(px_x, px_y, WHITE)

                if alive_px > 3 and cell[0] == isAlive:
                    self.pixel(px_x, px_y, BLACK)

                if alive_px == 3 and cell[0] == isDead:
                    self.pixel(px_x, px_y, WHITE)



pygame.init()
screen = pygame.display.set_mode((500, 500))

r = Life(screen)

r.pixel(25,64, WHITE)
r.pixel(26,65, WHITE)
r.pixel(24,63, WHITE)

r.pixel(50,120, WHITE)
r.pixel(51,121, WHITE)
r.pixel(49,119, WHITE)

r.pixel(135,150, WHITE)
r.pixel(136,151, WHITE)
r.pixel(134,149, WHITE)


while True:
  
  r.copy()
  r.clear()
  r.render()
  

  pygame.display.flip()