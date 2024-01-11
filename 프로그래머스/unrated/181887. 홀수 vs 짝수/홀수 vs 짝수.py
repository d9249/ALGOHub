def solution(num_list):
    tmp1, tmp2 = 0, 0
    for i in range(0, len(num_list), 2):
        tmp1 += num_list[i]
    for i in range(1, len(num_list), 2):
        tmp2 += num_list[i]
    if tmp1 < tmp2:
        return tmp2
    else:
        return tmp1