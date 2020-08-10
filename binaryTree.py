
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if self.value is None:
            self.value = BST(value)
        else:
            self.helperInsert(self, value)

    def helperInsert(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = BST(value)
                node.left.parent = node
            else:
                self.helperInsert(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = BST(value)
                node.right.parent = node
            else:
                self.helperInsert(node.right, value)

    def contains(self, value):
        return self.helperContains(self, value)

    def helperContains(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif node.value > value:
            return self.helperContains(node.left, value)
        else:
            return self.helperContains(node.right, value)

    def find(self, value):
        return self.helperFind(self, value)

    def helperFind(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        elif node.value > value:
            return self.helperFind(node.left, value)
        else:
            return self.helperFind(node.right, value)

    def remove(self, value):
        node = self.find(value)
        if node is None:
            return KeyError
        # when node is leaf
        if node.left is None and node.right is None:
            if node.value > node.parent.value:
                node.parent.right = None
            else:
                node.parent.left = None
        # when node having only one child
        elif node.left is None:
            if node.value > node.parent.value:
                node.parent.right = node.right
                node.right.parent = node.parent
            else:
                node.parent.left = node.right
                node.right.parent = node.parent
        elif node.right is None:
            if node.value < node.parent.value:
                node.parent.left = node.left
                node.left.parent = node.parent
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
        # when node has both child
        else:
            rightChild = node.right
            toReplace = rightChild
            while toReplace.left is not None:
                toReplace = toReplace.left
            toReplace.parent = None
            temp = node.value
            node.value = toReplace.value
            toReplace.value = temp
            return self.remove(temp)
tree = BST(5)
tree.insert(1)
tree.insert(7)
tree.insert(3)
tree.insert(6)
tree.insert(8)
tree.remove(7)
print(tree.contains(7))