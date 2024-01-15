def solution(arr, k):
    answer =[]
    for value in arr:
        if value not in answer:
            answer.append(value)
    if len(answer) > k:
        answer = answer[:k]
    elif len(answer) == k:
        answer = answer
    elif len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer