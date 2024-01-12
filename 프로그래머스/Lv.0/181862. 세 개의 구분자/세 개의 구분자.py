def solution(myStr):
    answer = []
    answer = myStr.split('a')
    answer = ' '.join(answer).split('b')
    answer = ' '.join(answer).split('c')
    answer = ' '.join(answer).split(' ')
    answer = ' '.join(answer).split()
    if not answer:
        answer.append('EMPTY')
    return answer