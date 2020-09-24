from collections import deque

class Deque:

    def __init__(self):
        self.list=[]
        self.len=0
        self.head=0
        self.tail=0

    def push_front(self,data):
        self.list=deque(self.list)
        self.list.appendleft(data)
        self.list=list(self.list)
        self.len+=1
        self.tail+=1

    def push_back(self,data):
        self.list.append(data)
        self.len+=1
        self.tail+=1

    def isEmpty(self):
        if self.tail-self.head==0:
            return 1
        return 0

    def pop_front(self):
        if self.isEmpty():
            return -1
        result=self.list[self.head]
        self.list=deque(self.list)
        self.list.popleft()
        self.list=list(self.list)
        self.head+=1
        return result

    def pop_back(self):
        if self.isEmpty():
            return -1
        result=self.list[self.tail]
        self.list.pop()
        self.tail-=1
        return result

    def size(self):
        if self.isEmpty():
            return 0
        return self.tail-self.head

    def front(self):
        if self.isEmpty():
            return -1
        return self.head

    def back(self):
        if self.isEmpty():
            return -1
        return self.tail

    def seeDeque(self):
        return self.list

d=Deque()
d.push_back(1)  # [1]
d.push_front(2) # [2,1]
print(d.front())# 2
print(d.back()) # 1
print(d.size()) # 2
print(d.isEmpty())  # 0
print(d.pop_front()) # 1
print(d.pop_back()) # -1
print(d.size()) # 0
print(d.isEmpty())  # 1
print(d.pop_back()) #-1
d.push_front(3)
print(d.isEmpty())  #0
print(d.front())    #3
print(d.seeDeque())

print(d.seeDeque())

