    from adafruit_circuitplayground import cp
    import time
    cp.pixels.brightness = .01

    while True:
        if cp.light <= 30:  # Adjust threshold for sensitivity to darkness
            cp.pixels[0] = (0,255,0)

        if    cp.light <= 27:
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)

        if  cp.light  <= 24: 
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)

        if  cp.light  <= 21: 
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)

        if  cp.light  <= 18: 
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)
            cp.pixels[4] = (0,255,0)

        if  cp.light  <= 15: 
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)
            cp.pixels[4] = (0,255,0)
            cp.pixels[5] = (0,255,0) 

        if  cp.light  <= 12: 
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)
            cp.pixels[4] = (0,255,0)
            cp.pixels[5] = (0,255,0)
            cp.pixels[6] = (0,255,0)

        if  cp.light  <= 9 :   
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)
            cp.pixels[4] = (0,255,0)
            cp.pixels[5] = (0,255,0)
            cp.pixels[6] = (0,255,0)
            cp.pixels[7] = (0,255,0)

        if  cp.light  <= 6 :  
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)
            cp.pixels[4] = (0,255,0)
            cp.pixels[5] = (0,255,0)
            cp.pixels[6] = (0,255,0)
            cp.pixels[7] = (0,255,0)
            cp.pixels[8] = (0,255,0)

        if  cp.light  <= 3 :  
            cp.pixels[0] = (0,255,0) #light 1,0,0 red, 0,1,0 green, 0,0,1 blue
            cp.pixels[1] = (0,255,0)
            cp.pixels[2] = (0,255,0)
            cp.pixels[3] = (0,255,0)
            cp.pixels[4] = (0,255,0)
            cp.pixels[5] = (0,255,0)
            cp.pixels[6] = (0,255,0)
            cp.pixels[7] = (0,255,0)
            cp.pixels[8] = (0,255,0)
            cp.pixels[9] = (0,255,0)
        if cp.light > 10:  # Adjust threshold for sensitivity to darkness
            cp.pixels.fill((0,0,0))
