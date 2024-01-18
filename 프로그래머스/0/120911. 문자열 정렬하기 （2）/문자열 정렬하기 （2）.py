def solution(my_string):
    answer = my_string.lower()
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer