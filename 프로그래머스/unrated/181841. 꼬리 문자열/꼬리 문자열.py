def solution(str_list, ex):
    tmp = []
    for i in range(len(str_list)):
        if ex not in str_list[i]:
            tmp.append(str_list[i])
    tmp = ''.join(tmp)
    return tmp