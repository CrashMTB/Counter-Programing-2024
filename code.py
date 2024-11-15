from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration  # Get acceleration along X, Y, Z axes
    if x > 5:
        cp.pixels[1,2,3] = (0,1,0)
    elif x < -5:
        cp.pixels[6,7,8] = (0,1,0)
