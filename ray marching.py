def marchingCircles(startPoint, objects, direction):
  ### Calculate distance to nearest object
  ### Move point that distance in the direction
  ### Repeat with new point
  ### If distance approaches 0 then collision is true
  pass

def getOverlap(objects):
  for pixel in shader.points:
    ### Calculate the distances between the objects and append to a list
    distanceList = []
    for object in objects:
      distance = distances.circleToPoint(pixel.pos, object.centre, object.radius)
      distanceList.append(distance)
    ### Get the max of the two points
    distance = max(distanceList)
    ### if max is less than zero then its in the overlap 
    if distance <= 0:
      pixel.colour = (255,255,255)

def getCombination(objects):
  for pixel in shader.points:
    ### Calculate the distances between the objects and append to a list
    distanceList = []
    for object in objects:
      distance = distances.circleToPoint(pixel.pos, object.centre, object.radius)
      distanceList.append(distance)
    #print(distanceList)
    ### Get the min of the two points
    distance = min(distanceList)
    ### if max is less than zero then its in the overlap 
    if distance <= 0:
      pixel.colour = (255,255,255)

def getSmoothedCombination(objects):
  for pixel in shader.points:
    ### Calculate the distances between the objects and append to a list
    distanceList = []
    for object in objects:
      distance = distances.circleToPoint(pixel.pos, object.centre, object.radius)
      distanceList.append(distance)
    ### Get the max (or min) of the two points
    distance = smoothMin(distanceList[0], distanceList[1])
    ### if smoothmin is less than zero then its in the overlap 
    if distance <= 0:
      pixel.colour = (255,255,255)
