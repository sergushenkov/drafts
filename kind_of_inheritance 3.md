Пример для implementation inheritance придумать не смог - не понимаю как можно наследовать программную реализацию для уникальной абстракции структуры данных. В обратную сторону - легко 

```python
# facility inheritance
class Transport:
    self.environment = ['land', 'water', 'air']
    self.cargo = []
    def deliver(self, cargo)

class Boat(Transport):
    self.environment = ['water']

class Plane(Transport):
    self.environment = ['air']
```