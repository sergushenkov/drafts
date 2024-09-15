import pure_robot as r
from pymonad.tools import curry
from pymonad.state import State

robot_init = r.RobotState(0.0, 0.0, 0, r.WATER)
transfer = r.transfer_to_cleaner

robot_state = State.insert(robot_init)


@curry(2)
def move(dist, state):
    def count_computation():
        return r.move(transfer, dist, state)

    return State(count_computation)


@curry(2)
def turn(turn_angle, state):
    def count_computation():
        return r.turn(transfer, turn_angle, state)

    return State(count_computation)


@curry(2)
def set(new_internal_state, state):
    def count_computation():
        return r.set_state(transfer, new_internal_state, state)

    return State(count_computation)


@curry(1)
def start(state):
    def count_computation():
        return r.start(transfer, state)

    return State(count_computation)


@curry(1)
def stop(state):
    def count_computation():
        return r.stop(transfer, state)

    return State(count_computation)


finale = (
    robot_state.then(move(100))
    .then(turn(-90))
    .then(set("soap"))
    .then(start())
    .then(move(50))
    .then(stop())
)

finale.run()
