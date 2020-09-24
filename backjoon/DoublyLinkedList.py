class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,data):
        self.head=Node(data)

    def push(self,data):
        node=self.head
        while node is not None:
            node=node.next
            node.prev=node
        node.next=Node(data)

d=DoublyLinkedList(1)
d.push(2)