from adxl345 import ADXL345
from time import sleep

adxl345 = ADXL345()

while 1:
	axes = adxl345.getAxes(True)
	print "x= %.3fG\ty=%.3fG\tz=%.3fG" %(axes['x'], axes['y'], axes['z'])
	sleep(1)
