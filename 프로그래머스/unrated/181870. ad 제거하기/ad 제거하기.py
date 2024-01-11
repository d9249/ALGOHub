def solution(strArr):
    answer = []
    print(strArr)
    for i in range(len(strArr)):
        if 'ad' not in strArr[i]:
            answer.append(strArr[i])
    return answer