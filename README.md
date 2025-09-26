# Sense the Wall 
Use the ultrasonic distance sensor to sense the wall in front of your robot. 
Code motors' behaviors based on the distance sensor's data. 
There are taped markers on the ground to help you better observe your robot's movement. 

## Requirements:

### 1. Physical Configuration
1.1. Wiring Pico and Motor Driver Board

    Control left motor using A channel of the motor driver board.
    Control right motor using B channel.
    (5%) Use GPIO7 for left motor's PWM input.
    (5%) Use GPIO9 for left motor's IN1 input.
    (5%) Use GPIO8 for left motor's IN2 input.
    (5%) Use GPIO15 for right motor's PWM input.
    (5%) Use GPIO13 for right motor's IN1 input.
    (5%) Use GPIO14 for right motor's IN2 input.
    (5%) Use GPIO12 for motor driver's STBY input.

1.2. Circuit Picture

Please take a picture of your circuit and display it below 👇

### 2. Coding Exercise
1. (80%) Complete `wall_sensing.py` perform the following sequential movements.
   ![wall_sense](/wall_sensing.png)

   Initially, place the robot (distasnce sensor) 0.5 meters away from the wall. By starting your program, the robot should be automatically perform the following sequence.
   1. (20%) Drive forward. Stop when distance to the wall is 0.25 +/- 0.1 meters.
   2. (20%) Drive backward. Stop when distance to the wall is 1 +/- 0.1 meters.
   3. (20%) Drive forward. Stop when distance to the wall is 0.25 +/- 0.1 meters.
   4. (20%) Drive backward. Stop when distance to the wall is 0.5 +/- 0.1 meters.
   
> Hints:
> 1. Find an appropriate speed for your robot.
> 2. You may need to use different duty cycles on the wheels so that your robot can drive straight.
> 3. [picozero](https://picozero.readthedocs.io/en/latest/) library is optional. You can reapeatedly trigger the HC-SR04 module using a PWM signal then read its feedback.

2. (20%) Upload a video which records the robot's back and forth movement. 

