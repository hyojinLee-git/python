n=int(input())
a=[]
while n>0:
  n-=1
  m=int(input())
  #print(m)
  a.append(m)
a.sort()
for i in a:
  print(i)