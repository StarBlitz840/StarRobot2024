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

smash_right = Motor(Port.A)
smash_left = Motor(Port.D)
wheel_right = Motor(Port.E)
wheel_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
sensor_right = ColorSensor(Port.F)
sensor_left = ColorSensor(Port.B)
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


def run_1():
    chassis.settings(straight_speed=250)
    chassis.straight(-600)
    chassis.settings(turn_rate=45)
    chassis.turn(90)
    chassis.settings(turn_rate=100)
    till_black(30, 0)
    chassis.straight(10)
    chassis.turn(30)
    follow_line(40, 3, sensor_right, "right", 1.5)


    chassis.settings(straight_speed=250)

# run_1()
# smash_left.run_time(2000, 3000)
def forword_and_backwords(thing):
    chassis.straight(thing)
    thing = thing * -1
    chassis.straight(thing)

def duck():
    smash_left.run_time(1000, 500)

                                # while "false":
                                #     print (sensor_right.reflection())
run_1()
# forword_and_backwords(-150)
# forword_and_backwords(-150)
# follow_line(40, 5, sensor_left, "right", 1.5)
