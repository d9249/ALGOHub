def solution(num_list):
    num = 1
    if len(num_list) > 10:
        answer = sum(num_list)
    else:
        for i in range(len(num_list)):
            num = num * num_list[i]
            answer = num
    return answer