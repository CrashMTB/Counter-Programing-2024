from adafruit_circuitplayground import cp
import time
import random

# Set the brightness for all LEDs
cp.pixels.brightness = 0.1

# Set a shake detection threshold (this may need fine-tuning)
shake_threshold = 15.0

# Variable to track if the LEDs were already updated
colors_updated = False

while True:
    # Get the current acceleration values along X, Y, Z axes
    x, y, z = cp.acceleration

    # Check if the movement exceeds the threshold
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        # Only update the LEDs if they haven't been updated already after the last shake
        if not colors_updated:
            # Update each LED with a random color
            for i in range(10):
                cp.pixels[i] = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            # Mark that the LEDs have been updated
            colors_updated = True

        # Small delay to debounce the shake detection (adjust this if needed)
        time.sleep(0.1)
    
    # If there's no shake, reset the update flag so that it can be updated next time
    else:
        colors_updated = False
