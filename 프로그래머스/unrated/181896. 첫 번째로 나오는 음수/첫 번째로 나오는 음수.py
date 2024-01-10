def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
        else:
            answer = -1
    return answer