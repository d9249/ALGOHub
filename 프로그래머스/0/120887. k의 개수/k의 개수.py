def solution(i, j, k):
    answer = 0
    arr = []
    for n in range(i, j+1):
        arr.append(n)
    arr = str(arr)
    for i in range(len(arr)):
        if str(k) in arr[i]:
            answer+=1
    return answer