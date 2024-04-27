В рамках задания я должен был сделать три примера полноценного рефакторинга, с перекомбинацией логических частей проекта. К сожалению, нормальных больших проектов нет, буду использовать задачи с Advent of Code - 2022.

## День 2
### Было
```python
game = """A Y
B X
C Z"""

BALANCE = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, ('B', 'X'): 0,
           ('B', 'Y'): 3, ('B', 'Z'): 6, ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}
FIFURA = {'X': 1, 'Y': 2, 'Z': 3}

with open('input.txt', 'r') as f:
    game = f.read()
score = 0
for raund in game.split('\n'):
    if raund.strip() == '':
        break
    a, x = raund.strip().split(' ')
    score += FIFURA[x] + BALANCE[(a, x)]
print(score)
```
### Стало
```python
import os


def read_data(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(dir_name + "\\" + file_name, "r") as f:
        game = f.read()
        result = []
        for round in game.split("\n"):
            if round.strip() == "":
                break
            pair = round.strip().split(" ")
            result.append(pair)
        return result


def count_game(game):
    balance = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }
    figure = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for elf, player in game:
        score += figure[player] + balance[(elf, player)]
    return score


if __name__ == "__main__":
    file_name = "input.txt"
    game = read_data(file_name)
    result = count_game(game)
    print(result)
```
Исходный "монолит" где вперемешку ввод/вывод/тестовые данные разбит на функции, которые можно легко проверить по отдельности, на тех самых тестовых данных, плюс легко добавить свои тесты.

read_data() - читает данные из указанного файла, возвращает список строк, подготовленных к вычислениям

count_game() - вычисляет результат на основе входящих данных

## День 3
### Было
```python
bags = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

alfabet = 'abcdefghijklmnopqrstuvwxyz'
alfabet += alfabet.upper()
things = dict(zip(alfabet, range(1, 53)))

with open('input.txt', 'r') as fd:
    bags = fd.read()
result = 0
for bag in bags.split('\n'):
    part1 = set(i for i in bag[:len(bag)//2])
    part2 = set(i for i in bag[len(bag)//2:])
    common = part1 & part2
    if common:
        for i in common:
            result += things[i]
print(result)
```
### Стало
```python
import os


def read_data(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(dir_name + "\\" + file_name, "r") as f:
        raw_data = f.read()
        bags = [bag.strip() for bag in raw_data.split("\n")]
        return bags


def create_things():
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    alfabet += alfabet.upper()
    things = dict(zip(alfabet, range(1, 53)))
    return things


def find_common(bag):
    part1 = set(i for i in bag[: len(bag) // 2])
    part2 = set(i for i in bag[len(bag) // 2 :])
    common = part1 & part2
    return common


def count_score(bags):
    things = create_things()
    result = 0
    for bag in bags:
        common = find_common(bag)
        for thing in common:
            result += things[thing]
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    bags = read_data(file_name)
    result = count_score(bags)
    print(result)
```
Аналогично предыдущему случаю, но функций стало побольше. Все функции, кроме read_data(), "чистые" - т.е. подходят для программирования в функциональном стиле

read_data() - читает данные из указанного файла, возвращает список строк, подготовленных к вычислениям

create_things() - создает словарь, где ключ - буква, значение - ее вес

find_common() - находит общие элементы в двух частях мешка

count_score() - вычисляет результат на основе входящих данных

## День 4
### Было
```python
sections = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

with open('input.txt', 'r') as f:
    sections = f.read()

score = 0
for pair in sections.split('\n'):
    if pair.strip() == '':
        break
    (a, b), (c, d) = (x.split('-') for x in pair.split(','))
    first = {x for x in range(int(a), int(b) + 1)}
    second = {x for x in range(int(c), int(d) + 1)}
    if (first <= second) or (second <= first):
        score += 1
    # print(first, second, score)
print(score)
```
### Стало
```python
import os


def read_data(file_name):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    with open(dir_name + "\\" + file_name, "r") as f:
        raw_data = f.read()
        result = []
        for row in raw_data.split("\n"):
            if row.strip() == "":
                break
            (a, b), (c, d) = (x.split("-") for x in row.split(","))
            result.append(tuple(map(int, (a, b, c, d))))
        return result


def count_score(sections):
    score = 0
    for a, b, c, d in sections:
        is_first_bigger = a <= c and b >= d
        is_second_bigger = c <= a and d >= b
        if is_first_bigger or is_second_bigger:
            score += 1
    return score


if __name__ == "__main__":
    file_name = "input.txt"
    sections = read_data(file_name)
    score = count_score(sections)
    print(score)
```

Третий пример - аналогично первому

Примеры конечно примитивные, но это данность для DE. Если не относишься к Platform DE, которые собственно делают инструменты для остальных, то собственный код всегда на страницу кода, крайне редко когда больше