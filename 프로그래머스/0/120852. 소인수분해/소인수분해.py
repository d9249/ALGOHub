def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n = n / d
            answer.append(d)
        else:
            d = d + 1
    answer = sorted(list(set(answer)))
    return answer