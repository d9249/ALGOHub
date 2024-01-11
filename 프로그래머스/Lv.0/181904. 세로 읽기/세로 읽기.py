def solution(my_string, m, c):
    answer = list(map(str, my_string))
    tmp = []
    for i in range(c-1, len(my_string), m):
        tmp.append(answer[i])
    answer = ''.join(tmp)
    return answer