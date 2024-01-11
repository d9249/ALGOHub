def solution(numLog):
    answer = []
    for i in range(1, len(numLog), 1):
        tmp = numLog[i] - numLog[i-1]
        if tmp == 1:
            answer.append('w')
        elif tmp == -1:
            answer.append('s')
        elif tmp == 10:
            answer.append('d')
        elif tmp == -10:
            answer.append('a')
    answer = ''.join(answer)
    return answer