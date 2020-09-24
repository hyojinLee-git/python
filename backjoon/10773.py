class Stack:
    def __init__(self):
        self.len=0
        self.list=[]

    def push(self,data):
        self.len+=1
        return self.list.append(data)

    def isEmpty(self):
        if self.list==[]:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            return -1
        self.list.pop()
        self.len-=1

    def top(self):
        if self.isEmpty():
            return -1
        return self.list[-1]
    def seeStack(self):
        return self.list

num=int(input())
s=Stack()

while num>0:
    num-=1
    data=int(input())

    if data==0:
        s.pop()
    else:
        s.push(data)

if s.seeStack()==[]:
    print(0)
else:
    print(sum(s.seeStack()))




