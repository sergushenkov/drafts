# inheritance of the type
class Weapon:
    name = None
    damage = None
    weight = None

class Sword(Weapon):
    name = 'Sword'
    damage = 10
    weight = 10

class Axe(Weapon):
    name = 'Axe'
    damage = 15
    weight = 15

class Warrior:
    name = None
    weapon = None
    
    def attack(self):
        pass

class Knight(Warrior):
    name = 'Knight'
    weapon = Sword()

class Barbarian(Warrior):
    name = 'Barbarian'
    weapon = Axe()
