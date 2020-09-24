array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array,commands):
    temp=[]
    answer=[]
    for i in range(len(commands)):
        temp.append(array[commands[i][0]-1:commands[i][1]])
        temp[i].sort()
        answer.append(temp[i][commands[i][2]-1])
    #print(temp)
    #print(answer)
    return answer

print(solution(array,commands))