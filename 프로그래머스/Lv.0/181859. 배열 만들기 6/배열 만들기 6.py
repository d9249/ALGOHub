def solution(arr):
    answer = []
    i=0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
            i+=1
        elif answer != [] and answer[-1] == arr[i]:
            answer = answer[:-1]
            i+=1
        elif answer != [] and answer[-1] != arr[i]:
            answer.append(arr[i])
            i+=1
    if answer == []:
        answer.append(-1)
    return answer