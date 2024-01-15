def solution(myString, pat):
    answer = 0
    tmp = []
    for i in range(0, len(myString), 1):
        tmp = myString[i:i+len(pat)]
        if pat == tmp:
            answer += 1
    return answer