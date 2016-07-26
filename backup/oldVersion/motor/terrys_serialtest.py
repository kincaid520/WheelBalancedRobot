import serial
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
DIRECTION = 7
GPIO.setup(DIRECTION,GPIO.OUT)
GPIO.output(DIRECTION,GPIO.HIGH)


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()


#LED: on
#checksum = int('0xff', 16) - (int('0x01', 16) + int('0x04', 16) + int('0x03', 16) + int('0x19', 16) + int('0x01', 16))
#ser.write("\xff\xff\x01\x04\x03\x19\x01"+chr(checksum))
#time.sleep(0.1)
#LED: off
#ser.write("\xff\xff\x01\x04\x03\x19\x00\xde")
#time.sleep(0.1)



#Read
ser.write("\xff\xff\x01\x04\x02\x24\x02\xd2")
time.sleep(0.008)

GPIO.output(DIRECTION,GPIO.LOW)
#time.sleep(0.006)
response = ser.readline()
print response.encode("hex")
print response[-3:-1].encode("hex")
ser.close()
