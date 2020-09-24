num = int(input())

def solution(string):
    stack = []
    for i in range(len(string)):

        if string[i] == '(':
            stack.append('(')

        elif string[i] == ')':
            if stack != []:
                stack.pop()
            else:
                return 'NO'
            # print('No')
        #else:
        #    pass

    if stack == []:
        return 'YES'
        # print('Yes')
    else:
        return 'NO'
        # print('No')

# print(stack)

while num > 0:
    num -= 1
    string = input()
    print(solution(string))
