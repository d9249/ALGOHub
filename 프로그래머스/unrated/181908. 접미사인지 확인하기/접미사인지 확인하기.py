def solution(my_string, is_suffix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    if is_suffix in answer:
        answer = 1
    else:
        answer = 0
    return answer