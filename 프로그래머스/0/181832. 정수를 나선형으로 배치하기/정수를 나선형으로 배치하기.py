def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    dr = [0, 1, 0, -1]
    dl = [1, 0, -1, 0]
    i, j, count, d = 0, 0, 1, 0
    answer[i][j] = count
    count+=1
    while n*n >= count:
        ni, nj = i+dr[d], j+dl[d]
        if 0 <= ni < n and 0 <= nj < n and answer[ni][nj] == 0:
            i, j = ni, nj
            answer[i][j] = count
            count +=1
        else:
            d = (d+1)%4
    return answer