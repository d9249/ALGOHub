def solution(order):
    answer = 0
    for i, idx in enumerate(order):
        print(i, idx)
        if ('american' or 'anything' in order[i]) and ('cafelatte' not in order[i]):
            answer += 4500
        elif 'cafelatte' in order[i]:
            answer += 5000
    return answer