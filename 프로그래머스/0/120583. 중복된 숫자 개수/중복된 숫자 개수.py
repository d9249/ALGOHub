def solution(array, n):
    answer = 0
    for i in range(len(array)):
        if n == array[i]:
            answer+=1
    return answer