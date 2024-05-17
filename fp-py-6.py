"""
Перевод денег со счет на счет
"""

from pymonad.tools import curry
from pymonad.state import State

user_init = {'items': 0, 'accounts': [2000, 100]}

user_state = State.insert(user_init['items'])


@curry(2)
def transfer(money, user_items):
    def count_computation(accs):
        return user_items + 1, [accs[0] - money, accs[1] + money]
    return State(count_computation)

finale = user_state.then(transfer(100)).then(transfer(200)).then(transfer(300))

fin = finale.run(user_init['accounts'])

print(fin) 