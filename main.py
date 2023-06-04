import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello World!')

points = []

class Point:
  def __init__(self, pos, colour):
    self.pos = pos
    self.colour = colour

for i in range(100):
  for j in range(100):
    #points.append(Point((i*4, j*4), (i/100*255, j/100*255, 0)))
    points.append(Point((4*i, 4*j), (0, 0, 0)))

def frame():
  for point in points:
    pygame.draw.circle(screen, point.colour, (point.pos[0]+2, point.pos[1]+2), 2)
  pygame.display.update()
