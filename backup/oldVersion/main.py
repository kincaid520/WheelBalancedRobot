import sys
sys.path.append('motor')
sys.path.append('adxl345')

from libdynamixel import *
from adxl345 import *

DEBUG = True


MOTOR_ID = 1

sensor = ADXL345()

while True:
	axes = sensor.getAxes(True)
	x = axes['x']
	speedX = x*80

	if DEBUG:
		print x

	if speedX > 100:
		speedX = 100
	elif speedX < -100:
		speedX = -100

	if x < -0.3 or x > 0.3:
		MovingSpeed(MOTOR_ID, speedX)
	else:
		MovingSpeed(MOTOR_ID, 0)
	

	sleep(0.1)

