from adafruit_circuitplayground import cp
import time
#cp.pixels.brightness = .01

while True:      #everything goes in here
    #how to interact with pixel
    #0-255
    cp.pixels[0] = (100,0,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
    cp.pixels[1] = (100,0,0)
    cp.pixels[2] = (100,0,0)
    cp.pixels[3] = (100,0,0)
    cp.pixels[4] = (100,0,0)
    cp.pixels[5] = (100,0,0)
    cp.pixels[6] = (100,0,0)
    cp.pixels[7] = (100,0,0)
    cp.pixels[8] = (100,0,0)
    cp.pixels[9] = (100,0,0)
    cp.play_tone(500, 0.75)  # Plays a 440 Hz tone (A4) for 1 second
ads
    time.sleep(0.5)
    cp.pixels[0] = (0,0,100) 
    cp.pixels[1] = (0,0,100)
    cp.pixels[2] = (0,0,100)
    cp.pixels[3] = (0,0,100)
    cp.pixels[4] = (0,0,100)
    cp.pixels[5] = (0,0,100)
    cp.pixels[6] = (0,0,100)
    cp.pixels[7] = (0,0,100)
    cp.pixels[8] = (0,0,100)
    cp.pixels[9] = (0,0,100)
    cp.play_tone(900, 0.75)
    time.sleep(0.5)
   
    #cp.pixels.fill((0, 1, 0))

