from adafruit_circuitplayground import cp
import time
import random


while True:  
    cp.pixels.brightness = 0.1    #everything goes in here
    x, y, z = cp.acceleration  # Get acceleration along X, Y, Z axes
    shake_threshold = 15.0  # Example threshold value
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        
        cp.pixels[0] = (random.randint(0,256),random.randint(0,256),random.randint(0,256)) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
        cp.pixels[1] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[2] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[3] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[4] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[5] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[6] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[7] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[8] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
        cp.pixels[9] = (random.randint(0,256),random.randint(0,256),random.randint(0,256))
