def solution(ineq, eq, n, m):
    answer = 0
    if (eq == '=' and ineq == '>'):
        if n >= m:
            answer = 1
        else:
            answer = 0
    elif (eq == '=' and ineq == '<'):
        if n <= m:
            answer = 1
        else:
            answer = 0
    elif (eq == '!' and ineq == '>'):
        if n > m:
            answer = 1
        else:
            answer = 0
    elif (eq == '!' and ineq == '<'):
        if n < m:
            answer = 1
        else:
            answer = 0
    return answer