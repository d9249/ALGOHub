def solution(my_string, num1, num2):
    answer = list(my_string)
    tmp1 = answer[num1]
    tmp2 = answer[num2]
    answer[num1] = tmp2
    answer[num2] = tmp1
    answer = ''.join(answer)
    return answer