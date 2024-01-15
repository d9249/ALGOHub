def solution(q, r, code):
    answer = []
    for i in range(len(code)):
        # if r != 0:
        if (i%q) == r:
            answer.append(code[i])
        # else:
            # answer.append(code[i])
    answer = ''.join(answer)
    return answer