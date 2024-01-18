def solution(my_string):
    answer = []
    for x in my_string:
        if x not in answer:
            answer.append(x)
    answer = ''.join(answer)
    return answer