def solution(my_string, letter):
    tmp = []
    for i in my_string:
        if i != letter:
            tmp.append(i)
    tmp = ''.join(tmp)
    return tmp