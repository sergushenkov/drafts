Пример с переделкой "старого" кода под новые рекомендации найти не смог - потому что две рекомендации и так по факту всегда использовал, хотя и неосознанно, а третья требует под себя большой переделки кода, так что наглядности не получится, по факту придётся сравнивать два различных кода.

Пример из курса по алгоритмам, который прохожу сейчас на работе.

1. Рекомендация - избавляться от точек генерации исключений, запрещая соответствующее ошибочное поведение на уровне интерфейса класса - для меня звучит необычно :) 
Просто не привык использовать исключения в классе - максимум вставляя их на этапе отладки. 
После - все такие проблемы исключаю проверкой данных (правда обычно не на уровне классов - потому что чаще пишу в императивном стиле, а не ООП)

2. Рекомендация - избавляться от дефолтных конструкторов без параметров,
и передавать конструктору обязательные аргументы - тоже удивило.
Конкретно это правило для меня кажется очевидным.
Чтобы я написал какой то совсем абстрактный конструктор, который по дефолту везде ставит None, а потом требуется отдельными методами присваивать значения - это надо именно так поставить задачу, и то будет вопрос - а может сразу всё сделать?

3. Рекомендация - избегать увлечения примитивными типами данных, разрабатывать прикладную систему типов - оценил это в курсе Быстрая прокачка в ООП. Раньше не использовал - но сейчас стараюсь применять, создавая специфичные структуры со своими методами

```py
class Node:
    def __init__(self):
        """
        избавляемся от дефолтных конструкторов без параметров
        тут выглядит как будто не происходит задания атрибутов - но только потому 
        что их невозможно задать, не получив все данные класса Tree
        (в т.ч. __parent)
        """
        self.__parent = None
        self.__deep = None
        self.__child_radius = []
        self.__child = []

    def consider_child_radius(self, child_radius):
        """
        разрабатывать прикладную систему типов
        максимальный радиус дочерних деревьев данной ноды - хранится в самой ноде 
        и доступен для изменения только соответствующими методами 
        (закрыт от прямого доступа)
        """
        self.__child_radius.append(child_radius)

    def get_parent(self):
        return self.__parent

    def get_deep(self):
        return self.__deep

    def get_child(self):
        return self.__child

    def get_radius(self):
        if self.__child_radius:
            return max(self.__child_radius) + 1
        return 0

    def get_diameter(self):
        """
        избавляться от точек генерации исключений
        все случаи прописаны в коде - поэтому необходимости ловить исключения не возникает
        """
        if not self.__child_radius:
            return 1
        first_child_max_radius = max(self.__child_radius)
        first_max_radius = first_child_max_radius + 1
        self.__child_radius.remove(first_child_max_radius)
        second_max_radius = max(self.__child_radius) + 1 if self.__child_radius else 0
        self.__child_radius.append(first_child_max_radius)
        return first_max_radius + second_max_radius

    def set_deep(self, deep):
        self.__deep = deep

    def add_child(self, child):
        self.__child.append(child)

    def set_parent(self, parent):
        if self.__parent is None:
            self.__parent = parent


class Tree:
    max_deep = 0
    def __init__(self, nodes_parents=None):
        """
        избавляемся от дефолтных конструкторов без параметров
        класс Tree состоит из классов Node - в методе __init__ для каждого экземпляра класса Node присваиваются все необходимые атрибуты
        """
        root = Node()
        root.set_deep(0)
        self.__nodes = [root]
        if nodes_parents is None:
            return

        self.__nodes.extend([Node() for _ in nodes_parents])
        for i, parent_index in enumerate(nodes_parents):
            node_index = i + 1
            node = self.__nodes[node_index]
            parent = self.__nodes[parent_index]
            node.set_parent(parent)
            parent.add_child(node)

        node_index = 0
        n = len(nodes_parents) + 1
        """
        избавляться от точек генерации исключений
        вылезала ошибка на тестах, где nodes_parents даны не в порядке возрастания. 
        Обрабатываю программно такие случаи
        """
        sort_nodes = [root]
        while len(sort_nodes) < n:
            parent = sort_nodes[node_index]
            child = parent.get_child()
            if child:
                deep = parent.get_deep() + 1
                self.max_deep = max(self.max_deep, deep)
            for node in child:
                node.set_deep(deep)
                sort_nodes.append(node)
            node_index += 1

        for i in range(1, n):
            node = self.__nodes[n - i]
            parent = node.get_parent()
            radius = node.get_radius()
            parent.consider_child_radius(radius)

    def get_dimensions(self):
        root = self.__nodes[0]
        max_diameter = root.get_diameter()
        return self.max_deep, max_diameter

    def get_deeps(self):
        return [node.get_deep() for node in self.__nodes]


if __name__ == "__main__":
    _ = int(input())
    nodes_parents = [int(x) for x in input().split()]
    tree = Tree(nodes_parents)
    print(*tree.get_dimensions())
    print(*tree.get_deeps())
```