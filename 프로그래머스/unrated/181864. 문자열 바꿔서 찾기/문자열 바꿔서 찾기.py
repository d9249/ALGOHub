def solution(myString, pat):
    answer = list(myString)
    tmp = []
    for i in range(len(myString)):
        if answer[i] == 'A':
            tmp.append('B')
        elif answer[i] == 'B':
            tmp.append('A')
    tmp = ''.join(tmp)
    if pat in tmp:
        return 1
    else:
        return 0