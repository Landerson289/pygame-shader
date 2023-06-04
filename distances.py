import math as maths

def points(point1, point2):
  dx = point1[0] - point2[0]
  dy = point1[1] - point2[1]
  d = maths.sqrt(dx**2 + dy**2)
  return d

def circleToPoint(point, centre, radius):
  d = points(point, centre) - radius
  return d

def circles(centre1, radius1, centre2, radius2):
  d = points(centre1, centre2) - radius1 - radius2
  return d
  
