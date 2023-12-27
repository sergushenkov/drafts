## Пример 1

```py
import os


def create_maps(almanac):
    almanac_parts = almanac.split("\n\n")

    seeds_v = list(map(int, almanac_parts[0][7:].split(" ")))
    seeds = []
    for i in range(len(seeds_v) // 2):
        seeds.append((0, seeds_v[2 * i], seeds_v[2 * i + 1]))

    seed2soil = []
    soil2fertilizer = []
    fertilizer2water = []
    water2light = []
    light2temperature = []
    temperature2humidity = []
    humidity2location = []
    maps = [
        seed2soil,
        soil2fertilizer,
        fertilizer2water,
        water2light,
        light2temperature,
        temperature2humidity,
        humidity2location,
    ]

    src = seeds
    for i, almanac_part in enumerate(almanac_parts[1:]):
        current_map = []
        for record in almanac_part.splitlines()[1:]:
            dst_start, src_start, range_length = map(int, record.split(" "))
            current_map.append([src_start, range_length, dst_start])
        while src:
            (_, src_start, src_range_length) = src.pop()
            is_not_in_map = True
            for map_start, map_range_length, dst_start in current_map:
                if (
                    src_start >= (map_start + map_range_length)
                    or (src_start + src_range_length - 1) < map_start
                ):
                    continue
                if map_start <= src_start < (
                    map_start + map_range_length
                ) and map_start <= (src_start + src_range_length) <= (
                    map_start + map_range_length
                ):
                    maps[i].append(
                        (
                            src_start,
                            dst_start + (src_start - map_start),
                            src_range_length,
                        )
                    )
                    is_not_in_map = False
                    break
                if map_start > src_start and map_start <= (
                    src_start + src_range_length
                ) <= (map_start + map_range_length):
                    maps[i].append(
                        (map_start, dst_start, src_start + src_range_length - map_start)
                    )
                    src.append((0, src_start, map_start - src_start))
                    is_not_in_map = False
                    break
                if map_start <= src_start < (map_start + map_range_length) and (
                    src_start + src_range_length
                ) > (map_start + map_range_length):
                    maps[i].append(
                        (
                            src_start,
                            dst_start + (src_start - map_start),
                            (map_start + map_range_length - src_start),
                        )
                    )
                    src.append(
                        (
                            0,
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break
                if map_start > src_start and (src_start + src_range_length) > (
                    map_start + map_range_length
                ):
                    maps[i].append((map_start, dst_start, map_range_length))
                    src.append((0, src_start, map_start - src_start))
                    src.append(
                        (
                            0,
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break
            if is_not_in_map:
                maps[i].append((src_start, src_start, src_range_length))
        src = maps[i].copy()
    return maps


test_almanac = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
maps = create_maps(test_almanac)
humidity_to_location = maps[6]
humidity_to_location.sort(key=lambda x: x[1])
assert humidity_to_location[0][1] == 46

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    maps = create_maps(fd.read())
    humidity_to_location = maps[6]
    humidity_to_location.sort(key=lambda x: x[1])
    print(humidity_to_location[0][1])
```

Задача взята из https://adventofcode.com/2023/day/5, вторая часть. Если сформулировать суть - текстом даются входные диапазоны, которые надо прогнать через серию маппингов, у которых заданы разные диапазоны источников. Т.е. напрашивается сущность Карта, которая при инициализации парсит текст, задавая собственные правила преобразования и соответственно она будет иметь метод mapping, который преобразует входные данные в результат. Тогда по факту всю ключевую логику можно будет выразить в несколько строк:

```py
for almanac_part in almanac_parts[1:]:
    current_map = Map(almanac_part)
    src = current_map.mapping(src)
```
Ну и целиком это будет выглядеть так:

