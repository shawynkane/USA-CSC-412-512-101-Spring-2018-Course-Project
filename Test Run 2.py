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

Left = brickpi3.BrickPi3.PORT_D # port for left motor
Right = brickpi3.BrickPi3.PORT_A # port for right motor
MotorTS = brickpi3.BrickPi3.PORT_1 # port for the touch sensor for the motors
US = brickpi3.BrickPi3.PORT_2 # port for the ultrasonic sensor
RBGColor = brickpi3.BrickPi3.PORT_3 # port for the red, blue, green color sensor

# 'BP' is the instance of the brick pi
# 'secs' is the number of seconds to run the motors
# 'power' is the percentage of power that the motor runs at. (-100 to 100)
# A negative power percent makes the motor run backwards. A positive power percent makes the motor run forward.
def moveSeconds(BP, secs, power):
    BP.set_motor_power(Left + Right, power)
    time.sleep(secs)
    BP.set_motor_power(Left + Right, 0)
    return

# 'BP' is the instance of the brick pi
# 'degrees' should be positive.
# 'power' is the percentage of power that the motor runs at. (-100 to 100)
# A negative power percent makes the motor run backwards. A positive power percent makes the motor run forward.
def moveDegrees(BP, degrees, power):
    if power == 0:
        BP.set_motor_power(Left + Right, 0)
        return
    rightInitialDegrees = BP.get_motor_encoder(Right)
    leftInitialDegrees = BP.get_motor_encoder(Left)
    rightStopped = False
    leftStopped = False
    if power > 0: # move forwards # when a motor rotates forward it adds degrees to the encoder
        rightDegreeToTurnTo = rightInitialDegrees + degrees
        leftDegreeToTurnTo = leftInitialDegrees + degrees
        BP.set_motor_power(Left + Right, power)
        while ((not rightStopped) and (not leftStopped)):
            if (BP.get_motor_encoder(Right) >= rightDegreeToTurnTo):
                BP.set_motor_power(Right, 0)
                rightStopped = True
            if (BP.get_motor_encoder(Left) >= leftDegreeToTurnTo):
                BP.set_motor_power(Left, 0)
                leftStopped = True
    else: # move backwards # when a motor rotates backwards it subtracts degrees from the encoder
        rightDegreeToTurnTo = rightInitialDegrees - degrees
        leftDegreeToTurnTo = leftInitialDegrees - degrees
        BP.set_motor_power(Left + Right, power)
        while ((not rightStopped) and (not leftStopped)):
            if (BP.get_motor_encoder(Right) <= rightDegreeToTurnTo):
                BP.set_motor_power(Right, 0)
                rightStopped = True
            if (BP.get_motor_encoder(Left) <= leftDegreeToTurnTo):
                BP.set_motor_power(Left, 0)
                leftStopped = True
    return

# 'BP' is the instance of the brick pi
# 'motorOn' is the motor that will move or run
# 'motorOff' is the motor that will not move or run
# 'degrees' should be positive.
# 'power' is the percentage of power that the motor runs at. (-100 to 100)
# A negative power percent makes the motor run backwards. A positive power percent makes the motor run forward.
def turnOneMotor(BP, motorOn, motorOff, degrees, power):
    if power == 0: # stop
        BP.set_motor_power(motorOff + motorOn, 0)
        return
    BP.set_motor_power(motorOff + motorOn, 0)
    initialDegrees = BP.get_motor_encoder(motorOn)

    if power > 0: # turn forward
        degreeToTurnTo = initialDegrees + degrees
        BP.set_motor_power(motorOn, power)
        while (BP.get_motor_encoder(motorOn) <= degreeToTurnTo):
            pass
        BP.set_motor_power(motorOn, 0)
    else: # turn backwards
        degreeToTurnTo = initialDegree - degrees
        BP.set_motor_power(motorOn, power)
        while (BP.get_motor_encoder(motorOn) >= degreeToTurnTo):
            pass
        BP.set_motor_power(motorOn, 0)
    return

