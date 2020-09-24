rise,fall,distance=map(int,input().split())
answer=(distance-rise)//(rise-fall)
if (distance-rise)%(rise-fall)==0:
  print(answer+1)
else:
  print(answer+2)