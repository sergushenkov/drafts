from pymonad.tools import curry
from pymonad.maybe import Just
from pymonad.list import ListMonad


@curry(2)
def add(x, y):
    return x + y


add10 = add(10)
assert add10(20) == 30
assert Just(20).then(add10) == Just(30)
assert ListMonad(1, 2, 3).then(add10) == ListMonad(11, 12, 13)
assert list(map(add10, [1, 2, 3])) == [11, 12, 13]
