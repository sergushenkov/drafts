


Двухсвязанный список, написан по TDD, первая версия

```
class Node:
    def __init__(self, val=None):
        self.value = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFront(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def addTail(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def removeFront(self):
        if self.head is None:
            return None
        node = self.head
        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.prev = None
        return node.value

    def removeTail(self):
        if self.tail is None:
            return None
        node = self.tail
        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = node.prev
            self.tail.next = None
        return node.value

    def size(self):
        cnt = 0
        node = self.head
        while node is not None:
            cnt += 1
            node = node.next
        return cnt
```

Тесты к первой версии двухсвязного списка:

```
import unittest
from deque import Deque


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_addFront_removeTail(self):
        self.assertIsNone(self.deque.removeTail(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')
        for i in range(5):
            self.assertEqual(self.deque.size(), i, 'length is not correct')
            self.deque.addFront(i)
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
        self.assertEqual(self.deque.head.value, 4, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.value, 3,
                         'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.value,
                         2, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.value,
                         1, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.next.value,
                         0, 'tail.value is not correct')
        self.assertEqual(self.deque.head, self.deque.tail.prev.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next, self.deque.tail.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next, self.deque.tail.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next, self.deque.tail.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next.next, self.deque.tail,
                         'deque is not correct')
        for i in range(5):
            self.assertEqual(self.deque.size(), 5 - i, 'length is not correct')
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
            self.assertEqual(self.deque.removeTail(), i, 'tail is not correct')
        self.assertIsNone(self.deque.removeTail(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')

    def test_addTail_removeFront(self):
        self.assertIsNone(self.deque.removeFront(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')
        for i in range(5):
            self.assertEqual(self.deque.size(), i, 'length is not correct')
            self.deque.addTail(i)
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
        self.assertEqual(self.deque.head.value, 0, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.value, 1,
                         'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.value,
                         2, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.value,
                         3, 'tail.value is not correct')
        self.assertEqual(self.deque.head.next.next.next.next.value,
                         4, 'tail.value is not correct')
        self.assertEqual(self.deque.head, self.deque.tail.prev.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next, self.deque.tail.prev.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next, self.deque.tail.prev.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next, self.deque.tail.prev,
                         'deque is not correct')
        self.assertEqual(self.deque.head.next.next.next.next, self.deque.tail,
                         'deque is not correct')
        for i in range(5):
            self.assertEqual(self.deque.size(), 5 - i, 'length is not correct')
            self.assertIsNone(self.deque.head.prev, 'head.prev is not None')
            self.assertIsNone(self.deque.tail.next, 'tail.next is not None')
            self.assertEqual(self.deque.removeFront(),
                             i, 'tail is not correct')
        self.assertIsNone(self.deque.removeFront(),
                          'empty deque return not None')
        self.assertIsNone(self.deque.head, 'head is not None')
        self.assertIsNone(self.deque.tail, 'tail is not None')


if __name__ == '__main__':
    unittest.main()
```

Двухсвязанный список, написан с использованием спецификаций, вторая версия

```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Dequeue():
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
        self._remove_status = Dequeue.REMOVE_ERR
        self._get_status = Dequeue.GET_ERR

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
            self._remove_status = Dequeue.REMOVE_ERR
            return
        self._remove_status = Dequeue.REMOVE_OK
        self._size -= 1
        if self._head.next is None:
            self._head = None
            self._tail = None
            return
        self._tail.prev.next = None
        self._tail = self._tail.prev

    def remove_front(self):
        """
        Предусловие - очередь не пуста
        Постусловие - удалено значение из головы, сместив очередь влево"""
        if self._head is None:
            self._remove_status = Dequeue.REMOVE_ERR
            return
        self._remove_status = Dequeue.REMOVE_OK
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
            self._get_status = Dequeue.GET_ERR
            return None
        self._get_status = Dequeue.GET_OK
        return self._head.value

    def size(self):
        return self._size

    def get_get_status(self):
        return self._get_status

    def get_remove_status(self):
        return self._remove_status



    def get_tail(self):
        """
        выдача из головы"""
        if self._head is None:
            self._get_status = Dequeue.GET_ERR
            return None
        self._get_status = Dequeue.GET_OK
        return self._tail.value
```

Тесты ко второй версии двухсвязного списка:

```
from dequeue import Dequeue


def test_queue_init():
    tq = Dequeue()
    assert tq.size() == 0
    assert tq.get_get_status() == Dequeue.GET_ERR
    assert tq.get_remove_status() == Dequeue.REMOVE_ERR


def test_queue_add_tail():
    tq = Dequeue()
    assert tq.size() == 0
    tq.add_tail(0)
    assert tq.size() == 1
    tq.add_tail(1)
    assert tq.size() == 2


def test_queue_get():
    tq = Dequeue()
    assert tq.get_head() is None
    assert tq.get_get_status() == Dequeue.GET_ERR
    tq.add_tail(0)
    assert tq.get_head() == 0
    assert tq.get_get_status() == Dequeue.GET_OK
    tq.add_tail(1)
    assert tq.get_head() == 0


def test_queue_remove_front():
    tq = Dequeue()
    for i in range(3):
        tq.add_tail(i)
    assert tq.get_head() == 0
    tq.remove_front()
    assert tq.size() == 2
    assert tq.get_head() == 1
    assert tq.get_get_status() == Dequeue.GET_OK
    tq.remove_front()
    tq.remove_front()
    assert tq.get_head() is None
    assert tq.get_get_status() == Dequeue.GET_ERR
    assert tq.get_remove_status() == Dequeue.REMOVE_OK
    assert tq.size() == 0
    tq.remove_front()
    assert tq.get_remove_status() == Dequeue.REMOVE_ERR
    assert tq.size() == 0


def test_dequeue_init():
    dq = Dequeue()
    assert dq.size() == 0
    assert dq.get_get_status() == Dequeue.GET_ERR
    assert dq.get_remove_status() == Dequeue.REMOVE_ERR


def test_dequeue_add_front():
    dq = Dequeue()
    dq.add_front(1)
    assert dq.size() == 1
    dq.add_front(2)
    assert dq.size() == 2
    dq.add_front(3)
    assert dq.size() == 3
    assert dq.get_head() == 3
    assert dq.get_get_status() == Dequeue.GET_OK
    dq.remove_front()
    assert dq.get_remove_status() == Dequeue.REMOVE_OK
    assert dq.size() == 2
    assert dq.get_head() == 2
    assert dq.get_get_status() == Dequeue.GET_OK
    dq.remove_front()
    assert dq.get_head() == 1
    assert dq.size() == 1


def test_dequeue_remove_tail():
    dq = Dequeue()
    dq.remove_tail()
    assert dq.size() == 0
    assert dq.get_remove_status() == Dequeue.REMOVE_ERR
    dq.add_front(1)
    dq.add_front(2)
    assert dq.get_tail() == 1
    dq.remove_tail()
    assert dq.get_remove_status() == Dequeue.REMOVE_OK
    assert dq.size() == 1
    assert dq.get_tail() == 2
    dq.remove_tail()
    assert dq.get_remove_status() == Dequeue.REMOVE_OK
    assert dq.size() == 0
    assert dq.get_tail() is None
    dq.remove_tail()
    assert dq.get_remove_status() == Dequeue.REMOVE_ERR
    assert dq.size() == 0
```