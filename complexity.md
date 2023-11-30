Исходный файл - [bst_original.py](bst_original.py) - взят из домашнего задания курса "Алгоритмы и структуры данных". Тема чистого кода на тот момент была не особо знакома, плюс в принципе концентрация была на том чтобы решить задачу, а не на понятность кода или на снижение алгоритмической сложности, поэтому что оптимизировать - есть. Проверка, что рефакторинг не меняет логику - с помощью тестов [test_bst.py](test_bst.py). Тесты к слову тоже нужно бы переделать - сейчас некоторые вещи сделал бы по другому. Оптимизированый модуль - [bst.py](bst.py).

Первый шаг - метод DeepAllNodes. В исходном файле это 32 строки, вычислительная сложность (compexicity) - 13
```python
    def DeepAllNodes(self, order=0):
        if self.Root is None:
            return ()
        nodes_for_check = []
        checked_nodes = set()
        result = []
        current_node = self.Root
        while current_node is not None:
            if current_node in checked_nodes:
                is_not_checked = False
            else:
                is_not_checked = True
            if is_not_checked and order == 0:
                nodes_for_check.extend(
                    [current_node.RightChild, current_node, current_node.LeftChild]
                )
            elif is_not_checked and order == 1:
                nodes_for_check.extend(
                    [current_node, current_node.RightChild, current_node.LeftChild]
                )
            elif is_not_checked and order == 2:
                nodes_for_check.extend(
                    [current_node.RightChild, current_node.LeftChild, current_node]
                )
            if is_not_checked:
                checked_nodes.add(current_node)
            else:
                result.append(current_node)
            current_node = None
            while current_node is None and nodes_for_check:
                current_node = nodes_for_check.pop()
        return tuple(result)
```

После оптимизации строк осталось почти столько же. Метод стал проще (compexicity - 3), но из метода выделился один приватный метод (compexicity - 2) плюс создался целый класс (compexicity - 2)

```python
    def DeepAllNodes(self, order=0):
        nodes_for_check = ListWithoutNone((self.Root,))
        checked_nodes = set()
        result = []
        while nodes_for_check:
            current_node = nodes_for_check.pop()
            if current_node in checked_nodes:
                result.append(current_node)
                continue
            nodes_for_check.extend(
                self._custom_order_node_with_children(current_node, order)
            )
            checked_nodes.add(current_node)
        return tuple(result)

    @staticmethod
    def _custom_order_node_with_children(node, order):
        """
        Задаёт нужный порядок узла и его потомков, в зависимости от задания"""
        order_keys = {
            0: (0, 1, 2),  # in-order
            1: (1, 0, 2),  # post-order
            2: (0, 2, 1)}  # pre-order  
        nodes = [node.RightChild, node, node.LeftChild]
        custom_order = ListWithoutNone()
        for i in order_keys[order]:
            custom_order.append(nodes[i])
        return custom_order


class ListWithoutNone(list):
    """
    Расширение списка list, которое удаляет помещённые в него элементы None"""
    def __init__(self, iterable=(None,)):
        super().__init__(filter(lambda x: x is not None, iterable))

    def append(self, item):
        super().extend(filter(lambda x: x is not None, [item]))
```

Использование класса ListWithoutNone (расширение списка list, которое удаляет помещённые в него элементы None) позволило полностью отказаться от проверки узлов и их потомков на is None

Вынос метода _custom_order_node_with_children() сделала более наглядной логику метода DeepAllNodes(). Плюс внутри самого метода реализовано использование таблицы данных вместо нескольких if

В итоге внутри метода DeepAllNodes() всего один цикл и одно условие внутри него - можно сказать минимально-оптимальная структура