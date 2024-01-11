#importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Remote
from pybricks.parameters import Button
from pybricks.parameters import Port, Direction


hub = PrimeHub()

#setup

smash_right = Motor(Port.A)
smash_left = Motor(Port.D)
wheel_right = Motor(Port.B)
wheel_left = Motor(Port.F, Direction.COUNTERCLOCKWISE)
sensor_right = ColorSensor(Port.C)
sensor_left = ColorSensor(Port.E)
chassis = DriveBase(wheel_left, wheel_right, 62.4, 135)
chassis.use_gyro(True)
chassis.settings(straight_speed=250)
chassis.settings(turn_rate=100)


#vars
colors = (Color.BLACK,
          Color.RED,
          Color.YELLOW,
          Color.GREEN,
          Color.BLUE,
          Color.WHITE,
          Color.NONE)
sensor_left.detectable_colors(colors)
sensor_right.detectable_colors(colors)

#functions
def till_black(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_left.color() != Color.BLACK:
        print(sensor_left.color())
        pass

    chassis.stop()

def till_not_black(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_right.color() == Color.BLACK:
        pass

    chassis.stop()

#code
# chassis.straight(700, then=Stop.NONE)
# till_black(150, 0)
# wait(1000)
# chassis.turn(-90)
# till_not_black(150, 0)
# smash_right.run_time(3000, 2200)
# chassis.straight(-80)
# chassis.turn(-90)
# chassis.settings(straight_speed=750)
# chassis.straight(900)
# chassis.settings(straight_speed=250)
# smash_right.run_time(-1000, 500)

chassis.straight(800)
chassis.settings(turn_rate=45)
chassis.turn(90)
chassis.settings(turn_rate=100)
