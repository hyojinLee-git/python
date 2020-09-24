class Queue():

    def __init__(self):
        self.list=[]
        self.len=0
        self.front=0
        self.back=0


    def push(self,data):
        self.list.append(data)
        self.len+=1
        self.back+=1


    def isEmpty(self):
        if self.back-self.front==0:
            self.list=[]
            self.front=0
            self.back=0
            return 1
        return 0

    def erase(self):
        if self.isEmpty():
            return -1
        result=self.list[self.front]
        #self.len-=1
        self.front+=1
        return result


    def head(self):
        if self.isEmpty()==1:
            return -1
        return self.list[0]

    def tail(self):
        if self.isEmpty()==1:
            return -1
        return self.list[self.back-1]

    def size(self):
        if self.isEmpty()==1:
            return 0
        return self.back-self.front

num=int(input())
q=Queue()




while num>0:
    num-=1
    input_split=input().split()
    op=input_split[0]

    if op=='push':
        q.push(int(input_split[1]))
    elif op=='front':
        print(q.head())
    elif op=='back':
        print(q.tail())
    elif op=='empty':
        print(q.isEmpty())
    elif op=='size':
        print(q.size())
    elif op=='pop':
        print(q.erase())
    else:
        print('unacceptable op')



