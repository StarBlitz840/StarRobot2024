# importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.tools import wait

hub = PrimeHub()

# setup

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

# vars
colors = (
    Color.BLACK,
    Color.RED,
    Color.YELLOW,
    Color.GREEN,
    Color.BLUE,
    Color.WHITE,
    Color.NONE,
)
sensor_left.detectable_colors(colors)
sensor_right.detectable_colors(colors)


# functions
def rightround(thing):
    chassis.straight(thing)
    thing = thing * -1
    chassis.straight(thing / 2)


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


def s_icon():
    hub.display.icon(
        [
            [0, 100, 100, 100, 100],
            [100, 0, 0, 0, 0],
            [0, 100, 100, 100, 0],
            [0, 0, 0, 0, 100],
            [0, 100, 100, 100, 0],
        ]
    )


def t_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 100],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
        ]
    )


def a_icon():
    hub.display.icon(
        [
            [0, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
        ]
    )


def r_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
        ]
    )


def b_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 0],
        ]
    )


def l_icon():
    hub.display.icon(
        [
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 0, 0, 0, 0],
            [100, 100, 100, 100, 0],
        ]
    )


def i_icon():
    hub.display.icon(
        [
            [0, 100, 100, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 100, 100, 0],
        ]
    )


def z_icon():
    hub.display.icon(
        [
            [100, 100, 100, 100, 100],
            [0, 0, 0, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 0, 0, 0],
            [100, 100, 100, 100, 100],
        ]
    )


def follow_line(speed: int, seconds: float, sensor: ColorSensor, side="right", kp=1.5):
    error = sensor.reflection() - TARGET
    timer = StopWatch()
    timer.reset()
    direction = 1 if speed > 0 else -1
    if side == "right":
        direction = direction * -1
    while timer.time() < seconds * 1000:
        error = sensor.reflection() - TARGET
        change = int(error * kp * direction)
        wheel_right.dc(speed + change)
        wheel_left.dc(speed - change)


def follow_line_until_black(
    speed: int, sensor: ColorSensor, detection_sensor: ColorSensor, side="right", kp=1.5
):
    error = sensor.reflection() - TARGET
    direction = 1 if speed > 0 else -1
    if side == "right":
        direction = direction * -1
    while detection_sensor.reflection() > 9:
        error = sensor.reflection() - TARGET
        change = int(error * kp * direction)
        wheel_right.dc(speed + change)
        wheel_left.dc(speed - change)


# code
def run_1():
    # mixer
    chassis.settings(straight_speed=250)
    chassis.straight(-300, then=Stop.NONE)
    chassis.settings(straight_speed=80)
    chassis.straight(-150)
    chassis.straight(10)
    chassis.settings(turn_rate=30)
    chassis.turn(90)
    chassis.settings(turn_rate=100)
    chassis.settings(straight_speed=200)
    till_black(30, 0)
    chassis.turn(30)
    follow_line(30, 1.99, sensor_right, "right")
    follow_line_until_black(30, sensor_right, sensor_left)
    chassis.straight(40)
    chassis.turn(-70)
    chassis.settings(straight_speed=100)
    # team miion
    smash_right.run_time(1000, 500)
    chassis.straight(200, then=Stop.NONE)
    smash_right.run_time(-3000, 400)
    chassis.straight(-50)
    chassis.turn(120)
    follow_line(50, 2, sensor_right, "right")
    till_not_black(180, 0)
    chassis.straight(80)
    smash_left.run_time(-1000, 1000)
    smash_left.run_time(1000, 3000)
    chassis.settings(straight_speed=300)
    chassis.turn(10)
    chassis.straight(500, then=Stop.NONE)
    till_black(50, 0)
    follow_line(40, 5, sensor_right)
    chassis.straight(400)
    chassis.settings(straight_speed=250)


def run_5():
    chassis.straight(500)
    chassis.turn(70)


def haratza_tesha():
    wheel_right.dc(100)
    wheel_left.dc(100)
    while "1 + 1 == 3":
        pass


# run_1()
# run_1()


hub.display.icon(
    [
        [0, 100, 0, 100, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)
# chassis.turn(30)
# follow_line(30, 1.99, sensor_right, "right")
# rightround(-199)
run_1()
s_icon()
wait(400)
t_icon()
wait(400)
a_icon()
wait(400)
r_icon()
wait(400)
b_icon()
wait(400)
l_icon()
wait(400)
i_icon()
wait(400)
t_icon()
wait(400)
z_icon()
wait(400)
# haratza_tesha()
# smash_right.run_time(3000, 1999)
# chassis.settings(straight_speed=1000)
# chassis.straight(-200)
