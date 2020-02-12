#!/usr/bin/python3
"""
        _                 _
       (_)               | |
 _ __   _  __  __   ___  | |
| '__| | | \ \/ /  / _ \ | |
| |    | |  >  <  |  __/ | |
|_|    |_| /_/\_\  \___| |_|


HC­SR04 Test
============

The goal of this script is to test GPIO and HC­SR04 Ultrasonic Sensor connection
from command line.

Copyright rixel 2020
Distributed under the Boost Software License, Version 1.0.
See accompanying file LICENSE or a copy at https://www.boost.org/LICENSE_1_0.txt
"""



# To use GPIO features with Python on your Raspberry Pi you have to install
# python3-rpi.gpio
import RPi.GPIO as GPIO
from signal import SIGINT, signal
from sys import stdout
import time import sleep, time



# Use these constants to change port according to your viring setup.
# Keep in mind, the numbering of the GPIO pins in this script follows the BOARD
# style. if you want to change the numbering style modify GPIO_STYLE.
GPIO_STYLE = GPIO.BOARD

ECHO = 18                   # Pin number where the script collects echo signal.
TRIG = 16                   # Pin number where the script sends trigger signal.

# Use these constants to find the limits of the sensor.
TRIGGER_CALM_DOWN = 2       # Time (in senconds) with released trigger signal.
TRIGGER_SIGNAL = 0.00001    # Time (in senconds) to send trigger signal.
SENSOR_SCALER = 17150       # Scaler multiplier to calibrate the sensor.



def ctrl_c_handle(*args):
    """
    Handles control-C event and stops the script.
    ---------------------------------------------
    @Params: aegs (anything)    [optional] The ability to capture arguments
                                serves to avoid errors only.
    """

    print('Calibration process stopped.')
    exit()



def main():
    """
    Handles the main loop
    ---------------------
    """

    global ECHO
    global GPIO_STYLE
    global TRIG

    print ('Initializing GPIO...')
    print('Press control-C to stop calibration.')
    GPIO.setmode(GPIO_STYLE)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    try:
        print ('\rCalibration starts.', end='')
        stdout.flush()
        while True:
            GPIO.output(TRIG, False)
            sleep(2)
            GPIO.output(TRIG, True)
            sleep(0.00001)
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO) == 0:
                pass
            pulse_start = time()
            while GPIO.input(ECHO) == 1:
                pass
            pulse_duration = time() - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            if distance > 2 and distance < 400:
                print ('\rDistance: {} cm(s)       '.format(distance), end='')
                stdout.flush()
            else:
                print ('\rDistance out of range!  ', end='')
                stdout.flush()
    except Exception:
        # This is just a test script and errors happen somtimes.
        print('\n[!] Error happen.')
        GPIO.output(TRIG, False)



if __name__ == '__main__':
    signal(SIGINT, ctrl_c_handle)
    main()
else:
    print('This is a script, not a module.')
