Исходный файл - [bst_original.py](bst_original.py) - взят из домашнего задания курса "Алгоритмы и структуры данных". Тема чистого кода на тот момент была не особо знакома, плюс в принципе концентрация была на том, чтобы решить задачу, а не на понятность кода или на снижение цикломатической сложности, поэтому что оптимизировать - есть. Проверка, что рефакторинг не меняет логику - с помощью тестов [test_bst.py](test_bst.py). Тесты к слову тоже нужно бы переделать - сейчас некоторые вещи сделал бы по другому. Оптимизированный модуль - [bst.py](bst.py).

Первый шаг - метод DeepAllNodes. В исходном файле это 32 строки, цикломатическая сложность (compexicity) - 13
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

Но вот на втором методе (DeleteNodeByKey()) такого результата не удалось достичь
Была сложность 15

```python
    def DeleteNodeByKey(self, key):
        for_delete = self.FindNodeByKey(key)
        if for_delete.NodeHasKey is False:
            return False

        if for_delete.Node.LeftChild is None and for_delete.Node.RightChild is None:
            if for_delete.Node is self.Root:
                self.Root = None
                return True
            parent_node = for_delete.Node.Parent
            if parent_node.LeftChild is for_delete.Node:
                parent_node.LeftChild = None
            else:
                parent_node.RightChild = None
            return True

        if for_delete.Node.LeftChild is None or for_delete.Node.RightChild is None:
            if for_delete.Node.LeftChild is None:
                child_node = for_delete.Node.RightChild
            else:
                child_node = for_delete.Node.LeftChild
            parent_node = for_delete.Node.Parent
            child_node.Parent = parent_node
            if parent_node is None:
                self.Root = child_node
                return True
            if parent_node.LeftChild is for_delete.Node:
                parent_node.LeftChild = child_node
            else:
                parent_node.RightChild = child_node
            return True

        change_node = self.FinMinMax(for_delete.Node.RightChild, FindMax=False)
        if change_node is not for_delete.Node.RightChild:
            change_node.Parent.LeftChild = change_node.RightChild  # is None or node
        change_node.LeftChild = for_delete.Node.LeftChild
        change_node.LeftChild.Parent = change_node
        if for_delete.Node.RightChild is not change_node:
            change_node.RightChild = for_delete.Node.RightChild
            change_node.RightChild.Parent = change_node
        parent = for_delete.Node.Parent
        change_node.Parent = parent
        if parent is None:
            self.Root = change_node
            return True
        if parent.LeftChild is for_delete.Node:
            parent.LeftChild = change_node
        else:
            parent.RightChild = change_node
        return True
```

Стала 40 

```python
    def DeleteNodeByKey(self, key): 
        deleting_node = self.FindNodeByKey(key)

        if deleting_node.NodeHasKey is False:
            return False
        
        has_left_child = deleting_node.Node.LeftChild is not None
        has_right_child =  deleting_node.Node.RightChild is not None
        has_parent = deleting_node.Node is self.Root
        parent = deleting_node.Node.Parent
        if has_parent :
            is_left_child = parent.LeftChild is deleting_node.Node

        if not(has_left_child or has_right_child) and not has_parent:
            self.Root = None
            return True

        if not(has_left_child or has_right_child) and has_parent and is_left_child:            
            parent.LeftChild = None
            return True

        if not(has_left_child or has_right_child) and has_parent and not is_left_child:    
            parent.RightChild = None
            return True

        if has_left_child and not has_right_child and not has_parent:
            child_node = deleting_node.Node.LeftChild
            self.Root = child_node
            return True

        if has_left_child and not has_right_child and has_parent and is_left_child:
            child_node = deleting_node.Node.LeftChild
            child_node.Parent = parent
            parent.LeftChild = child_node
            return True

        if has_left_child and not has_right_child and has_parent and not is_left_child:
            child_node = deleting_node.Node.LeftChild
            child_node.Parent = parent
            parent.RightChild = child_node
            return True

        if not has_left_child and not has_right_child and not has_parent:
            child_node = deleting_node.Node.RightChild
            self.Root = child_node
            return True

        if not has_left_child and not has_right_child and has_parent and is_left_child:
            child_node = deleting_node.Node.RightChild
            child_node.Parent = parent
            parent.LeftChild = child_node
            return True

        if not has_left_child and not has_right_child and has_parent and not is_left_child:
            child_node = deleting_node.Node.RightChild
            child_node.Parent = parent
            parent.RightChild = child_node
            return True

        change_node = self.FinMinMax(deleting_node.Node.RightChild, FindMax=False)
        if change_node is not deleting_node.Node.RightChild:
            change_node.Parent.LeftChild = change_node.RightChild 
        change_node.LeftChild = deleting_node.Node.LeftChild
        change_node.LeftChild.Parent = change_node
        if deleting_node.Node.RightChild is not change_node:
            change_node.RightChild = deleting_node.Node.RightChild
            change_node.RightChild.Parent = change_node
        parent = deleting_node.Node.Parent
        change_node.Parent = parent
        if parent is None:
            self.Root = change_node
            return True
        if parent.LeftChild is deleting_node.Node:
            parent.LeftChild = change_node
        else:
            parent.RightChild = change_node
        return True
```
Хотя вроде количество вложенных условий стало сильно меньше - сейчас большинство условий имеют вид if: return, код правда гораздо легче проверять

