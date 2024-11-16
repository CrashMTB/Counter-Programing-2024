from adafruit_circuitplayground import cp

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    if temp_f < 0:  # Example threshold for cold
        cp.pixels[0] = (1, 0, 0)# Blue for cold
    if temp_f > 10:   
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
    if temp_f > 20: 
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)

    if temp_f > 30:  
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
    if temp_f > 40:    
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
        cp.pixels[4] = (20, 0, 0)
    if temp_f > 50:    
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
        cp.pixels[4] = (20, 0, 0)
        cp.pixels[5] = (25, 0, 0) 
    if temp_f > 60:    
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
        cp.pixels[4] = (20, 0, 0)
        cp.pixels[5] = (25, 0, 0) 
        cp.pixels[6] = (30, 0, 0)    
    if temp_f > 70:    
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
        cp.pixels[4] = (20, 0, 0)
        cp.pixels[5] = (25, 0, 0) 
        cp.pixels[6] = (30, 0, 0) 
        cp.pixels[7] = (35, 0, 0)
    if temp_f > 80:
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
        cp.pixels[4] = (20, 0, 0)
        cp.pixels[5] = (25, 0, 0) 
        cp.pixels[6] = (30, 0, 0) 
        cp.pixels[7] = (35, 0, 0)
        cp.pixels[8] = (45, 0, 0)
    if temp_f > 90:
        cp.pixels[0] = (1, 0, 0)
        cp.pixels[1] = (5, 0, 0)
        cp.pixels[2] = (10, 0, 0)
        cp.pixels[3] = (15, 0, 0) 
        cp.pixels[4] = (20, 0, 0)
        cp.pixels[5] = (25, 0, 0) 
        cp.pixels[6] = (30, 0, 0) 
        cp.pixels[7] = (35, 0, 0)
        cp.pixels[8] = (45, 0, 0)
        cp.pixels[9] = (50, 0, 0)