'''
Пример кода, где применяются наследование, композиция и полиморфизм.

Композиция.
Класс Queue_ASD содержит в себе класс Node (композиция, Queue_ASD has a Node). Естественно, если в классе Queue_ASD записано хотя бы одно значение - в пустом классе Queue_ASD класса Node нет.

Наследование.
Классы Queue и Dequeue являются наследниками класса Queue_ASD (наследование, Queue is a Queue_ASD). Класс Queue по факту является полной копией класса Queue_ASD, содержит все те же самые методы. Класс Dequeue наследует все методы Queue_ASD, переопределяет один из них (__len__()) и добавляет три дополнительных.

Полиморфизм.
Класс Queue_ASD содержит magic метод __len__(), который позволяет применять к объекту класса функцию len(). Причём функция может получать на вход объекты и других типов - строка, список, кортеж - и во всех случаях будет отрабатывать корректно (полиморфизм). Далее класс Queue наследует метод __len__() из Queue_ASD как есть, а класс Dequeue переопределяет её (код не оптимальный - просто для иллюстрации) - т.е. функция len() получая на вход объекты разного типа будет работать по разным алгоритмам и вернёт правильные данные для каждого случая.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Queue_ASD has a Node - смотри метод add_tail(self, value)
class Queue_ASD:
    GET_OK = 1  # последний get_*() отработал нормально
    GET_ERR = 2  # список пуст

    REMOVE_OK = 1  # последний remove_*() отработал нормально
    REMOVE_ERR = 2  # список пуст

    def __init__(self):
        """
        конструктор
        постусловие:
        1) создана новая пустая очередь
        2) статусы операций указывают что очередь пуста"""
        self._head = None
        self._tail = None
        self._size = 0
        self._remove_status = Queue.REMOVE_ERR
        self._get_status = Queue.GET_ERR

    def add_tail(self, value):
        """
        Постусловие - в хвост очереди добавлено новое значение"""
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
            self._size = 1
            return
        self._tail.next = node
        node.prev = self._tail
        self._tail = node
        self._size += 1

    def remove_front(self):
        """
        Предусловие - очередь не пуста
        Постусловие - удалено значение из головы, сместив очередь влево"""
        if self._head is None:
            self._remove_status = Queue.REMOVE_ERR
            return
        self._remove_status = Queue.REMOVE_OK
        self._size -= 1
        if self._head.next is None:
            self._head = None
            self._tail = None
            return
        self._head.next.prev = None
        self._head = self._head.next

    def get_head(self):
        """
        выдача из головы"""
        if self._head is None:
            self._get_status = Queue.GET_ERR
            return None
        self._get_status = Queue.GET_OK
        return self._head.value

    def __len__(self):
        return self._size

    def get_get_status(self):
        return self._get_status

    def get_remove_status(self):
        return self._remove_status


# Queue is a Queue_ASD
class Queue(Queue_ASD):
    pass


# Dequeue is a Queue_ASD
class Dequeue(Queue_ASD):
    def add_front(self, value):
        """
        Постусловие - в голову очереди добавлено новое значение"""
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
            self._size = 1
            return
        self._head.prev = node
        node.next = self._head
        self._head = node
        self._size += 1

    def remove_tail(self):
        """
        Предусловие - очередь не пуста
        Постусловие - удалено значение из хвоста"""
        if self._head is None:
            self._remove_status = Queue.REMOVE_ERR
            return
        self._remove_status = Queue.REMOVE_OK
        self._size -= 1
        if self._head.next is None:
            self._head = None
            self._tail = None
            return
        self._tail.prev.next = None
        self._tail = self._tail.prev

    def get_tail(self):
        """
        выдача из головы"""
        if self._head is None:
            self._get_status = Queue.GET_ERR
            return None
        self._get_status = Queue.GET_OK
        return self._tail.value

    def __len__(self):
        i = 0
        node = self._head
        while node is None:
            i += 1
            node = node.next
        return i