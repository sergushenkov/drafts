from typing import final

class EventListener(object):
    
    @final
    def legasy_metod(self):
        print("it's method EventListener!")


class DelegateA(EventListener):
    def legasy_metod(self):
        print("it's A!!!")

    def new_method(self):
        print("it's new method")


a = DelegateA()
a.legasy_metod()
a.new_method() 

"""
Пытался найти вариант, как запретить перезапись метода в наследуемом классе - на стековерфлоу наткнулся на вариант с делегированием, н
о - он не позволяет создавать новые методы, которых нет в классе-родителе. 
И в этом контексте становится вообще непонятно, зачем может быть нужен такой способ

В общем, похоже в python это нереализуемо 
"""


"""
Возможность запрета и для методов, и для классов, 
появилась в Python 3.8 -- 
с помощью декоратора @final


class Base:
    @final
    def do_not_override_this(self) -> None: ...

class A(Base):
    # error: Cannot override final attribute "do_not_override_this"
    # (previously declared in base class "Base")
    def do_not_override_this(self) -> None: ...


@final
class FinalBase: ...

class B(FinalBase): ...
# error: Cannot inherit from final class "FinalBase"
"""