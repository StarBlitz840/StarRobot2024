#importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#setup

BLACK = 5
WHITE = 42
TARGET = 23

smash_right = Motor(Port.D)
smash_left = Motor(Port.E)
wheel_right = Motor(Port.B)
wheel_left = Motor(Port.F, Direction.COUNTERCLOCKWISE)
sensor_right = ColorSensor(Port.A)
sensor_left = ColorSensor(Port.C)
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
def forword_and_backwords(thing):
    chassis.straight(thing)
    thing = thing * -1
    chassis.straight(thing)

def duck():
    smash_left.run_time(1000, 500)

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


def follow_line(speed: int, seconds: int, sensor: ColorSensor, side = "right", kp = 3):
    error = sensor.reflection() - TARGET
    timer = StopWatch()
    timer.reset()
    direction = 1 if speed > 0 else -1
    if side == 'right':
        direction = direction * -1
    while timer.time() < seconds * 1000:
        error = sensor.reflection() - TARGET
        change = int(error * kp * direction)
        wheel_right.dc(speed + change)
        wheel_left.dc(speed - change)

#code
def run_1():
    chassis.settings(straight_speed=250)
    chassis.straight(-300, then=Stop.NONE)
    chassis.settings(straight_speed=40)
    chassis.straight(-120)
    chassis.settings(turn_rate=45)
    chassis.turn(90)
    chassis.settings(turn_rate=100)
    till_black(30, 0)
    chassis.straight(10)
    chassis.turn(30)
    follow_line(40, 3, sensor_right, "right", 1.5)


    chassis.settings(straight_speed=250)



run_1()
chassis.straight(1000)