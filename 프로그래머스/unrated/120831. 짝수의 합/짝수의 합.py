def solution(n):
    answer = 0
    num = [i for i in range(2, n+1, 2)]
    print(num)
    answer = sum(num)
    return answer