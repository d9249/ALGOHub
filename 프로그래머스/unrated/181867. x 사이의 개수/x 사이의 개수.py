def solution(myString):
    answer = myString.split('x')
    arr = []
    for i in range(len(answer)):
        arr.append(len(answer[i]))
    return arr