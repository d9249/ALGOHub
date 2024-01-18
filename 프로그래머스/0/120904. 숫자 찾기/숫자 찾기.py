def solution(num, k):
    answer = list(str(num))
    tmp = -1
    for i in answer:
        if str(k) in i:
            tmp = answer.index(i)+1
    return tmp