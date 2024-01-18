def solution(n):
    answer = 0
    num = 1
    while num != n:
        for i in range(1,n):
            if n%i == 0:
                answer+=1
            else:
                answer+=0
            num+=1
    return answer+1