```py

import os


class Map:
    def __init__(self, almanac_part):
        almanac_part = almanac_part.splitlines()
        self._name = almanac_part[0][:-1]
        self._map = []
        for record in almanac_part[1:]:
            dst_start, src_start, range_length = map(int, record.split(" "))
            self._map.append([dst_start, src_start, range_length])

    def mapping(self, source):
        dst = []
        while source:
            (src_start, src_range_length) = source.pop()
            is_not_in_map = True
            for dst_start, map_start, map_range_length in self._map:
                if (
                    src_start >= (map_start + map_range_length)
                    or (src_start + src_range_length - 1) < map_start
                ):
                    continue  # этот маппинг не применим к этому входному диапазону

                if map_start <= src_start < (
                    map_start + map_range_length
                ) and map_start <= (src_start + src_range_length) <= (
                    map_start + map_range_length
                ):
                    dst.append((dst_start + (src_start - map_start), src_range_length))
                    is_not_in_map = False
                    break  # входной диапазон целиком внутри маппинга

                if map_start > src_start and map_start <= (
                    src_start + src_range_length
                ) <= (map_start + map_range_length):
                    dst.append((dst_start, src_start + src_range_length - map_start))
                    source.append((src_start, map_start - src_start))
                    is_not_in_map = False
                    break  # входной диапазон начинается ДО маппинга

                if map_start <= src_start < (map_start + map_range_length) and (
                    src_start + src_range_length
                ) > (map_start + map_range_length):
                    dst.append(
                        (
                            dst_start + (src_start - map_start),
                            (map_start + map_range_length - src_start),
                        )
                    )
                    source.append(
                        (
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break  # входной диапазон заканчивается после маппинга

                if map_start > src_start and (src_start + src_range_length) > (
                    map_start + map_range_length
                ):
                    dst.append((dst_start, map_range_length))
                    source.append((src_start, map_start - src_start))
                    source.append(
                        (
                            (map_start + map_range_length),
                            (
                                src_start
                                + src_range_length
                                - (map_start + map_range_length)
                            ),
                        )
                    )
                    is_not_in_map = False
                    break  # маппинг перекрывает середину входного диапазона

            if is_not_in_map:  # для входного диапазона не нашёлся подходящий маппинг
                dst.append((src_start, src_range_length))
        return dst


def create_maps(almanac):
    almanac_parts = almanac.split("\n\n")

    seeds_v = list(map(int, almanac_parts[0][7:].split(" ")))
    seeds = []
    for i in range(len(seeds_v) // 2):
        seeds.append((seeds_v[2 * i], seeds_v[2 * i + 1]))

    src = seeds
    for almanac_part in almanac_parts[1:]:
        current_map = Map(almanac_part)
        src = current_map.mapping(src)
    return src


test_almanac = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
humidity_to_location = create_maps(test_almanac)
humidity_to_location.sort(key=lambda x: x[0])
assert humidity_to_location[0][0] == 46

input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    almanac = fd.read()
    humidity_to_location = create_maps(almanac)
    humidity_to_location.sort(key=lambda x: x[0])
    print(humidity_to_location[0][0])
```

Неожиданный эффект - это не только сделало код более наглядным, но и сократил его

## Пример 2

```py
import os


def count_win(camel_cards):
    all_hands = []
    cards_weight = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0,
    }
    for line in camel_cards.splitlines():
        hand, bid = line.split(" ")
        bid = int(bid)
        cards = dict()

        hands_weight = 0
        for card in hand:
            cards[card] = cards.get(card, 0) + 1
            hands_weight = hands_weight * 13 + cards_weight[card]

        if 5 in cards.values():
            hand_type = 7
        elif 4 in cards.values():
            hand_type = 6
        elif 3 in cards.values() and 2 in cards.values():
            hand_type = 5
        elif 3 in cards.values():
            hand_type = 4
        elif 2 in cards.values() and len(cards.values()) == 3:
            hand_type = 3
        elif 2 in cards.values() and len(cards.values()) == 4:
            hand_type = 2
        else:
            hand_type = 1

        all_hands.append((hand, bid, hand_type, hands_weight))

    all_hands.sort(key=lambda x: (x[2], x[3]))
    range = 1
    total_winnings = 0
    for _, bid, hand_type, hands_weight in all_hands:
        total_winnings += range * bid
        range += 1
    return total_winnings


test_camel_cards = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
total_winnings = count_win(test_camel_cards)
assert total_winnings == 6440


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    total_winnings = count_win(fd.read())
    print(total_winnings)
```

