def solution(num_list, n):
    answer = [[0 for i in range(n)] for j in range(len(num_list)//n)]
    tmp = 0
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            answer[i][j] = num_list[tmp]
            tmp +=1
    return answer