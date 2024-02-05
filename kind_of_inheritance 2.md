```python
# variation inheritance
class Animal():
  def sound(self):
    print('some sounds')

class Dog(Animal):
  def sound(self):
    print('woof-woof')

class Cat(Animal):
  def sound(self):
    print('meow-meow')


# reification inheritance
class Animal():
  def sound(self):
    pass

class Dog(Animal):
  def sound(self):
    print('woof-woof')

class Cat(Animal):
  def sound(self):
    print('meow-meow')


# structure inheritance
class Person:
  self.strength = 10
  self.stamina = 10
  self.health = 100

class Attack()
  def attack(self, strength, weapon):
    return strength * weapon.damage

class Warrier(Person, Attack):
  self.weapon = 'Sword'
```