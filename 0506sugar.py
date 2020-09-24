a=int(input())

five=a//5
three=(a%5)//3
print(five,three)


if (a%5)%3 !=0:
    print(-1)
else:
    print(int(five+three))