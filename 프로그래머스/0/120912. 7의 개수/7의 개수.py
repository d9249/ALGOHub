def solution(array):
    answer = ''.join(str(s) for s in array)
    tmp = 0
    for i in range(len(answer)):
        if '7' in answer[i]:
            tmp+=1
    return tmp