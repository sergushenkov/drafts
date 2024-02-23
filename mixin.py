class RadioMixin(object):
    def play_song_on_station(self, station):
        print(f"In {self.name} play song on station {station}")


class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving {self.name} with max speed {self.max_speed}")


class Car(Vehicle, RadioMixin):
    pass


class Boat(Vehicle):
    pass


class Buildiing:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House(Buildiing, RadioMixin):
    pass


sweat_home = House("Sweat home", 100)
sweat_home.play_song_on_station("102FM")

my_car = Car("ВАЗ 2110", 140)
my_car.drive()
my_car.play_song_on_station("Европа плюс")

my_boat = Boat("Надувной матрас", 5)
my_boat.drive()
try:
    my_boat.play_song_on_station("Европа плюс")
except AttributeError:
    print(f"{my_boat.name} dont have radio :(")
