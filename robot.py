# importing modules
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch
from pybricks.tools import wait
from pybricks.tools import hub_menu


# setup

BLACK = 5
WHITE = 42
TARGET = 23

hub = PrimeHub()
arm_right = Motor(Port.D)
arm_left = Motor(Port.E)
wheel_right = Motor(Port.B)
wheel_left = Motor(Port.F, Direction.COUNTERCLOCKWISE)
sensor_right = ColorSensor(Port.A)
sensor_left = ColorSensor(Port.C)
chassis = DriveBase(wheel_left, wheel_right, 62.4, 135)
chassis.use_gyro(True)
hub.imu.reset_heading(0)
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
# def to_angle(angle, speed):
#     start_angle = hub.imu.heading()
#     math = angle - start_angle
#     chassis.settings(turn_acceleration=speed)
#     if math < 180 and math > 0:
#         chassis.turn(start_angle + angle)``
#     if math > -180 and math < 0:
#         chassis.turn(start_angle - angle)
#     if math > 180 and math > 0:
#         chassis.turn(start_angle - angle)
#     if math < -180 and math < 0:
#         chassis.turn(start_angle + angle)


def turn_to(angle):
    print(hub.imu.heading())
    start_angle = (hub.imu.heading() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)

    if deg_to_turn >= 180:
        chassis.turn(deg_to_turn - 360)
    else:
        chassis.turn(deg_to_turn)


def turn_to_right(angle):
    start_angle = hub.imu.heading() % 360  # 208
    deg_to_turn = angle - start_angle % 360  # 242
    chassis.turn(deg_to_turn)


def rightround(thing):
    chassis.straight(thing)
    thing = thing * -1
    chassis.straight(thing / 2)


def duck():
    arm_left.run_time(1000, 500)


