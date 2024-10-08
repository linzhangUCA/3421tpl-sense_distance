# Wall Sensing 
Use the ultrasonic distance sensor to sense the wall in front of your robot. Code your robot's behaviors according to the distance to the wall. There are taped markers on the ground to help you better observe your robot's movement. 

## Requirements:
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

2. (20%) Upload a video which records the robot's back and forth movement. 

