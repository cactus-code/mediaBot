import serial
import time
ser = serial.Serial("/dev/cu.usbmodemFD121",9600)

def notification_blink():
    ser.write(b'a')
