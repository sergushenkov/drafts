class NewSet(set):
    def __add__(self, other):
        return NewSet(self.union(other))


for x, y in ((1, 1), ("1", "1"), ([1], [1]), (NewSet((1,)), NewSet((1,)))):
    print(f"{type(x)}: {x} + {y} = {x + y}")
