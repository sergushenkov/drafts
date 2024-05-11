from pymonad.tools import curry


# 2.3.1
@curry(2)
def add_str(x, y):
    return x + y


hi = add_str("Hello, ")
print(hi("Petya"))


# 2.3.2
@curry(4)
def first_step(a, b, c, d):
    return a + b + d + c


final = first_step("Hello")(", ")("!")
print(final("Petya"))
