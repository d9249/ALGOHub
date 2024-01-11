def solution(arr, intervals):
    answer = []
    for i in range(len(intervals)):
        answer.append(arr[intervals[i][0]:intervals[i][1]+1])
    answer = sum(answer, [])
    return answer