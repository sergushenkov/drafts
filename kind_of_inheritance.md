```python
# subtype inheritance
class ListSame(List):
    # все значения в списке - одного типа
    pass


# restriction inheritance
class ListWithoutNone(List):
    def add(self, value):
        if value is not None:
            self.append(value)


# extension inheritance
class ListOfPictures(list):
  def slide_show(self):
    for picture in self:
      picture.show()
```