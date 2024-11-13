from adafruit_circuitplayground import cp

while True:
    x, y, z= cp.acceleration  # Get acceleration along X, Y, Z axes
    if x > 5:
        cp.pixels[1] = (0,1,0)
        cp.pixels[2] = (0,1,0)
        cp.pixels[3] = (0,1,0)
    elif x < -5:
        cp.pixels[6] = (0,1,0)
        cp.pixels[7] = (0,1,0)
        cp.pixels[8] = (0,1,0)
    else:
        cp.pixels.fill((0,0,0))
