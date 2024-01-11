def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer.append(1)
            elif arr[i][j] != arr[j][i]:
                answer.append(0)
    if 0 in answer:
        answer = 0
    else:
        answer = 1
    return answer