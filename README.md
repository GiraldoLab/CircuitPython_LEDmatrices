# CircuitPython_LEDmatrices
Code for controlling LED matrices through the SCORPIO microcontroller, receives and sends messages to the host PC (code.py)


Recieving messages:
- "optomotor": Moving alternating stripes to induce a optomotor response. Can adjust angular velocity, direction of movement, etc
- "stripe": Provides a stripe at a random position to observe stripe fixation behavior
- "sun": One LED will simulate a sun stimulus. Can set sun position at random.

Output messages:
- "optomotor": Sends direction of movement.
- "stripe": Sends stripe position
- "sun": Sends sun position
