class EventListener(object):
    def __init__(self, delegate):
        self.delegate = delegate

    def legasy_metod(self):
        print("it's method EventListener!")


class DelegateA(object):
    def legasy_metod(self):
        print("it's A!!!")

    def new_method(self):
        print("it's new method")


a = EventListener(DelegateA())
a.legasy_metod()
# a.new_method()  # AttributeError: 'EventListener' object has no attribute 'new_method'

"""
Пытался найти вариант, как запретить перезапись метода в наследуемом классе - на стековерфлоу наткнулся на вариант с делегированием, н
о - он не позволяет создавать новые методы, которых нет в классе-родителе. 
И в этом контексте становится вообще непонятно, зачем может быть нужен такой способ

В общем, похоже в python это нереализуемо 
"""