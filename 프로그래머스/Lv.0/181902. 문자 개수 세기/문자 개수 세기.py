def solution(my_string):
    answer = [0 for i in range(52)]
    tmp = []
    for i in range(len(my_string)):
        tmp.append(my_string[i])
    for i in range(len(tmp)):
        if ord(tmp[i]) >= 97:
            tmp[i] = ord(tmp[i])-71
        else:
            tmp[i] = ord(tmp[i])-65
    tmp.sort()
    for i, idx in enumerate(tmp):
        answer[idx] += 1
    return answer