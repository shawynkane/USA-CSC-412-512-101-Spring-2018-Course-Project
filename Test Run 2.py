# Author: Ryan Creel, Shawyn Kane, and Genesis Stroud
# Date File Created: 4/13/2018
# Course: CSC 412/512-101
# Assignement: Course Project
# Group Members: Ryan Creel, Shawyn Kane, and Genesis Stroud
# 
# This source code is based off the source code from the following:
	# C/C++ code that the code in this file is based/model on, came from the following:
		# http://robotsquare.com/wp-content/uploads/2013/10/MantyBrickPi.zip
		# For Additional Information See the Following:
			# http://robotsquare.com/2013/10/23/manty-with-raspberry-pi-and-brickpi/
	# References for Python Code:
		# https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Motors.py
		# https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Touch_Sensor.py
		# https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/NXT-Color_Sensor_Color.py
		# https://www.dexterindustries.com/BrickPi/brickpi3-getting-started-step-4-program-brickpi-robot/brickpi3-getting-started-program-python/
		# For Additional Examples See the Following:
			# https://github.com/DexterInd/BrickPi3/tree/master/Software/Python/Examples
			# https://www.dexterindustries.com/BrickPi/brickpi3-getting-started-step-4-program-brickpi-robot/brickpi3-getting-started-program-python/
			# https://www.dexterindustries.com/BrickPi/brickpi-tutorials-documentation/program-it/python/brickpi-python-idle/
			# Type "import brickpi3" and then "help(brickpi3)" in the python interpreter on the brickpi3/raspberrypi for more information/documentation on the python brickpi3 module.
import time
import brickpi3

Left = brickpi3.BrickPi3.PORT_D
Right = brickpi3.BrickPi3.PORT_A
MotorTS = brickpi3.BrickPi3.PORT_1
US = brickpi3.BrickPi3.PORT_2
RBGColor = brickpi3.BrickPi3.PORT_3

def moveSeconds(BP, secs, power): # power is the percentage of power that the motor runs at
    BP.set_motor_power(Left + Right, power)
    time.sleep(secs)
    BP.set_motor_power(Left + Right, 0)
    return

def moveDegrees(BP, degrees, power):
    if power == 0:
        BP.set_motor_power(Left + Right, 0)
    rightInitialDegrees = BP.get_motor_encoder(Right)
    leftInitialDegrees = BP.get_motor_encoder(Left)
    rightStopped = False
    leftStopped = False
    if power > 0: # when a motor rotates forward it adds degrees to the encoder
        BP.set_motor_power(Left + Right, power)
        while ((not rightStopped) and (not leftStopped)):
            if (abs(BP.get_motor_encoder(Right)-rightInitialDegrees) >= degrees):
                BP.set_motor_power(Right, 0)
                rightStopped = True
            if (abs(BP.get_motor_encoder(Left)-leftInitialDegrees) >= degrees):
                BP.set_motor_power(Left, 0)
                leftStopped = True
    else: # when a motor rotates backwards it subtracts degrees from the encoder
        BP.set_motor_power(Left + Right, power)
        while ((not rightStopped) and (not leftStopped)):
            if (abs(rightInitialDegrees-BP.get_motor_encoder(Right)) >= degrees):
                BP.set_motor_power(Right, 0)
                rightStopped = True
            if (abs(leftInitialDegrees-BP.get_motor_encoder(Left)) >= degrees):
                BP.set_motor_power(Left, 0)
                leftStopped = True

def turn(BP, left):
    return

def testSensors(BP):
    for i in range(5):
        time.sleep(5)
        try:
            value = BP.get_sensor(RBGColor)
            print("RBGColor Sensor = " + str(value))
        except brickpi3.SensorError as e:
            print(e)
            
        try:
            value = BP.get_sensor(US)
            print("Ultrasonic Sensor = " + str(value))
        except brickpi3.SensorError as e:
            print(e)
            
        try:
            value = BP.get_sensor(MotorTS)
            print("Touch Sensor = " + str(value))
        except brickpi3.SensorError as e:
            print(e)
            
def syncLegs(BP):
    power = 20
    # while touch sensor is pressed move both legs off touch sensor
    BP.set_motor_power(Left + Right, power)
    while BP.get_sensor(MotorTS) == 1:
        pass
    BP.set_motor_power(Left + Right, 0)
    time.sleep(5)
        
    while BP.get_sensor(MotorTS) == 1:
        BP.set_motor_power(Left + Right, power)
        while BP.get_sensor(MotorTS) == 1:
            pass
        BP.set_motor_power(Left + Right, 0)
        time.sleep(5)

    # Trun Right until Touch Sensor pressed
    BP.set_motor_power(Right, power)
    while BP.get_sensor(MotorTS) == 0:
        pass
    BP.set_motor_power(Right, 0)
	
    # Turn Right until Touch Sensor released
    BP.set_motor_power(Right, power)
    while BP.get_sensor(MotorTS) == 1:
        pass        
    BP.set_motor_power(Right, 0)

    # Turn the Right Motor 180 degrees
    BP.set_motor_power(Right, 20)
    rightInitialDegrees = BP.get_motor_encoder(Right)
    while ((BP.get_motor_encoder(Right)-rightInitialDegrees)<180):
        pass
    BP.set_motor_power(Right, 0)
    print("Degrees Turned: " + str(BP.get_motor_encoder(Right)-rightInitialDegrees))

    # This function is hanging up after this point, may be due to low batteries.
    
    # Trun Left until Touch Sensor pressed
    BP.set_motor_power(Left, power)
    while BP.get_sensor(MotorTS) == 0:
        print("left 1") 
    BP.set_motor_power(Left, 0)
	
    # Turn Left until Touch Sensor released
    BP.set_motor_power(Left, power)
    while BP.get_sensor(MotorTS) == 1:
        print("left 2")
    BP.set_motor_power(Left, 0)    
    
def main():
    print("Hello, Brick Pi!")
    
    BP = brickpi3.BrickPi3()
    BP.reset_all()
    BP.set_sensor_type(MotorTS, brickpi3.BrickPi3.SENSOR_TYPE.TOUCH)
    BP.set_sensor_type(RBGColor, brickpi3.BrickPi3.SENSOR_TYPE.NXT_COLOR_FULL)
    BP.set_sensor_type(US, brickpi3.BrickPi3.SENSOR_TYPE.NXT_ULTRASONIC)
    time.sleep(0.05)
    print("Initial Total Degrees Left Motor has Turned: " + str(BP.get_motor_encoder(Left)))
    print("Initial Total Degrees Right Motor has Turned: " + str(BP.get_motor_encoder(Right)))
    #BP.offset_motor_encoder(Left, BP.get_motor_encoder(Left))
    #BP.offset_motor_encoder(Right, BP.get_motor_encoder(Right))
    #print(BP.get_motor_encoder(Left))
    #print(BP.get_motor_encoder(Right))
    print()
    
    BP.set_motor_power(Left + Right, -50)
    time.sleep(5)
    BP.set_motor_power(Left + Right, 0)
    
    #print(BP.get_motor_encoder(Left))
    #testSensors(BP)
    #syncLegs(BP)
    print("Final Total Degrees Left Motor has Turned: " + str(BP.get_motor_encoder(Left)))
    print("Final Total Degrees Right Motor has Turned: " + str(BP.get_motor_encoder(Right)))
    #BP.set_motor_position(Right, 180)
    
    #BP.set_motor_power(Right + Left, 50)
    #time.sleep(6)
    
    #move(BP, 1.5, 20)
    BP.set_motor_power(Left + Right, 0)
    BP.reset_all()
    
main()
