def solution(myString):
    answer = ''.join(myString).split('x')
    answer = ' '.join(answer).split()
    answer.sort()
    return answer