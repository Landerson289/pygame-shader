import pygame
import distances
import shader

#pygame.init()
#screen = pygame.display.set_mode((400, 300))
#pygame.display.set_caption('Hello World!')

### WHEN REWRITING INTO C# USE INHERITANCE TO HAVE A PARENT 'OBJECT' CLASS WITH CIRCLE, SQUARE, ETC CHILD CLASSES
class Circle:
  def __init__(self, dFunc, centre, sprite, colour, radius):
    self.distanceFunc = dFunc
    self.centre = centre
    self.screenPos = (centre[0] - radius, centre[1] - radius)
    self.sprite = pygame.image.load(sprite)
    self.radius = radius
    self.sprite = pygame.transform.scale(self.sprite, (2*radius, 2*radius))
    var = pygame.PixelArray(self.sprite)
    var.replace((0,0,0), colour)
    self.colour = colour
    del var


def displayObjects(objects):
  for pixel in shader.points:
    for object in objects:
      if distances.circleToPoint(pixel.pos, object.centre, object.radius) <= 0:
        pixel.colour = (255,255,255)



objects = [Circle(distances.circleToPoint, [100,100], "circle.png", (0,0,0), 100), Circle(distances.circleToPoint, [100,100], "circle.png", (0,0,0), 100)]
