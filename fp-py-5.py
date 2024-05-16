from pymonad.list import ListMonad

is_failed = lambda x: ListMonad((x[0], x[1])) if abs(x[0] - x[1]) <= 4 else ListMonad()


def next_event(x):
    event = input()
    if event == "b":
        return ListMonad()
    if event[0] == "l" and event[1:].isdigit():
        return ListMonad((x[0] + int(event[1:]), x[1])).bind(is_failed)
    if event[0] == "r" and event[1:].isdigit():
        return ListMonad((x[0], x[1] + int(event[1:]))).bind(is_failed)
    return ListMonad((x[0], x[1]))


print(
    ListMonad((0, 0)).bind(next_event).bind(next_event).bind(next_event) != ListMonad()
)
