def solution(a, d, included):
    answer, tmp = [], []
    for i in range(len(included)):
        answer.append(a)
        a += d
    answer = answer[:len(included)]
    for i in range(len(included)):
        if included[i] == True:
            tmp.append(answer[i])
    answer = sum(tmp)
    return answer