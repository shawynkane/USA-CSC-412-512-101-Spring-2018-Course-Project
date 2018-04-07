# Author: Shawyn Kane
# Date File Created: 4/3/2018
# Course: CSC 412/512-101
# Assignement: Course Project
# Group Members: Ryan Creel, Shawyn Kane, and Genesis Stroud
# 
# This source code is based off the source code from the following:
	# C/C++ code that the code in this file is based/model on, came from the following:
		# http://robotsquare.com/wp-content/uploads/2013/10/MantyBrickPi.zip
		# For Additional Information See the Following:
			# http://robotsquare.com/2013/10/23/manty-with-raspberry-pi-and-brickpi/
	# Python Code came from the following:
		# https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Motors.py
		# https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Touch_Sensor.py
		# https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/NXT-Color_Sensor_Color.py
		# https://www.dexterindustries.com/BrickPi/brickpi3-getting-started-step-4-program-brickpi-robot/brickpi3-getting-started-program-python/
		# For Additional Examples See the Following:
			# https://github.com/DexterInd/BrickPi3/tree/master/Software/Python/Examples
			# https://www.dexterindustries.com/BrickPi/brickpi3-getting-started-step-4-program-brickpi-robot/brickpi3-getting-started-program-python/
			# https://www.dexterindustries.com/BrickPi/brickpi-tutorials-documentation/program-it/python/brickpi-python-idle/
	
# the following 2 imports (time and brickpi3) and the associated comments are from https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Motors.py
import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers


result = -1
down = 0
up = 1

def msleep(msec):
	"This function is based on the msleep function from http://robotsquare.com/wp-content/uploads/2013/10/MantyBrickPi.zip"
	sleep(0.01*msec)
	return

def do_update():
	"This function is based on the do_update function from http://robotsquare.com/wp-content/uploads/2013/10/MantyBrickPi.zip"
	while True:
		result = BrickPiUpdateValues()
		msleep(10)
		if (result != 0):
			break
	return

def main():
	print("Hello, Brick Pi!")
	# Set up
		#
	
	# the following line of code is based on the code found at https://www.dexterindustries.com/BrickPi/brickpi-tutorials-documentation/program-it/python/brickpi-python-idle/
	result = BrickPiSetup()
	
	
	# the following 2 lines of code and the associated comments are from https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Motors.py
	BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
	BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH) # Configure for a touch sensor. If an EV3 touch sensor is connected, it will be configured for EV3 touch, otherwise it'll configured for NXT touch.
	
	# the following line of code and the associated comment is based on line 57 in https://github.com/DexterInd/BrickPi3/blob/master/Software/Python/Examples/LEGO-Motors.py
	BP.MotorEnable(PORT_A + PORT_B + PORT_C) # I do not know if this is correct syntax, but should replace the next three lines.
	
	# the following 5 lines of code is based on the code found at https://www.dexterindustries.com/BrickPi/brickpi-tutorials-documentation/program-it/python/brickpi-python-idle/
	BrickPi.MotorEnable[PORT_A] = 1 # enable right motor
	BrickPi.MotorEnable[PORT_B] = 1 # enable left motor
	BrickPi.MotorEnable[PORT_C] = 1 # enable head motor
	result = BrickPiSetupSensors()
	BrickPi.MotorSpeed[PORT_A] = 200
	result = BrickPiUpdateValues()