def solution(arr):
    answer = arr
    tmp = []
    for i in range(len(arr)):
        if len(arr) <= 2**i:
            tmp.append(i)
    if len(arr) < 2**tmp[0]:
        num = 2**tmp[0] - len(arr)
        for j in range(num):
            answer.append(0)
    return answer