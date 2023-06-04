# pygame-shader
This is a simple shader made for pygame which I made quickly to aid me with another project, hence the inefficient and unorganised nature of the code. 

## display
main.py handles the display work. It has a Point class which has the colour and location of the point. This would be better named pixel but I was in a rush. It has a list of 10,000 of these points evenly distributed in a grid shape on the screen. These are all 4 in diameter. These are all assigned black at first. frame() loops through this list of points and draws them all to a screen and updates pygame.

## object rendering
It can only handle circles at the moment. These are defined by a circle class which takes in all the properties of the circle. Every object in the scene should be in the objects list which is passed into an "object render" function which loops through all the pixels and objects to check if the signed distance between every pixel and the object is negative and if so will set the pixel's colour to white (this should be updated to change it to the colour of the object). 
