#! /usr/bin/env python3

import serial,time # yes, even though the library is "pyserial"
ser = serial.Serial('/dev/ttyACM0', baudrate = 9600) # open the connection
try:
  while 1:
    if(ser.in_waiting >0): # check for a line to be read
      line = ser.readline() # read the line from the serial connection
      line = line.decode('utf-8') # convert to UTF-8 encoding
      line = line.rstrip()
      timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      #print(line)
      print(f'"{timestamp}",{line}') #enclose timestamp (a string) in quotes
except:
  ser.close() # close the serial connection
  print("done.")

