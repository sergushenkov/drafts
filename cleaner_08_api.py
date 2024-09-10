import pure_robot


robots = {
    'pure_robot': {
        'init': pure_robot.RobotState,
        'move': pure_robot.move,
        'turn': pure_robot.turn,
        'set': pure_robot.set_state,
        'start': pure_robot.start,
        'stop': pure_robot.stop,
    },
}
# конструктор
def init():
    return robots['pure_robot']['init'](0.0, 0.0, 0, pure_robot.WATER)


# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print(message)


def get_x(cleaner_state):
    return cleaner_state.x


def get_y(cleaner_state):
    return cleaner_state.y


def get_angle(cleaner_state):
    return cleaner_state.angle


def get_state(cleaner_state):
    return cleaner_state.state


def action(robot, command, cleaner_state):
    cmd = command.split(" ")
    transfer = transfer_to_cleaner
    if cmd[0] == "move":
        return robots[robot]['move'](transfer, int(cmd[1]), cleaner_state)
    if cmd[0] == "turn":
        return robots[robot]['turn'](transfer, int(cmd[1]), cleaner_state)
    if cmd[0] == "set":
        return robots[robot]['set'](transfer, cmd[1], cleaner_state)
    if cmd[0] == "start":
        return robots[robot]['start'](transfer, cleaner_state)
    if cmd[0] == "stop":
        return robots[robot]['stop'](transfer, cleaner_state)
