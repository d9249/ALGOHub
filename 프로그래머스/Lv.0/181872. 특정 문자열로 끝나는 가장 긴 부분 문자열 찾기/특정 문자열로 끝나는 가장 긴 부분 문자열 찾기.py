def solution(myString, pat):
    answer = ''
    tmp = 0
    if pat in myString:
        for i in range(len(myString)):
            if pat[-1] == myString[i]:
                tmp = i
    answer = myString[:tmp+1]
    return answer