# 'BP' is the instance of the brick pi
# 'turnLeft' is a boolean indicating true to turn left and false to turn right
# 'degrees' should be positive.
# To go backwards make 'power' a negative number.
# A negative power percent makes the motor run backwards. A positive power percent makes the motor run forward.
def turnBothMotors(BP, turnLeft, degrees, power): #### THE ROBOT IS HANGING UP SOMEWHERE IN THIS FUNCTION. #### THE ROBOT STOPS AND DOES NOTHING AND THE PROGRAM DOES NOT GO PAST THE FUNCTION CALL TO THIS FUNCTION.
    forward = Right
    reverse = Left
    if turnLeft:
        forward = Left
        reverse = Right
    if power == 0: # stop
        BP.set_motor_power(reverse + forward, 0)
        return
    BP.set_motor_power(reverse + forward, 0)
    forwardInitialDegrees = BP.get_motor_encoder(forward)
    reverseInitialDegrees = BP.get_motor_encoder(reverse)
    if power > 0: # turn forward
        forwardDegreeToTurnTo = forwardInitialDegrees + degrees
        reverseDegreeToTurnTo = reverseInitialDegrees - degrees
        forwardStopped = False
        reverseStopped = False
        BP.set_motor_power(forward, power)
        BP.set_motor_power(reverse, -power)
        while ((not forwardStopped) and (not reverseStopped)):
            if (BP.get_motor_encoder(forward) <= forwardDegreeToTurnTo):
                BP.set_motor_power(forward, 0)
                forwardStopped = True
            if (BP.get_motor_encoder(reverse) >= reverseDegreeToTurnTo):
                BP.set_motor_power(reverse, 0)
                reverseStopped = True
    else: # turn backwards
        forwardDegreeToTurnTo = forwardInitialDegree - degrees
        reverseDegreeTOTurnTo = reverseInitialDegree + degrees
        forwardStopped = False
        reverseStopped = False
        BP.set_motor_power(forward, power)
        BP.set_motor_power(reverse, -power)
        while ((not forwardStopped) and (not reverseStopped)):
            if (BP.get_motor_encoder(forward) >= forwardDegreeToTurnTo):
                BP.set_motor_power(forward, 0)
                forwardStopped = True
            if (BP.get_motor_encoder(reverse) <= reverseDegreeToTurnTo):
                BP.set_motor_power(reverse, 0)
                reverseStopped = True
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
    
    # Trun Left until Touch Sensor pressed
    BP.set_motor_power(Left, power)
    while BP.get_sensor(MotorTS) == 0:
        pass
    BP.set_motor_power(Left, 0)
	
    # Turn Left until Touch Sensor released
    BP.set_motor_power(Left, power)
    while BP.get_sensor(MotorTS) == 1:
        pass
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
    
    #BP.set_motor_power(Left + Right, -50)

    #time.sleep(5)
    #BP.set_motor_power(Left + Right, 0)
    
    #print(BP.get_motor_encoder(Left))
    #testSensors(BP)
    syncLegs(BP)
    power = 50
    degrees = 360*3
    
    #moveDegrees(BP, degrees, power)
    #turnOneMotor(BP, Left, Right, degrees, power)
    
    turnBothMotors(BP, True, degrees, power)#### THE ROBOT IS HANGING UP SOMEWHERE IN THIS FUNCTION. #### THE ROBOT STOPS AND DOES NOTHING AND THE PROGRAM DOES NOT GO PAST THE FUNCTION CALL TO THIS FUNCTION.
    
    print("Final Total Degrees Left Motor has Turned: " + str(BP.get_motor_encoder(Left)))
    print("Final Total Degrees Right Motor has Turned: " + str(BP.get_motor_encoder(Right)))
    #BP.set_motor_position(Right, 180)
    
    #BP.set_motor_power(Right + Left, 50)
    #time.sleep(6)
    
    #move(BP, 1.5, 20)
    BP.set_motor_power(Left + Right, 0)
    BP.reset_all()
    
main()
