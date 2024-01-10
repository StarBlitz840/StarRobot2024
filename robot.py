# importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Remote
from pybricks.parameters import Button
from pybricks.parameters import Port, Direction


hub = PrimeHub()

# setup

smash_right = Motor(Port.A)
smash_left = Motor(Port.D)
wheel_right = Motor(Port.B)
wheel_left = Motor(Port.F, Direction.COUNTERCLOCKWISE)
sensor_right = ColorSensor(Port.C)
sensor_left = ColorSensor(Port.E)
chassis = DriveBase(wheel_left, wheel_right, 62.4, 135)
chassis.use_gyro(True)
chassis.settings(straight_speed=250)


# defining functions
def go_till_touchin_black(speedy):
    while sensor_left.color() != Color.BLACK:
        chassis.straight()


# go_till_touchin_black(3)
# code
# wheel_left.run_time(3000, 1000)
# wheel_right.run_time(3000, 1000)
chassis.straight(660)
chassis.turn(-90)
# chassis.straight(38)
# smashsigmaskibidi_right.run_time(3000, 2200)
# chassis.straight(-20)
# chassis.turn(-90)
# chassis.straight(900)
