def solution(s):
    answer = ''
    for i in s:
        a_count = s.count(i)
        if a_count == 1:
            answer += i
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer