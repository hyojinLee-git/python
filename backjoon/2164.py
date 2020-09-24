class Queue():

    def __init__(self):
        self.list=[]
        self.len=0
        self.front=0
        self.back=0


    def push(self,data):
        self.len+=1
        self.back+=1
        return self.list.append(data)


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
        self.list[self.front]=0
        #self.len-=1
        self.front+=1
        #return self.front

    def head(self):
        if self.isEmpty():
            return -1
        return self.list[self.front]

    def seeQueue(self):
        return self.list

    def goBack(self):
        temp=self.list[self.front]
        self.list[self.front]=0
        self.push(temp)
        self.front+=1

num=int(input())
card=Queue()

for i in range(num):
    card.push(i+1)

count=0
if card.seeQueue()==[1]:
    print(1)
elif card.seeQueue()==[1,2]:
    print(2)
elif card.seeQueue()==[1,2,3]:
    print(2)
else:
    while True:
        card.erase()
        count+=1
        #num-=1
        #print(num)
        card.goBack()
        count+=1
        #num-=1
        #ㅠㅠ

    print(card.seeQueue())
    print(card.head())
    print(card.seeQueue()[-1])

