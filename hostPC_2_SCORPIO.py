
#!/usr/bin/env python

import time
import json
import serial

class DeviceComm(serial.Serial):
    """
    Implements basic device communications
    """

    def __init__(self, port):
        port_param = {'port': port, 'baudrate': 9600, 'timeout': 0.2}
        super(DeviceComm, self).__init__(port=port, baudrate=9600, timeout=0.2)
        self.num_throw_away = 10
        self.throw_away_lines()

    def throw_away_lines(self):
        """ 
        Throw away first few lines. Deals with case where user has updated the
        firmware which writes a bunch text to the serial port. 
        """
        for i in range(self.num_throw_away):
            line = self.readline()

    def send_and_receive(self, msg_dict):
        """
        Send and receive message from the device.
        """
        msg_json = json.dumps(msg_dict) + '\n'
        print('Sent Message:', msg_json)
        self.write(msg_json.encode())
        rsp_json = self.readline()
        rsp_json = rsp_json.strip()
        print("Received response:", rsp_json)
        rsp_dict = {}
        try:
            rsp_dict = json.loads(rsp_json.decode('utf-8'))
            print("Decoded response:", rsp_dict)
        except ValueError as e:
            print ('Error decoding json message:', e)
            
        return rsp_dict

# --------------------------------------------------------------------------------------

if __name__ == '__main__':

    import time
    import random
    from datetime import datetime

    port = '/dev/ttyACM0'  # Set to match your device
    dev = DeviceComm(port)

    # Define the message to send
    message = {'command': 'optomotor'}

    # Send the message and receive the response
    response = dev.send_and_receive(message)

    # Print the response
    print ('Response:', response)

    count = 0
    stripes_running = False

    while True:
        count += 1
        value = random.random()
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        msg = {'command': 'optomotor'}
        if not stripes_running:
            response = dev.send_and_receive(msg)
            if response.get('message') == 'Stripes started':
                stripes_running = True
                print('Stripes started!')
            else:
                print('Failed to start stripes')

        rsp = dev.send_and_receive({'message': message, 'count': count, 'value': value, 'date': date})
        print ('msg:', msg)
        print ('rsp:', rsp)

    time.sleep(0.2)





