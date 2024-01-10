def solution(my_string, alp):
    for i in range(len(my_string)):
        my_string = list(my_string)
        if my_string[i] == alp:
            my_string[i] = ''.join(alp.upper())
    my_string = ''.join(my_string)
    return my_string