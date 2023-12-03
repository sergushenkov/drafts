class BSTNode:
    def __init__(self, key, val, parent=None):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если надо добавить новый узел левым потомком


class BST:
    def __init__(self, node=None):
        self.Root = node  # корень дерева или None

    def FindNodeByKey(self, key):
        found = BSTFind()
        next_node = self.Root
        found.Node = next_node
        while next_node is not None and next_node.NodeKey != key:
            if key < next_node.NodeKey:
                next_node = next_node.LeftChild
                found.ToLeft = True
            else:
                next_node = next_node.RightChild
                found.ToLeft = False
            if next_node is not None:
                found.Node = next_node
        if next_node is None:
            return found
        found.NodeHasKey = True
        return found

    def AddKeyValue(self, key, val):
        found = self.FindNodeByKey(key)
        if found.NodeHasKey is True:
            return False
        new_node = BSTNode(key, val, found.Node)
        if found.Node is None:
            self.Root = new_node
            return True
        if found.ToLeft:
            found.Node.LeftChild = new_node
        else:
            found.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if self.Root is None or FromNode is None:
            return None
        found_node = FromNode
        if FindMax:
            next_node = FromNode.RightChild
        else:
            next_node = FromNode.LeftChild
        while next_node is not None:
            found_node = next_node
            if FindMax:
                next_node = next_node.RightChild
            else:
                next_node = next_node.LeftChild
        return found_node

    def DeleteNodeByKey(self, key):  # complexity = 15
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

    def Count(self):
        if self.Root is None:
            return 0
        node_count = 1
        nodes = [self.Root.LeftChild, self.Root.RightChild]
        while nodes:
            node = nodes.pop()
            if node is None:
                continue
            node_count += 1
            nodes.extend([node.LeftChild, node.RightChild])
        return node_count

    def WideAllNodes(self):
        if self.Root is None:
            return ()
        all_nodes = [self.Root]
        node_index = 0
        while node_index < len(all_nodes):
            current_node = all_nodes[node_index]
            if current_node.LeftChild is not None:
                all_nodes.append(current_node.LeftChild)
            if current_node.RightChild is not None:
                all_nodes.append(current_node.RightChild)
            node_index += 1
        return tuple(all_nodes)

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
        order_keys = {
            0: (0, 1, 2),  # in-order
            1: (1, 0, 2),  # post-order
            2: (0, 2, 1),
        }  # pre-order
        nodes = [node.RightChild, node, node.LeftChild]
        custom_order = ListWithoutNone()
        for i in order_keys[order]:
            custom_order.append(nodes[i])
        return custom_order


class ListWithoutNone(list):
    def __init__(self, iterable=(None,)):
        super().__init__(filter(lambda x: x is not None, iterable))

    def append(self, item):
        super().extend(filter(lambda x: x is not None, [item]))
