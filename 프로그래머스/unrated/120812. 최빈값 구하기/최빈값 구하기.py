def solution(array):
    answer = 0
    set_array = set(array)
    max_count = 0
    for i in set_array:
        count = array.count(i)
        if max_count < count:
            max_count = count
            answer = i
        elif max_count == count:
            answer = -1
    return answer