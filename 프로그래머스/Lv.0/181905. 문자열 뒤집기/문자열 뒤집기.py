def solution(my_string, s, e):
    answer = list(my_string[s:e+1])
    answer.reverse()
    answer = ''.join(answer)
    # print(answer)
    string = my_string[:s] + answer
    emp = my_string[len(string):]
    # print(emp)
    return string+emp