Третий пример: из идущего Advent of Code. Было (сложность 13):

```python
def find_details(text_schema):
    schema = text_schema.split('\n')
    gears = dict()
    for j, row in enumerate(schema):
        i = 0
        while i < len(row):
            if not row[i].isdigit():
                i += 1
                continue
            first_ch = i
            while i < len(row) and row[i].isdigit():
                i += 1
            last_ch = i
            is_gear = False
            start_row = max(j-1, 0)
            end_row = j + 1
            start_ch = max(first_ch - 1, 0)
            end_ch = last_ch + 1
            for delta_row, check_row in enumerate(schema[start_row:end_row + 1]):
                for delta_ch, ch in enumerate(check_row[start_ch:end_ch]):
                    if ch == "*":
                        is_gear = True
                        xy = (start_row+delta_row, start_ch+delta_ch)
                        if xy in gears:                        
                            gears[xy].append(int(row[first_ch:last_ch]))
                        else:
                            gears[xy] = [int(row[first_ch:last_ch])]
                        break
                if is_gear:
                    break
    result = 0
    for nums in gears.values():
        if len(nums) == 2:
            result += nums[0] * nums[1]
    return gears, result
```

Стало - три функции, сложностью 5, 4 и 4 соответственно

```python
def find_numbers(row):
    start_end_numbers = []
    i = 0
    while i < len(row):
        if not row[i].isdigit():
            i += 1
            continue
        start_number = i
        while i < len(row) and row[i].isdigit():
            i += 1
        start_end_numbers.append((start_number, i))
    return start_end_numbers


def check_gears(schema, j, first_ch, last_ch):
    start_row = max(j - 1, 0)
    end_row = j + 1
    start_ch = max(first_ch - 1, 0)
    end_ch = last_ch + 1
    for delta_row, check_row in enumerate(schema[start_row : end_row + 1]):
        for delta_ch, ch in enumerate(check_row[start_ch:end_ch]):
            if ch == "*":
                return (start_row + delta_row, start_ch + delta_ch)


def count_gear_ratio(text_schema):
    schema = text_schema.split("\n")
    gears = dict()
    for j, row in enumerate(schema):
        for first_ch, last_ch in find_numbers(row):
            xy = check_gears(schema, j, first_ch, last_ch)
            if xy in gears:
                gears[xy].append(int(row[first_ch:last_ch]))
            else:
                gears[xy] = [int(row[first_ch:last_ch])]
    return sum(
        map(lambda x: x[0] * x[1], filter(lambda x: len(x) == 2, gears.values()))
    )
```

Помимо очевидного вынесения части кода в отдельные функции, применял методы функционального программирования (map, filter - но это не панацея, попытавшись переписать find_numbers() целиком в функциональном стиле, получил сложность 20)

По итогу - очень красиво получилось в первом примере, не так очевидно в третьем, и вызвало вопросы во втором. Сама идея понятно, но не везде ясно как лучше приложить. Из очевидно полезного - поставил себе расширение radon для анализа сложности кода - теперь буду ориентироваться на него
