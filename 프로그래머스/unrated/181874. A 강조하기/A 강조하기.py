def solution(myString):
    answer = []
    for i in range(len(myString)):
        if myString[i] == 'a' or myString[i] == 'A':
            answer.append(myString[i].upper())
        elif myString[i] != 'a':
            answer.append(myString[i].lower())
    answer = ''.join(answer)
    # print(answer)
    return answer