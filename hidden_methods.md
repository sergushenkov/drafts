В python нет полноценного сокрытия методов. Можно добавить двойное подчеркивание в начале имени метода или переменной - к нему будет чуть сложнее обратиться снаружи класса, в котором этот атрибут определён, но с небольшими ухищрениями его всё таки можно вызвать как obj._MyClass__my_private_method(). Ну и всегда можно переписать метод в классе-наследнике.

```python

class MyClass():
  
  def my_public_method(self):
    print('Вариант 1 - метод публичен в родительском классе А и публичен в его потомке B')

  def __my_private_method(self):
    print('Вариант 4 - метод скрыт в родительском классе А и скрыт в его потомке B')


class MyClassSuccessor(MyClass):
  pass

parent = MyClass()
parent.my_public_method()  # публичный метод можно вызвать
# parent.__my_private_method()  # "приватный" метод нельзя так просто вызвать
parent._MyClass__my_private_method()  # но можно вызвать так

child = MyClassSuccessor()  # всё также для потомка
child.my_public_method()  # публичный метод можно вызвать
# child.__my_private_method()  # "приватный" метод нельзя так просто вызвать
child._MyClassSuccessor__my_private_method()  # но можно вызвать так
```