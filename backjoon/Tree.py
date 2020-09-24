"""
         (1)
         / \
       (2) (3)
      / \
   (4)  (5)

Inorder: (Left,Root,Right):4 2 5 1 3
Preorder: (Root,Left,Right):1 2 4 5 3
Postorder: (Left,Right,Root):4 5 2 3 1
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def makeNode(self, data, left, right):
        node = self.root
        node.data = data
        node.left = left
        node.right = right
        return node

    def inorder(self,node):
        node = self.root
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)


t = BinaryTree(1)
n4 = t.makeNode(4, None, None)
n5 = t.makeNode(5, None, None)
n3 = t.makeNode(3, None, None)
n2 = t.makeNode(2, n4, n5)
n1 = t.makeNode(1, n2, n3)
t.inorder(n1)
