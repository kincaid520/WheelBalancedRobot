from sys import argv
from time import sleep
from pylab import *
import mcp4725
import mpu9250

# Define settings
DEBUGON = True
THRESHOLD = 170
SCANNING_TIMES = 1000

g_testVoltage = 190
inputFile,inputVoltage=argv
if len(argv) == 2 and type(int(inputVoltage)) is int:
    g_testVoltage = int(inputVoltage)
    print "Input Voltage is %d"%(g_testVoltage)
    print "If it's not correct, ctrl-c in 5 seconds"
    sleep(5)

# Three ICs to use
sensor = mpu9250.MPU9250()
dacLeft = mcp4725.MCP4725(mcp4725.ADDRESS1)
dacRight = mcp4725.MCP4725(mcp4725.ADDRESS2)

# Default/Reset value
dacRight.set_voltage(0)
dacRight.set_clockwise()
dacLeft.set_voltage(0)
dacLeft.set_counterclockwise()

#Print the plot (debug)
if DEBUGON:
    ASenPlotx = []
    ASenPloty = []
    ASenPlotz = []
    GSenPlotx = []
    GSenPloty = []
    GSenPlotz = []

# Keep scanning (Debugging)
#MemAccel = []
print "Start Scanning..."
for i in range( SCANNING_TIMES ):
    Asensor = sensor.get_accel() # tuple:[x,y,z]
    Gsensor = sensor.get_gyro() # tuple:[x,y,z]
#	if Asensor-MemAccel > THRESHOLD:
#		MemAccel = Asensor
#		Asensor = sensor.getAccel()
#		if MemAccel-Asensor <= THRESHOLD:
#			ASenPlot.append(

    if DEBUGON:
		ASenPlotx.append(Asensor[0])
		ASenPloty.append(Asensor[1])
		ASenPlotz.append(Asensor[2])
		GSenPlotx.append(Gsensor[0])
		GSenPloty.append(Gsensor[1])
		GSenPlotz.append(Gsensor[2])
    #print "Accel: x: %5.f, y: %5.f, z: %5.f \t Gyro:  x: %5.f, y: %5.f, z: %5.f" %(Asensor[0], Asensor[1], Asensor[2], Gsensor[0], Gsensor[1], Gsensor[2])

#    if Gsensor[1] < 0:
#		dacLeft.set_voltage(int(Gsensor[1] * 4095 * (-1) / 32768))
#    else:
#		dacLeft.set_voltage(Gsensor[1] * 4095 / 32768 )
#	sleep(0.001)

# print the plot (debug)
    if i == 333:
        print "set voltage: %d"%(g_testVoltage)
        dacLeft.set_voltage(g_testVoltage)
        dacRight.set_voltage(g_testVoltage)
    if i == 666:
        print "set voltage: 0"
        dacLeft.set_voltage(0)
        dacRight.set_voltage(0)

print "Scanning Ended"



if DEBUGON:
	subplot(3,1,1)
	plot( ASenPlotx, label= "Accel Sensor X", color="r")
	#plot( ASenPloty, label= "Accel Sensor Y")
	plot( ASenPlotz, label= "Accel Sensor Z", color="b")
	#plot( GSenPlotx, label= "Gyro Sensor X")
	#plot( GSenPloty, label= "Gyro Sensor Y")
	#plot( GSenPlotz, label= "Gyro Sensor Z")
	legend()

	subplot(3,1,2)
	#plot( ASenPlotx, label= "Accel Sensor X")
	#plot( ASenPloty, label= "Accel Sensor Y")
	plot( ASenPlotz, label= "Accel Sensor Z", color="b")
	#plot( GSenPlotx, label= "Gyro Sensor X")
	plot( GSenPloty, label= "Gyro Sensor Y", color="g")
	#plot( GSenPlotz, label= "Gyro Sensor Z")
	legend()

	subplot(3,1,3)
	plot (ASenPlotx, label = "Accel Sensor X", color="r")
	#plot (ASenPloty, label = "Accel Sensor Y")
	#plot (ASenPlotz, label = "Accel Sensor Z")
	#plot (GSenPlotx, label = "Gyro Sensor X")
	plot (GSenPloty, label = "Gyro Sensor Y", color="g")
	#plot (GSenPlotz, label = "Gyro Sensor Z")
        legend()

	savefig("graph")
	show()
