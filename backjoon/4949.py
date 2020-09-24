
def solution(string):
    stack = []
    for i in range(len(string)):

        if string[i] == '(':
            stack.append('(')

        elif string[i] == ')':
            if stack==[]:
                return 'no'
            elif stack[-1]=='(':
                stack.pop()
            else:
                return 'no'
        elif string[i]=='[':
            stack.append('[')

        elif string[i]==']':
            if stack==[]:
                return 'no'
            elif stack[-1]=='[':
                stack.pop()
            else:
                return 'no'
            # print('No')
        else:
            pass

    if stack == []:
        return 'yes'
        # print('Yes')
    else:
        return 'no'
        # print('No')

# print(stack)


while True:
    string = input()
    if string=='.':
        break
    if string[-1]=='.':
        print(solution(string))
