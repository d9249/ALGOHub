def solution(code):
    answer = ''
    mode = 0    
    for i in range(len(code)):
        if mode == 0 and i%2 == 0 and code[i] != '1':
            answer += code[i]
        elif mode == 1 and i%2 == 1 and code[i] != '1':
            answer += code[i]
        elif code[i] == '1':
            mode = not mode
    if answer == '':
        answer = "EMPTY"
    return answer