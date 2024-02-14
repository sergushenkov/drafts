"""
По хорошему конечно надо сделать ещё версию этого же кода, но без использования паттерна Visitor,
но понимаю, что мне просто страшно браться за это. Я очень оценил, то что не надо заморачиваться
какой метод инструмента применять в данный конкретный момент для данного конкретного объекта на пути. 
Даже мысленно представляя, какая мешанина будет даже с десятком объектов - жутко. Используя Visitor можно спокойно создавать сотни объектов,
а потом обращаться к ним в любой момент.
Плюс, если потребуется что-то поменять в механике - с Visitor это будет очень легко. Если же хардкодить все вызовы в коде - надо будет долго потом отлаживать,
очень жёсткая структура получится.
Наверное, первый паттерн, где есть именно ощущение "Вау", а не просто - "Ну это же банально" 
(хотя я конечно в паттернах по прежнему не особо силён :)).
Однозначно, беру себе в копилку. Правда в дата-инженерных задачах нынешнего уровня не особо актуально, 
но для крупных проектов точно неоценимо.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Thing(ABC):
    @abstractmethod
    def use(self, visitor: Visitors) -> None:
        pass


class Axe(Thing):
    toughness = 100

    def use(self, visitor: Visitors) -> None:
        visitor.destroy(self)

    def attack(self) -> int:
        if self.toughness == 0:
            print("Вашим топором невозможно пользоваться")
            return 0
        print("Вы наносите сильный удар топором")
        self.toughness -= 1
        if self.toughness <= 0:
            print("Топор разваливается у вас в руках")
            return 5
        return 25


class Picklock(Thing):
    def use(self, visitor: Visitors):
        visitor.picklock(self)

    def pick_the_lock(self) -> str:
        print("Вам удается вскрыть замок")
        return True


class MagicScroll(Thing):
    def use(self, visitor: Visitors):
        visitor.explore(self)


class Visitors(ABC):
    name = ""
    is_closed = True

    @abstractmethod
    def destroy(self, element: Axe) -> None:
        pass

    @abstractmethod
    def picklock(self, element: Picklock) -> None:
        pass

    @abstractmethod
    def explore(self, element: MagicScroll) -> str:
        pass


class WoodDoor(Visitors):
    name = "Деревянная дверь"
    is_closed = True
    toughness = 10
    description = "Запертая деревянная дверь, она не выглядит слишком прочной"

    def destroy(self, thing) -> None:
        print("Вы пытаетесь разбить дверь")
        damage = thing.attack()
        if damage >= self.toughness:
            print("Ваше оружие взламывает дверь")
            self.is_closed = False
            self.description = "Сломанная деревянная дверь открыта нараспашку"
            return
        print("Вы нанесли небольшой урон двери")
        self.toughness -= damage

    def picklock(self, element) -> None:
        print("Вы пытаетесь взломать замок двери")
        if element.pick_the_lock():
            print("Вы успешно взломали замок")
            self.is_closed = False
            self.description = "Открытая деревянная дверь"

    def explore(self, element) -> None:
        print("Вы исследуете дверь")
        print(self.description)


class IronDoor(Visitors):
    name = "Стальная дверь"
    is_closed = True
    toughness = 1000
    description = "Запертая стальная дверь, похоже не получится её разбить"

    def destroy(self, thing) -> None:
        print("Вы пытаетесь разбить дверь")
        damage = thing.attack()
        if damage >= self.toughness:
            print("Ваше оружие взламывает дверь")
            self.is_closed = False
            self.description = "Разбитая стальная дверь открыта нараспашку"
            return
        print("Вы нанесли небольшую царапину")
        self.toughness -= damage

    def picklock(self, element) -> None:
        print("Вы пытаетесь взломать замок двери")
        if element.pick_the_lock():
            print("Вы успешно взломали замок")
            self.is_closed = False
            self.description = "Открытая стальная дверь"

    def explore(self, element) -> None:
        print("Вы исследуете дверь")
        print(self.description)


class Casket(Visitors):
    name = "Шкатулка"
    is_closed = True
    toughness = 5
    description = "Изящная шкатулка, заперта. Судя по весу - внутри что-то есть"

    def destroy(self, thing) -> None:
        print("Вы пытаетесь разбить шкатулку")
        damage = thing.attack()
        if damage >= self.toughness:
            print("Ваше оружие разбивает шкатулку вдребезги")
            self.is_closed = False
            self.description = (
                "Обломки шкатулки. Видны остатки флакона с каким-то эликсиром"
            )
            return
        print("Вы помяли шкатулку")
        self.toughness -= damage

    def picklock(self, element) -> None:
        print("Вы пытаетесь взломать замок шкатулки")
        if element.pick_the_lock():
            print("Вы успешно взломали замок")
            self.is_closed = False
            self.description = (
                "Открытая шкатулка, внутри лежит флакон с волшебным эликсиром"
            )

    def explore(self, element) -> None:
        print("Вы исследуете шкатулку")
        print(self.description)


if __name__ == "__main__":
    visitor1 = IronDoor()
    visitor2 = Casket()
    visitor3 = WoodDoor()
    ways = [visitor1, visitor2, visitor3]
    thing1 = Axe()
    thing2 = Picklock()
    thing3 = MagicScroll()
    things = {"1": thing1, "2": thing2, "3": thing3}

    while ways:
        visitor = ways.pop()
        while visitor.is_closed:
            print(f"Вы видите перед собой {visitor.name}")
            choose = input(
                "Что вы хотите использовать? Топор - 1, отмычку - 2, волшебный свиток - 3: "
            )
            thing = things[choose]
            thing.use(visitor)

    print("Вы вышли из подземелья")
