class Vector:
    def __init__(self, list_of_values) -> None:
        self.values = []
        for val in list_of_values:
            self.values.append(val)

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.values, other.values)])


v1 = Vector(
    [
        Vector([Vector([1, 2, 3]), Vector([4, 5, 6])]),
        Vector([Vector([7, 8, 9]), Vector([10, 11, 12])]),
    ]
)

v2 = Vector(
    [
        Vector([Vector([13, 14, 15]), Vector([16, 17, 18])]),
        Vector([Vector([19, 20, 21]), Vector([22, 23, 24])]),
    ]
)

v = v1 + v2
print(v)

for a in v.values:
    for b in a.values:
        print(b.values)

"""
<__main__.Vector object at 0x000001C24F06B730>
[14, 16, 18]
[20, 22, 24]
[26, 28, 30]
[32, 34, 36]
"""