class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class SinglyLinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def push(self, data):
        node = self.head                #node:data=1,next=None      node:data
        while node.next is not None:
            node = node.next            #node=node.next=None
        node.next = Node(data)          #node.next=2,None

    def delete(self, data):
        node = self.head
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next
            node = node.next

    def display(self):
        node = self.head
        while node.next is not None:
            print(node.data, '->', end='')
            # print(node.next)
            node = node.next
        print(node.data)

    def listNum(self):
        node=self.head
        length=0
        while node.next is not None:
            length+=1
            node=node.next
        #print(length+1)
        return length+1

    def search(self,data):
        node=self.head
        i=0
        for i in range(self.listNum()):
            node=node.next
            i += 1
            if node.data==data:
                break
        return i+1

    def insert(self,before,data):
        node=self.head
        while node.next is not None:
            node=node.next
            if node.data==before:
                new=Node(data)
                new.next=node.next
                node.next=new

n = SinglyLinkedList(1)
n.push(2)
n.push(3)
n.push(4)
n.push(5)
n.display()
print(n.listNum())
print(n.search(3))
n.insert(3,7)
n.display()
n.insert(7,5)
n.display()
n.push(6)
n.display()
