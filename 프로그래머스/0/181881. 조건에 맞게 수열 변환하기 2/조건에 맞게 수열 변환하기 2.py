def solution(arr):
    answer = 0
    tmp = []
    while tmp != arr:
        tmp = arr.copy()
        for j in range(len(arr)):
            if arr[j] >= 50 and arr[j]%2 == 0:
                arr[j] /= 2
            elif arr[j] < 50 and arr[j]%2 == 1:
                arr[j] = (arr[j]*2)+1
        answer += 1
    return answer-1