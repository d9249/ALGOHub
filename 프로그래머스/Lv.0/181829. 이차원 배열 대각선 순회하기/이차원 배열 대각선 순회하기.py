def solution(board, k):
    answer = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i + j) <= k:
                answer.append(board[i][j])
    answer = sum(answer)
    return answer