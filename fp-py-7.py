"""
int ConquestCampaign(int N, int M, int L, int [] battalion) 
получает первыми двумя параметрами размер плацдарма "Квадраты" NxM, а battalion содержит массив из L*2 целых чисел (L >= 1) с индексацией с нуля, в котором каждый чётный (с чётным индексом) элемент содержит очередную координату области высадки по первому измерению N, а каждый нечётный (с нечётным индексом) элемент содержит очередную координату области высадки по второму измерению M.
Не исключено, что в связи с неразберихой в командовании координаты областей высадки могут дублироваться.
На примере с картинки параметры будут такими: N = 3, M = 4, L = 2, battalion = [2,2, 3,4]

Возвращает функция день, начиная с 1, когда все области будут взяты под контроль.
"""

from pymonad.tools import curry
from pymonad.state import State

n = 3
m = 4
l = 2
battalion = [2,2, 3,4]

points = set(zip((x - 1 for x in battalion[::2]), (y - 1 for y in battalion[1::2])))

user_init = {'day': 1, 'points':points, 'all_points': n * m}

print(points, user_init)

user_state = State.insert(user_init)


@curry(2)
def turn():
    def count_computation(accs):
        return user_items + 1, [accs[0] - money, accs[1] + money]
    return State(count_computation)

# finale = user_state.then(transfer(100)).then(transfer(200)).then(transfer(300))

# fin = finale.run(user_init['accounts'])

# print(fin) 