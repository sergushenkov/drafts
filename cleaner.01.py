"""
Ряд моментов не задан, сделал предположения, но необходимо уточнить у заказчика:
. Начальные координаты - (0,0), начальный угол - 0
. Начальное состояние устройства очистки - brush, не работает
. Угол поворота считается в градусах от вертикальной оси (если angle 0 - то move 10 увеличит координату y на 10)
. Движение в обратную сторону (move с отрицательным числом) не возможно
. Команда turn задаёт дельту от текущего угла, положительные значения по часовой, отрицательные - против
. Переключение режима работы в момент работы равносильно stop + set
. Две одинаковые команды подряд (start, stop, set x) или команда stop без предыдущего start не являются ошибкой и отрабатывают одинаково
. Неправильная команда не является ошибкой, никаких действий не вызывает
. Пустая строка заканчивает работу с программой
"""

import math


class Cleaner:
    STATES = {"brush", "water", "soap"}
    position = (0, 0)
    angle = 0
    current_state = "brush"
    clean_on = False

    def command(self, s):
        s = s.strip().split(" ")
        if len(s) == 2 and s[0] == "move" and s[1].isdigit():
            distance = int(s[1])
            return self.move(distance)
        if len(s) == 2 and s[0] == "turn" and s[1].lstrip("-").isdigit():
            delta_angle = int(s[1])
            return self.turn(delta_angle)
        if len(s) == 2 and s[0] == "set" and s[1] in self.STATES:
            next_state = s[1]
            return self.set(next_state)
        if len(s) == 1 and s[0] == "start":
            return self.start()
        if len(s) == 1 and s[0] == "stop":
            return self.stop()

    def move(self, distance):
        x, y = self.position
        angle_radians = math.radians(self.angle)
        x += int(distance * math.sin(angle_radians))
        y += int(distance * math.cos(angle_radians))
        self.position = (x, y)
        return f"POS {x},{y}"

    def turn(self, delta_angle):
        self.angle = (self.angle + 360 + delta_angle) % 360
        return f"ANGLE {self.angle}"

    def set(self, next_state):
        self.clean_on = False
        self.current_state = next_state
        return f"STATE {self.current_state}"

    def start(self):
        self.clean_on = True
        return f"START WITH {self.current_state}"

    def stop(self):
        self.clean_on = False
        return "STOP"


if __name__ == "__main__":
    cleaner = Cleaner()
    while True:
        s = input()
        if s == "":
            break
        rez = cleaner.command(s)
        if rez:
          print(rez)
