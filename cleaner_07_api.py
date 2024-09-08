import pure_robot_07 as pure_robot


# конструктор
def init(x=0.0, y=0.0, angle=0, state='WATER'):
    return pure_robot.RobotState(x, y, angle, pure_robot.states[state])


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


def action(command, cleaner_state):
    cmd = command.split(" ")
    transfer = transfer_to_cleaner
    if cmd[0] == "move":
        return pure_robot.move(transfer, int(cmd[1]), cleaner_state)
    if cmd[0] == "turn":
        return pure_robot.turn(transfer, int(cmd[1]), cleaner_state)
    if cmd[0] == "set":
        return pure_robot.set_state(transfer, cmd[1], cleaner_state)
    if cmd[0] == "start":
        return pure_robot.start(transfer, cleaner_state)
    if cmd[0] == "stop":
        return pure_robot.stop(transfer, cleaner_state)
