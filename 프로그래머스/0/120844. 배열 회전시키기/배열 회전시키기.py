def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append([numbers[-1]])
        answer.append(numbers[:-1])
        tmp = sum(answer, [])
    else:
        answer.append(numbers[1:])
        answer.append([numbers[0]])
        tmp = sum(answer, [])
    return tmp