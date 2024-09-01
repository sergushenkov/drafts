"""
Ряд моментов не задан, сделал предположения, но необходимо уточнить у заказчика:
. Начальные координаты - (0,0), начальный угол - 0
. Координаты отображаются с точностью до 0.1 м
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
    state = "brush"
    clean_on = False

    def transfer_to_cleaner(self, rez):
        print(rez)

    def command(self, code):
        action = self.transfer_to_cleaner
        for s in code:
            s = s.strip().split(" ")
            if s[0] == "move":
                distance = float(s[1])
                action(self.move(distance))
            if s[0] == "turn":
                delta_angle = int(s[1])
                action(self.turn(delta_angle))
            if s[0] == "set":
                new_state = s[1]
                action(self.set(new_state))
            if s[0] == "start":
                action(self.start())
            if s[0] == "stop":
                action(self.stop())

    def move(self, distance):
        x, y = self.position
        angle_radians = math.radians(self.angle)
        x += distance * math.sin(angle_radians)
        y += distance * math.cos(angle_radians)
        self.position = (x, y)
        return f"POS {round(x, 1)},{round(y, 1)}"

    def turn(self, delta_angle):
        self.angle = (self.angle + 360 + delta_angle) % 360
        return f"ANGLE {self.angle}"

    def set(self, new_state):
        self.clean_on = False
        self.state = new_state
        return f"STATE {self.state}"

    def start(self):
        self.clean_on = True
        return f"START WITH {self.state}"

    def stop(self):
        self.clean_on = False
        return "STOP"


code = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

if __name__ == "__main__":
    cleaner = Cleaner()
    cleaner.command(code)
