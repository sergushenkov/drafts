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
