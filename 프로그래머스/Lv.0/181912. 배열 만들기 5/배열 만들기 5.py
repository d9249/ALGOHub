def solution(intStrs, k, s, l):
    answer = []
    for i, intStrs in enumerate(intStrs):
        tmp = intStrs[s:]
        tmp = tmp[:l]
        if int(tmp) > int(k):
            answer.append(int(tmp))
    return answer