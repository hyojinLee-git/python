import math

progress = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progress,speeds):
    days = []
    for i in range(len(progress)):
        days.append(math.ceil((100 - progress[i]) / speeds[i]))

    #print(days)
    answer=[]
    while len(days)>0:
        cnt=1
        a=days.pop(0)
        days1=days.copy()
        for i in range(len(days)):
            if a>=days[i]:
                cnt+=1
                days1.pop(0)
            else:
                break
        answer.append(cnt)
        days=days1.copy()
    return answer