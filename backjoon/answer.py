answers = [1,2,3,4,5]

def solution(anwsers):

    student1 = [0 for i in range(len(answers))]
    num = 0
    for i in range(len(answers)):
        num += 1
        if num == 6:
            num = 1
        student1[i] = num
    #print(student1)

    student2=[]
    num = [1, 3, 4, 5]
    for i in range(len(answers)//2):
        student2.append(2)
        student2.append(num[i % 4])
    if len(answers)%2==1:
        student2.append(2)
    #print(student2)

    student3 = []
    num=[3,1,2,4,5]  # 31245 2개씩
    for i in range(len(answers)//2):
        student3.append(num[i%5])
        student3.append(num[i%5])
    if len(answers)%2==1:
        student3.append(num[i+1%5])
    #print(student3)

    correct_student1=0
    correct_student2=0
    correct_student3=0
    for i in range(len(answers)):
        if answers[i]==student1[i]:
            correct_student1+=1
        if answers[i]==student2[i]:
            correct_student2+=1
        if answers[i]==student3[i]:
            correct_student3+=1
    answer_dict={}

    answer_dict[1]=correct_student1
    answer_dict[2]=correct_student2
    answer_dict[3]=correct_student3

    answer=[]

    for key, value in answer_dict.items():
        value=int(value)
        if max(answer_dict.values())==value:
            answer.append(key)
    return answer

print(solution(answers))




