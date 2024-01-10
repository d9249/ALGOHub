def solution(rny_string):
    rny_string = list(rny_string)
    for i in range(len(rny_string)):
        if rny_string[i] == 'm':
            rny_string[i] = ''.join('rn')
    rny_string = ''.join(rny_string)
    return rny_string