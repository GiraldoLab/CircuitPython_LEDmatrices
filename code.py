import time
import board
import neopixel
from messaging import Messenger

# Configuration
# Define the number of pixels in each LED matrix
NUM_PIXELS = 256

# Define the number of LED matrices connected
NUM_MATRICES = 6
# Move over by 1 column of pixels(16 pixels)
SKIP_PIXELS = 16
PIXELS_TO_LIGHT = 48
MOVE_DELAY = 0.01  # seconds


# Initialize the LED matrix
pixels = neopixel.NeoPixel(board.NEOPIXEL0, NUM_PIXELS * NUM_MATRICES, brightness=1, auto_write=False)

# Define the current position of the pattern
current_pos = 0

# Define the color of the lit pixels
color = (0, 5, 0)

# Flag to track the direction of movement
move_forward = True

# Initialize the messenger
messenger = Messenger()

def turn_off_led_matrices():
    # Code to turn off LED matrices
    pixels.fill((0,0,0))
    pixels.show()


def alternating_stripes():
# Loop through the pixels in the pattern and light them up
    global current_pos, move_forward,  pixels

    for i in range(current_pos, NUM_PIXELS * NUM_MATRICES, PIXELS_TO_LIGHT * 2):

        if i + PIXELS_TO_LIGHT <= NUM_PIXELS * NUM_MATRICES:
            pixels[i:i+PIXELS_TO_LIGHT] = [color] * PIXELS_TO_LIGHT

    # Move the pattern to the right or left based on the direction
    if move_forward:
        current_pos += SKIP_PIXELS
    else:
        current_pos -= SKIP_PIXELS

    # Check if we've reached the end of the matrix
    if current_pos >= NUM_PIXELS * NUM_MATRICES or current_pos <= 0:
        # Toggle the direction
        move_forward = not move_forward

    # Turn off the last 16 pixels when moving forward
    if move_forward and current_pos >= NUM_PIXELS * NUM_MATRICES - SKIP_PIXELS:
        pixels[current_pos-NUM_PIXELS*NUM_MATRICES:current_pos] = [(0, 0, 0)] * SKIP_PIXELS


    # Show the updated LED matrix
    pixels.show()

'''
def alternating_stripes():
    global current_pos, move_forward, pixels

    for i in range(current_pos, NUM_PIXELS * NUM_MATRICES, PIXELS_TO_LIGHT * 2):

        if i + PIXELS_TO_LIGHT <= NUM_PIXELS * NUM_MATRICES:
            pixels[i:i+PIXELS_TO_LIGHT] = [color] * PIXELS_TO_LIGHT

def move_forward(direction=True):
    global current_pos, move_forward, pixels
    if direction == True:
        current_pos += SKIP_PIXELS
    else:
        current_pos -= SKIP_PIXELS
 ''' 

#Flag to track the state of the stripes 
stripes_running = False

while True:
    # Handle incoming messages
    msg = messenger.update()


    if msg:
        # We got a new message Print the received message
        print("Received message:", msg)

        if msg.get("command") == "optomotor" and not stripes_running:

            #Start moving the stripes
            #moving_stripes(move_forward) #Do I add move forward?
            alternating_stripes() #moving_Stripes

            #Update the stripes_running flag
            stripes_running = True
            
            #Send a response message
            response = {"message": "Stripes started"}
            messenger.send(response)

        elif msg.get("command") == "stop" and stripes_running:
            # Stop moving the stripes
            # Code to stop the movement of stripes

            # Turn off LED matrices
            turn_off_led_matrices()

            # Update the stripes_running flag
            stripes_running = False

            # Send a response message
            response = {"message": "Stripes stopped"}
            messenger.send(response)

        else:
            # Invalid command received
            response = {"error": "Invalid command"}
            messenger.send(response)
    # Wait for a short delay

    #Move the stripes
    # if stripes_running:
    #     alternating_stripes() 
    #     #Try 1

    #Wait for a short delay
    time.sleep(MOVE_DELAY)
    

'''
    # Send a response. It can by anything.
    rsp = {
            'time' : time.monotonic(),
            'message' : "It works!",     # 'message': msg,
            'message_count' : messenger.message_count,
            }
    messenger.send(rsp)

        elif messenger.error:
            # We have a message error - we couldn't parse the json.

            # Send error response. Again it can be anything you want
            rsp = {
                    'time' : time.monotonic(),
                    'error': messenger.error_message,
                    }
            messenger.send(rsp)

    # Wait for a short delay
    time.sleep(MOVE_DELAY)
'''