def solution(arr, queries):
    answer =[]
    for a in queries :
        b = arr[a[0]:a[1]+1]
        b.sort()
        for i in b :
            if i > a[2] :
                answer.append(i)
                break
            elif i == b[-1] :
                answer.append(-1)
    return answer