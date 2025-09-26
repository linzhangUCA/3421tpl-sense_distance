# Sense the Wall 
Use the ultrasonic distance sensor to sense the wall in front of your robot. 
Code motors' behaviors based on the distance sensor's data. 
There are taped markers on the ground to help you better observe your robot's movement. 

## Requirements:
> [!IMPORTANT]
> Redeem points by showcasing to Dr. Zhang in the classroom (LSCA105)

### 1. (25%) Physical Configuration
- (5%) Wire up a Common cathode RGB LED to Pico.
- (5%) Wire up motor driver board to Pico.
- (10%) Wire up HC-SR04 ultrasonic distance sensor to Pico. 
> [!NOTE]
> Please use a voltage divider circuit to down scale `Echo` pin's signal to around **3.3 V** before feed it into a GPIO pin on Pico.
- (5%) Wire up the power source.
    
### 2. (65%) Coding Exercise
Place your robot (distasnce sensor) 0.5 meters away from the wall. Start [wall_sensing.py](wall_sensing.py), and perform the following sequential movements.

1. (5%) Initialization (One-Time system check): blink all LEDs at the same time if the sensor found the wall (distance of `None` means no wall was found).
Blink LEDs with frequency of 5 Hz, lasting 2 seconds.
2. (10%) Drive **forward** with `GREEN` on.
3. (5%) **Stop 1 second** with `RED` on, when distance to the wall is 0.25 +/- 0.1 meters.
4. (10%) Drive **backward** with `BLUE` on.
5. (5%) **Stop 1 second** with `RED` on, when distance to the wall is 1 +/- 0.1 meters.
6. (10%) Drive **forward** with `GREEN` on.
7. (5%) **Stop 1 second** with `RED` on, when distance to the wall is 0.25 +/- 0.1 meters.
8. (10%) Drive **backward** with `BLUE` on.
9. (5%) **Stop** with `RED` on, when distance to the wall is 0.5 +/- 0.1 meters.

> [!NOTE]
> When one LED is on, other LEDs need to be turned off.

> [!TIP]
> - Pick a good speed for motors.
> - Polish your caster wheel or do some extra coding to make your robot move in straight lines.
> - Feel free to use the [motor control examples](https://github.com/linzhangUCA/3421example-motor_control) to drive your motors.
> - It is OK to use either [picozero](https://picozero.readthedocs.io/en/latest/) library or [distance sensing examples](https://github.com/linzhangUCA/3421example-ultrasonic_sensor) to get distance.

### 3. Voltage Divider Calculation


![wall_sense](/wall_sensing.png)

> Hints:
> 1. Find an appropriate speed for your robot.
> 2. You may need to use different duty cycles on the wheels so that your robot can drive straight.
> 3. [picozero](https://picozero.readthedocs.io/en/latest/) library is optional. You can reapeatedly trigger the HC-SR04 module using a PWM signal then read its feedback.


