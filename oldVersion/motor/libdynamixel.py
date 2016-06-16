import serial
import RPi.GPIO as GPIO
from time import sleep

DEBUG = 0
WRITE = 0x03
READ = 0x02
PING = 0x01
DELAY = 0.02

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.HIGH)

if DEBUG: print "Connecting to ttyAMA0..."
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)
port.open()
if DEBUG: print "\tttyAMA0 connected."

def uartTransmit():
	GPIO.output(4,GPIO.HIGH)
	print "Mode Transmit"

def uartReceive():
	GPIO.output(4,GPIO.LOW)
	print "Mode Receive"

def packet(ID,*parameter):
	parasum=0
	length= len(parameter[0])+1
	packet= "\xff\xff"+ chr(ID)+ chr(length)
	for i in range(len(parameter[0])):
		parasum = parameter[0][i]+parasum
		packet= packet+ chr(parameter[0][i])
	checksum= ID+ length+ parasum
	while checksum > 0xff:
		checksum = checksum-0x100
	checksum = ~checksum + 256
	packet = packet+ chr(checksum)
	return packet

def LedOn(*INP):
	if len(INP)!=1:
		print "Usage: LedOn( <ID> )"
		return(-1)
	[ID]=INP
	packetSend = packet( ID, [WRITE, 0x19, 0x01] )
	sleep(DELAY)
	port.write(packetSend)

def LedOff(*INP):
	if len(INP)!=1:
		print "Usage: LedOff( <ID> )"
		return(-1)
	[ID]=INP
	packetSend = packet( ID, [WRITE, 0x19, 0x00] )
	sleep(DELAY)
	port.write(packetSend)

def Load():
	uartReceive()
	sleep(0.008)
	packets=port.readline()
	print repr(packets)
	uartTransmit()

def Read(*INP):
	if len(INP)!=3:
		print "Usage: Read( <ID>, <START_ADDRESS>, <LENGTH_OF_DATA> )"
		return -1
	[ID, ADDRESS, LENGTH] = INP
	packetSend= packet(ID,[READ, ADDRESS, LENGTH])
	sleep(DELAY)
	port.write(packetSend)
	Load()
	
def MovingSpeed(*INP):
	if len(INP)!=2:
		print "Usage: MovingSpeed( <ID>, <speed (-100~100)> )"
		return -1
	[ID,Speed]=INP
	if Speed<-100 or Speed>100:
		print "Error, Speed out of range"
		print "Usage: MovingSpeed( <ID>, <speed (-100~100)> )"
		return -2
	if Speed>=0:
		Speed = Speed*10.23
		if DEBUG: print "Speed =" + repr(Speed)
		SpeedH = int( Speed/256 )
		if DEBUG: print "SpeedH =" + repr(SpeedH)
		SpeedL = int( Speed%256 )
		if DEBUG: print "SpeedL =" + repr(SpeedL)
		packetSend = packet(ID, [WRITE, 0x20, SpeedL, SpeedH])
		sleep(DELAY)
		port.write(packetSend)
	elif Speed<0:
		Speed = Speed * -1
		Speed = Speed*10.23
		if DEBUG: print "Speed =" + repr(Speed)
		SpeedH = int( Speed/256 )+4
		if DEBUG: print "SpeedH =" + repr(SpeedH)
		SpeedL = int( Speed%256 )
		if DEBUG: print "SpeedL =" + repr(SpeedL)
		packetSend = packet(ID, [WRITE, 0x20, SpeedL, SpeedH])
		sleep(DELAY)
		port.write(packetSend)
	else :
		print "Unknown Speed"
		return -3

def Ping(*INP):
	if len(INP)!=1:
		print "Usage: Ping( <ID> )"
		return -1
	[ID]=INP
	packetSend = packet(ID, [PING])
	sleep(DELAY)
	port.write(packetSend)
	Load()

