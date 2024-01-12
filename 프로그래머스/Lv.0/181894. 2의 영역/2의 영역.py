def solution(arr):
    answer = []
    r, l = 0, 0
    for i in range(len(arr)):
        if arr[i] == 2:
            l = i
    for j in range(len(arr)):
        if arr[j] == 2:
            r = j
            break
    answer = arr[r:l+1]
    if 2 not in answer:
        answer = [-1]
    return answer