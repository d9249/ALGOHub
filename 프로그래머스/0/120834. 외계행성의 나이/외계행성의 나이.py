def solution(age):
    answer = list(str(age))
    a = []
    for i in answer:
        tmp = ord(i)+49
        a.append(chr(tmp))
    a = ''.join(a)
    return a