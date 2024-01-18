def solution(order):
    answer = 0
    order = list(map(int, str(order)))
    for i in order:
        if i%3==0 and i!=0:
            answer+=1
    return answer