Это из задания https://adventofcode.com/2023/day/7 - первая часть. Есть сущность "Рука" (комбинация карт), имеющая атрибуты "вес" (задаётся последовательностью карт) и собственно "комбинацию" (по аналогии с покером). Соответственно напрашивается при инициализии объекта этой сущности распарсить из текста какие карты на руке и рассчитать эти атрибуты. В итоге вместо расчет всех рук становится очень наглядным

```py
for line in camel_cards.splitlines():
    str_hand, bid = line.split(" ")
    hand = Hand(str_hand)
    bid = int(bid)
    all_hands.append((hand.combination, hand.hands_weight, bid))
```

Ну и целиком это будет выглядеть так

```py
import os


class Hand:
    def __init__(self, str_hand):
        self.hands_weight = Hand.calculate_hands_weight(str_hand)
        self.combination = Hand.calculate_combination(str_hand)

    @staticmethod
    def calculate_hands_weight(str_hand):
        cards_weight = {
            "A": 12,
            "K": 11,
            "Q": 10,
            "J": 9,
            "T": 8,
            "9": 7,
            "8": 6,
            "7": 5,
            "6": 4,
            "5": 3,
            "4": 2,
            "3": 1,
            "2": 0,
        }
        hands_weight = 0
        for card in str_hand:
            hands_weight = hands_weight * 13 + cards_weight[card]
        return hands_weight

    @staticmethod
    def calculate_combination(str_hand):
        cards = dict()
        for card in str_hand:
            cards[card] = cards.get(card, 0) + 1
        if 5 in cards.values():
            return 7
        if 4 in cards.values():
            return 6
        if 3 in cards.values() and 2 in cards.values():
            return 5
        if 3 in cards.values():
            return 4
        if 2 in cards.values() and len(cards.values()) == 3:
            return 3
        if 2 in cards.values() and len(cards.values()) == 4:
            return 2
        return 1


def count_win(camel_cards):
    all_hands = []

    for line in camel_cards.splitlines():
        str_hand, bid = line.split(" ")
        hand = Hand(str_hand)
        bid = int(bid)
        all_hands.append((hand.combination, hand.hands_weight, bid))

    all_hands.sort(key=lambda x: (x[0], x[1]))
    range = 1
    total_winnings = 0
    for _, _, bid in all_hands:
        total_winnings += range * bid
        range += 1
    return total_winnings


test_camel_cards = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
total_winnings = count_win(test_camel_cards)
assert total_winnings == 6440


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    camel_cards = fd.read()

total_winnings = count_win(camel_cards)
print(total_winnings)
```

## Пример 3.

```py
import os


def count_win(camel_cards):
    all_hands = []
    cards_weight = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }
    for line in camel_cards.splitlines():
        hand, bid = line.split(" ")
        bid = int(bid)
        cards = dict()

        hands_weight = 0
        for card in hand:
            cards[card] = cards.get(card, 0) + 1
            hands_weight = hands_weight * 13 + cards_weight[card]

        J_number = cards.get("J", 0)
        other_card = [x for x in cards.values()]
        if J_number > 0:
            other_card.remove(J_number)

        first_other_card = 0
        if other_card:
            first_other_card = max(other_card)
            other_card.remove(first_other_card)

        second_other_card = 0
        if other_card:
            second_other_card = max(other_card)
            other_card.remove(second_other_card)

        if first_other_card + J_number == 5:
            hand_type = 7
        elif first_other_card + J_number == 4:
            hand_type = 6
        elif first_other_card + J_number == 3 and second_other_card == 2:
            hand_type = 5
        elif first_other_card + J_number == 3:
            hand_type = 4
        elif first_other_card + J_number == 2 and second_other_card == 2:
            hand_type = 3
        elif first_other_card + J_number == 2:
            hand_type = 2
        else:
            hand_type = 1

        all_hands.append((hand, bid, hand_type, hands_weight))

    all_hands.sort(key=lambda x: (x[2], x[3]))
    range = 1
    total_winnings = 0
    for _, bid, hand_type, hands_weight in all_hands:
        total_winnings += range * bid
        range += 1
    return total_winnings


test_camel_cards = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
total_winnings = count_win(test_camel_cards)
assert total_winnings == 5905


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    total_winnings = count_win(fd.read())
    print(total_winnings)
```

