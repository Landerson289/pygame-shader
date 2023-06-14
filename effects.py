import copy

def outline():
  points = copy.deepcopy(shader.points)
  
  for pixel in range(len(points)):
    middle = points[pixel]
    if 0 <= pixel%100:
      left = points[pixel-1]
      leftBool = left.colour == middle.colour
    else:
      leftBool = True
      
    if pixel < len(points) - 100:
      up = points[pixel+100]
      upBool = up.colour == middle.colour
    else:
      upBool = True

    if pixel >= 100:
      down = points[pixel-100]
      downBool = down.colour == middle.colour
    else:
      downBool = True

    if pixel%100 < 99:
      right = points[pixel+1]
      rightBool = right.colour == middle.colour
    else:
      rightBool = True
      
    if leftBool and upBool and downBool and rightBool:
      prevPoint = shader.points[pixel].colour
      shader.points[pixel].colour = (0,0,0)
      points[pixel].colour = prevPoint
    else:
      prevPoint = (shader.points[pixel].colour[0], shader.points[pixel].colour[1], shader.points[pixel].colour[2])
      shader.points[pixel].colour = (255,255,255)
      points[pixel].colour = prevPoint
