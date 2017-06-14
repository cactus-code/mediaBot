import serial
import time
ser = serial.Serial("/dev/cu.usbmodemFD121",9600)

def set_rgb_led(red_val,green_val,blue_val):
    ser.write(b'100')
