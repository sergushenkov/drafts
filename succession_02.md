Наследование через расширение класса-родителя вроде бы возможно в двух вариантах:
1) через расширение количества объектов входящих в класс - выглядит как костыльный вариант, чтобы не переделывать структуру, добавляют доп. атрибуты в уже имеющиеся классы так, чтобы эти атрибуты перекрывали дефолтные значения классов родителей. На самом деле не уверен что так делают - потому что выглядит уродливо. Класс Craft наследует все атрибуты класса Boat (), но дополнительно имеет флаг self.is_fly. Дефолтное значение False всё также про водные суда, а значения True - про воздушные суда
2) через расширение функционала - появление новых методов. В классе MotorBoat(Boat) появляется метод start_the_engine(), недоступный классу-родителю

Наследование через специализацию класса-родителя - выглядит более логичным, когда через добавление дефолтных атрибутов выделяют некоторое количество объектов родительского класса: WoodenBoat(Boat) содержит только лодки сделанные из древесины

```python
# лодка
class Boat:
    def __init__(self):
        print('boat...')
 
# класс судно - если может летать, то самолёт, если нет то лодка
class Craft(Boat):
    def __init__(self, is_fly = False):
        self.is_fly = is_fly

# расширение функционала класса-родителя
class MotorBoat(Boat)
    def start_the_engine(self):
        print("the engine is working...")

# специализация класса-родителя
class WoodenBoat(Boat):
    def __init__(self):
        self.material = 'wood'
```
