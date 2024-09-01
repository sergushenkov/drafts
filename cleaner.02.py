import math

code = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

STATES = {"brush", "water", "soap"}
position = (0, 0)
angle = 0
current_state = "brush"
clean_on = False


def command(s):
    if s[0] == "move":
        distance = int(s[1])
        move(distance)
    if s[0] == "turn" and s[1].lstrip("-").isdigit():
        delta_angle = int(s[1])
        turn(delta_angle)
    if len(s) == 2 and s[0] == "set" and s[1] in STATES:
        next_state = s[1]
        set(next_state)
    if len(s) == 1 and s[0] == "start":
        start()
    if len(s) == 1 and s[0] == "stop":
        stop()


def move(distance):
    global position, angle
    x, y = position
    angle_radians = math.radians(angle)
    x += int(distance * math.sin(angle_radians))
    y += int(distance * math.cos(angle_radians))
    position = (x, y)
    print(f"POS {x},{y}")


def turn(delta_angle):
    global angle
    angle = (angle + 360 + delta_angle) % 360
    print(f"ANGLE {angle}")


def set(next_state):
    global clean_on, current_state
    clean_on = False
    current_state = next_state
    print(f"STATE {current_state}")


def start():
    global clean_on
    clean_on = True
    print(f"START WITH {current_state}")


def stop():
    global clean_on
    clean_on = False
    print("STOP")


if __name__ == "__main__":
    for s in code:
        s = s.strip().split(' ')
        command(s)
