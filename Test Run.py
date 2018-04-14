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
down = 0
up = 1

speed = 25

def move(BP, secs, power):
    BP.set_motor_power(Left + Right, power)
    time.sleep(secs)
    BP.set_motor_power(Left + Right, 0)
    return

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
    power = 40
    # while touch sensor is pressed move both legs off touch sensor
    print(str(BP.get_sensor(MotorTS)))
    while BP.get_sensor(MotorTS) == 1:
        BP.set_motor_power(Left + Right, power)
        print("while loop 1")
    BP.set_motor_power(Left + Right, 0)
    time.sleep(5)
        
    while BP.get_sensor(MotorTS) == 1:
        while BP.get_sensor(MotorTS) == 1:
            BP.set_motor_power(Left + Right, power)
            BP.set_motor_power(Left + Right, 0)
        time.sleep(5)
        print("while loop")

    # Trun Right until Touch Sensor pressed
    while BP.get_sensor(MotorTS) == 0:
        print(str(BP.get_sensor(MotorTS)))
        BP.set_motor_power(Right, power)
    BP.set_motor_power(Right, 0)
            
def main():
    print("Hello, Brick Pi!")
    
    BP = brickpi3.BrickPi3()
    BP.reset_all()
    BP.set_sensor_type(MotorTS, brickpi3.BrickPi3.SENSOR_TYPE.TOUCH)
    BP.set_sensor_type(RBGColor, brickpi3.BrickPi3.SENSOR_TYPE.NXT_COLOR_FULL)
    BP.set_sensor_type(US, brickpi3.BrickPi3.SENSOR_TYPE.NXT_ULTRASONIC)
    time.sleep(0.05)
    #testSensors(BP)
    #syncLegs(BP)
    BP.set_motor_position(Right, 180)
    BP.set_motor_power(Right, 20)
    
    #move(BP, 3, 100)
    #BP.set_motor_power(Left + Right, 0)
    BP.reset_all()
    
main()