def till_black(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_left.reflection() > 9:
        print(sensor_left.color())
        pass

    chassis.stop()


def till_black_right(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_right.reflection() > 9:
        print(sensor_right.color())
        pass


def till_white(speed, turn_rate):
    chassis.drive(speed, turn_rate)

    while sensor_right.color() != Color.WHITE:
        print(sensor_right.color())
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


def clean_wheels():
    chassis.drive(720, 0)
    while "1 + 1 = 3":
        pass


# code
def run_1():
    # mixer
    chassis.settings(straight_speed=300)
    chassis.straight(-280, then=Stop.NONE)
    chassis.settings(straight_speed=80)
    chassis.straight(-150)
    chassis.straight(20)
    chassis.settings(turn_rate=40)
    chassis.turn(90)
    chassis.settings(turn_rate=100)
    chassis.settings(straight_speed=200)
    till_black(80, 0)
    chassis.turn(30)
    # to team mission
    follow_line(40, 1.5, sensor_right, "right")
    follow_line_until_black(30, sensor_right, sensor_left)
    arm_right.run_time(1000, 600, wait=False)
    chassis.straight(45)
    chassis.turn(-70)
    chassis.settings(straight_speed=100)
    # follow_line(30, 0.4, sensor_right)
    # team mission
    chassis.straight(50, then=Stop.NONE)
    arm_right.run_time(-3000, 475)
    chassis.straight(-50)
    # to purple man
    chassis.settings(turn_rate=100)
    chassis.turn(138)
    chassis.settings(straight_speed=700)
    chassis.settings(turn_rate=50)
    chassis.turn(50, wait=False)
    chassis.straight(438)
    chassis.settings(turn_rate=100)
    # till_white(180, 0)
    # purple man
    arm_left.run_time(-2000, 1000)
    arm_left.run_time(2000, 750)
    # TO HOME
    chassis.settings(straight_speed=700)
    chassis.straight(560, then=Stop.NONE)
    # chassis.settings(turn_rate=25)
    chassis.curve(450, 90, then=Stop.NONE)
    chassis.straight(500)
    # chassis.curve(75)
    # till_black(50, 0)
    #  follow_line(40, 5, sensor_left)
    # chassis.straight(400)
    # chassis.settings(straight_speed=250)


def run_2():
    arm_right.run_time(-250, 1000, wait=False)
    chassis.settings(straight_speed=700)
    chassis.straight(320)
    arm_right.run_time(250, 600, wait=False)
    wait(100)
    chassis.settings(straight_speed=700)
    chassis.straight(300)
    chassis.settings(straight_speed=250)
    wheel_right.run_time(700, 1500, wait=False)
    wheel_right.run_time(200, 1500, wait=False)
    arm_left.run_time(-3000, 2000)
    chassis.settings(straight_speed=700)
    chassis.straight(-1000)


def run_4():
    chassis.settings(straight_speed=800)
    chassis.straight(700)
    chassis.settings(straight_speed=190 + 60)
    till_black_right(199, 0)
    chassis.straight(30)
    arm_left.run_angle(700, 90)
    arm_left.run_angle(700, 180)
    wheel_left.run_time(300, 1500)
    chassis.straight(300)
    chassis.settings(straight_speed=60)
    chassis.straight(500, wait=False)
    arm_right.run_angle(-4000, 1700)
    chassis.settings(straight_speed=800)
    chassis.straight(-100)
    chassis.turn(80)
    chassis.straight(-3000)
    chassis.settings(straight_speed=190 + 60)
    # wheel_left.run_time(-1000, 900)
    # chassis.settings(straight_speed=400)
    # chassis.straight(-2000)


def run_5():
    chassis.settings(straight_speed=300)
    chassis.straight(-300)
    chassis.straight(20)
    chassis.settings(turn_rate=900)
    chassis.turn(70, wait=False)
    wait(400)
    chassis.curve(800, 90)
    chassis.straight(1)
    wait(5000)


def run_3():
    chassis.settings(straight_speed=800)
    chassis.straight(250, then=Stop.NONE)
    till_black(200, -30)
    chassis.straight(50)
    turn_to(45)
    chassis.settings(straight_speed=190 + 60)
    chassis.straight(300, wait=False)
    wait(300)
    arm_left.run_angle(180, -180)
    arm_left.run_angle(180, 180, wait=False)
    chassis.settings(straight_speed=800)
    chassis.straight(-200)
    chassis.curve(100, 120, then=Stop.NONE)
    chassis.straight(5000)


# run_1()
# run_1()


def run_6():
    chassis.settings(straight_speed=400)
    chassis.curve(-3000, -10)
    chassis.curve(-250, -80, then=Stop.NONE)
    chassis.straight(-150, wait=False)
    wait(500)
    arm_right.run_time(300, 700)
    chassis.straight(-200)
    chassis.curve(-100, 90)
    chassis.straight(100)
    chassis.curve(50, 50)
    chassis.settings(straight_speed=100)
    chassis.straight(-300)
    chassis.straight(50)
    chassis.turn(30)
    chassis.curve(-300, 30)


def run_7():
    chassis.straight(300)
    arm_right.run_time(-400, 2000)
    chassis.straight(-100)


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
# chassis.straight(500)
# smash_left.run_time(-2000, 2000)
# run_1()
def stats():
    precent = hub.battery.current() / 2100 * 100
    print("battery: ", hub.battery.current(), "mAh")
    print("battery: ", precent, "%")
    # wheel_left.run_time(300, 1500)


selected = hub_menu("1", "2", "3", "4", "5", "6", "7", 99, "9")


if selected == "1":
    run_1()
elif selected == "2":
    run_2()
elif selected == "3":
    run_3()
elif selected == "4":
    run_4()
elif selected == "5":
    run_5()
elif selected == "6":
    run_6()
elif selected == "7":
    run_7()
elif selected == 99:
    stats()
elif selected == "9":
    clean_wheels()

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
# clean_wheels()
# smash_right.run_time(3000, 1999)
# chassis.settings(straight_speed=1000)
# chassis.straight(-200)#

# chassis.drive(180)
