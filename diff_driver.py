from machine import Pin
from motor import Motor

class DiffDriver:
    def __init__(self, left_id=(9, 10, 11), right_id=(15, 13 ,14)):
        self.left_motor = Motor(left_id[0], left_id[1], left_id[2])
        self.right_motor = Motor(right_id[0], right_id[1], right_id[2])
        self.stby_pin = Pin(12, Pin.OUT)
        
    def enable(self):
        self.stby_pin.value(1)
        
    def disable(self):
        self.stby_pin.value(0)
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
    def forward(self, speed=0):  # 0 <= speed <= 1
        self.left_motor.forward(speed)
        self.right_motor.forward(speed)
    
    def backward(self, speed=0):  # 0 <= speed <= 1
        self.left_motor.backward(speed)
        self.right_motor.backward(speed)
        
    def spin_left(self, speed=0):  # in place
        self.left_motor.backward(speed)
        self.right_motor.forward(speed)
        
if __name__ == "__main__":
    # SETUP
    motor_driver = DiffDrivr()
    motor_driver.enable()
