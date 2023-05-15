### Original code for alternating stripes moving right
# 5/11/23 HP
import time
import board
import neopixel

# Configuration
# Define the number of pixels in each LED matrix
NUM_PIXELS = 256

# Define the number of LED matrices connected
NUM_MATRICES = 6
# Move over by 1 column of pixels(16 pixels)
SKIP_PIXELS = 16
PIXELS_TO_LIGHT = 48
MOVE_DELAY = 0.01  # seconds # EDIT to match angular velocity in literature

# Initialize the LED matrix
pixels = neopixel.NeoPixel(board.NEOPIXEL0, NUM_PIXELS * NUM_MATRICES, brightness=1, auto_write=False)

# Define the current position of the pattern
current_pos = 0

# Define the color of the lit pixels
color = (0, 5, 0)

# Loop forever
while True:
    # Turn off all the pixels
    pixels.fill((0, 0, 0))

    # Loop through the pixels in the pattern and light them up
    for i in range(current_pos, NUM_PIXELS * NUM_MATRICES, PIXELS_TO_LIGHT * 2):
        if i + PIXELS_TO_LIGHT <= NUM_PIXELS * NUM_MATRICES:
            pixels[i:i+PIXELS_TO_LIGHT] = [color] * PIXELS_TO_LIGHT

    # Move the pattern to the right by SKIP_PIXELS
    current_pos += SKIP_PIXELS

    # If we've reached the end of the matrix, reset to the beginning
    if current_pos >= NUM_PIXELS * NUM_MATRICES:
        current_pos = 0

    # Show the updated LED matrix
    pixels.show()

    # Wait for 3 seconds before moving the pattern again
    time.sleep(MOVE_DELAY)
    
    
    ############Things to improve##########
    # Once the stripe goes to the end of the last matrix, just disappears, might need to play around with the code or could potentially connect the last matrix to the first one
    # --> This got fixed by editing the num of LED matrix to 6 so might need to connect the last matrix to the first one?
    # Need either a timer to go in one direction and then start moving in the other direction
    # Look up the angular velocity (speed) for the stripe movement

