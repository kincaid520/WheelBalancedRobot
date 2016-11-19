import mpu9250
from time import sleep
from pylab import *
#Global Variables
g_scanningTimes=int(1000)

#Setting
sensor=mpu9250.MPU9250()

ASenPlotx=[]
ASenPloty=[]
ASenPlotz=[]
GSenPlotx=[]
GSenPloty=[]
GSenPlotz=[]
testPlotAX=[]
testPlotAZ=[]
testPlotGY=[]
totalAverageAZ=[]

averageAX=[0, 0, 0, 0]
averageAY=[0, 0, 0, 0]
averageAZ=[0, 0, 0, 0]
averageGX=[0, 0]
averageGY=[0, 0]
averageGZ=[0, 0]

#Scanning
print ("Start Scanning")
for i in range( g_scanningTimes ):

    #Getting Raw Data
    Asensor=sensor.get_accel() #tuple: [x, y, z]
    Gsensor=sensor.get_gyro() #tuple: [x, y, z]

    #Process the Data
    averageAX[ i%len(averageAX) ]=Asensor[0]
    averageAY[ i%len(averageAY) ]=Asensor[1]
    averageAZ[ i%len(averageAZ) ]=Asensor[2]
    averageGX[ i%len(averageGX) ]=Gsensor[0]
    averageGY[ i%len(averageGY) ]=Gsensor[1]
    averageGZ[ i%len(averageGZ) ]=Gsensor[2]
    CaliAX=sum(averageAX)/len(averageAX)
    CaliAY=sum(averageAY)/len(averageAY)
    CaliAZ=sum(averageAZ)/len(averageAZ)
    CaliGX=sum(averageGX)/len(averageGX)
    CaliGY=sum(averageGY)/len(averageGY)
    CaliGZ=sum(averageGZ)/len(averageGZ)

    #Save Data to Array
    if i>10:
        ASenPlotx.append( CaliAX )
        ASenPloty.append( CaliAY )
        ASenPlotz.append( CaliAZ )
        GSenPlotx.append( CaliGX )
        GSenPloty.append( CaliGY )
        GSenPlotz.append( CaliGZ )
        testPlotAX.append( Asensor[0] )
        testPlotAZ.append( Asensor[2] )
        testPlotGY.append( Gsensor[1] )
        totalAverageAZ.append(CaliAZ)
print ("Scanning Complete")
#Drawing Pictures
subplot( 3, 1, 1 )
plot( testPlotAX, label="raw", color="black" )
plot( ASenPlotx, label="Accel Sensor X", color="r" )
#plot( ASenPloty, label="Accel Sensor Y")
#plot( ASenPlotz, label="Accel Sensor Z", color="b")
#plot( GSenPlotx, label="Gyro Sensor X" )
#plot( GSenPloty, label="Gyro Sensor Y" )
#plot( GSenPlotz, label="gyro Sensor Z" )
legend()

subplot( 3, 1, 2 )
plot( testPlotAZ, label="raw", color="black" )
#plot( ASenPlotx, label="Accel Sensor X", color="r" )
#plot( ASenPloty, label="Accel Sensor Y")
plot( ASenPlotz, label="Accel Sensor Z", color="b")
#plot( GSenPlotx, label="Gyro Sensor X" )
#plot( GSenPloty, label="Gyro Sensor Y", color="g" )
#plot( GSenPlotz, label="gyro Sensor Z" )
legend()

subplot( 3, 1, 3 )
plot( testPlotGY, label="raw", color="black" )
#plot( ASenPlotx, label="Accel Sensor X", color="r" )
#plot( ASenPloty, label="Accel Sensor Y")
#plot( ASenPlotz, label="Accel Sensor Z", color="b")
#plot( GSenPlotx, label="Gyro Sensor X" )
plot( GSenPloty, label="Gyro Sensor Y", color="g" )
#plot( GSenPlotz, label="gyro Sensor Z" )
legend()

print "total AZ average is : %d"%(sum(totalAverageAZ)/len(totalAverageAZ))
show()
