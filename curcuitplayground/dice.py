import time
import random
from adafruit_circuitplayground import cp

# Set the number of pixels on the Circuit Playground (10 pixels)
num_pixels = 10

# Define a function to select a random pixel
def light_random_pixel():
    # Select a random pixel index (from 0 to 9)
    pixel_index = random.randint(0, num_pixels - 1)
    
    # Set the random pixel to a random color (Red, Green, Blue)
    cp.pixels[pixel_index] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Run the function to light a random pixel
while True:
    if cp.button_a:
        cp.pixels.fill(0,0,0)
        light_random_pixel()
        while cp.button_a:  # Wait until button is released
            pass
    


    if cp.button_b:
        cp.pixels[0] = (0,0,0) 
        cp.pixels[1] = (0,0,0)
        cp.pixels[2] = (0,0,0)
        cp.pixels[3] = (0,0,0)
        cp.pixels[4] = (0,0,0)
        cp.pixels[5] = (0,0,0)
        cp.pixels[6] = (0,0,0)
        cp.pixels[7] = (0,0,0)
        cp.pixels[8] = (0,0,0)
        cp.pixels[9] = (0,0,0)
