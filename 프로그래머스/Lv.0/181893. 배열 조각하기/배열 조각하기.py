def solution(arr, query):
    answer = arr
    for i, query in enumerate(query):
        print(i, query)
        if i%2 == 0:
            answer = answer[:query+1]
        else:
            answer = answer[query:]
    return answer