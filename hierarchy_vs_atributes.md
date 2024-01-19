Вместо атрибута с набором предопределённых значений лучше применять наследование от родителя.

## НЕПРАВИЛЬНО

```python
class Vegetables():
  def __init__(self, kind):
    self.kind = kind

  def cook(self):
    if self.kind == 'potato':
      return 'mash'
    if self.kind == 'cabbage':
      return 'soup'
    if self.kind == 'tomato':
      return 'salad'    
```

## ПРАВИЛЬНО

```python
class Vegetables():
  def cook(self):
    pass

class Potato(Vegetables):
  def cook(self):
    return 'mash'

class Cabbage(Vegetables):
  def cook(self):
    return 'soup'

class Tomato(Vegetables):
  def cook(self):
    return 'salad'
```