Это вторая часть предыдущего задания https://adventofcode.com/2023/day/7. Для сущности "Рука" меняются правила расчета атрибутов - сразу понятно где именно надо будет внести изменения. В данном случае даже добавился ещё один метод, но главное то, что не возникает вопросов, всё ли нужное я поменял

```py
import os


class Hand:
    def __init__(self, str_hand):
        self.hands_weight = Hand.calculate_hands_weight(str_hand)
        self.combination = Hand.calculate_combination(str_hand)

    @staticmethod
    def calculate_hands_weight(str_hand):
        cards_weight = {
            "A": 12,
            "K": 11,
            "Q": 10,
            "T": 9,
            "9": 8,
            "8": 7,
            "7": 6,
            "6": 5,
            "5": 4,
            "4": 3,
            "3": 2,
            "2": 1,
            "J": 0,
        }
        hands_weight = 0
        for card in str_hand:
            hands_weight = hands_weight * 13 + cards_weight[card]
        return hands_weight

    @staticmethod
    def calculate_combination(str_hand):
        cards = dict()
        for card in str_hand:
            cards[card] = cards.get(card, 0) + 1
        J_number, first_other_card, second_other_card = Hand.active_cards(cards)
        if first_other_card + J_number == 5:
            return 7
        if first_other_card + J_number == 4:
            return 6
        if first_other_card + J_number == 3 and second_other_card == 2:
            return 5
        if first_other_card + J_number == 3:
            return 4
        if first_other_card + J_number == 2 and second_other_card == 2:
            return 3
        if first_other_card + J_number == 2:
            return 2
        return 1

    @staticmethod
    def active_cards(cards):
        J_number = cards.get("J", 0)
        other_card = [x for x in cards.values()]
        if J_number > 0:
            other_card.remove(J_number)

        first_other_card = 0
        if other_card:
            first_other_card = max(other_card)
            other_card.remove(first_other_card)

        second_other_card = 0
        if other_card:
            second_other_card = max(other_card)
            other_card.remove(second_other_card)
        return J_number, first_other_card, second_other_card


def count_win(camel_cards):
    all_hands = []

    for line in camel_cards.splitlines():
        str_hand, bid = line.split(" ")
        hand = Hand(str_hand)
        bid = int(bid)
        all_hands.append((hand.combination, hand.hands_weight, bid))

    all_hands.sort(key=lambda x: (x[0], x[1]))
    range = 1
    total_winnings = 0
    for _, _, bid in all_hands:
        total_winnings += range * bid
        range += 1
    return total_winnings


test_camel_cards = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
total_winnings = count_win(test_camel_cards)
assert total_winnings == 5905


input_file_path = os.path.dirname(os.path.realpath(__file__)) + "//input.txt"
with open(input_file_path) as fd:
    camel_cards = fd.read()

total_winnings = count_win(camel_cards)
print(total_winnings)
```

## Общие выводы:

- были опасения что это добавит избыточного кода - по факту количество строк остаётся плюс-минус тем же
- это сильно упрощает чтение кода. Перечитывая исходные версии, мне приходилось вчитываться чтобы вспомнить, как же работает код, хотя написал его буквально три недели назад. Выделение правильных сущностей отделяет всю "техническую" часть от "бизнес-логики" - разбираться становится реально проще
- это упрощает внесение изменение - не надо выискивать по коду, надо ли что-то ещё где-то поменять, а сейчас это сразу сужается до метода в десять-двадцать строчек
- неожиданный эффект - как то стало яснее зачем вообще нужен ООП. Когда использовал ООП на курсе Алгоритмы и структуры данных - что-то такое начало в мозгу складываться, а вот сейчас, на этих задачах реально стало понятно что дают собственные классы и в чём их плюсы по сравнению с чисто императивным подходом