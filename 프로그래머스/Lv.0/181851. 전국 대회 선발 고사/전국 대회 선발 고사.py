def solution(rank, attendance):
    answer = 0
    tmp, tmp2 = [], []
    for i, idx in enumerate(attendance):
        if idx == True:
            tmp.append(rank[i])
    tmp.sort()
    for i in range(len(tmp)):
        tmp2.append(rank.index(tmp[i]))
    answer = tmp2[0]*10000 + tmp2[1]*100 + tmp2[2]
    return answer