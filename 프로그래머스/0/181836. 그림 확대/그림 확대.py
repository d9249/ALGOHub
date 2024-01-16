def solution(picture, k):
    answer = []
    answer2 = []
    tmp = []

    for i in range(len(picture)):
        for j in range(len(picture[i])):
            for n in range(k):
                tmp = picture[i][j]
                answer.append(tmp)
        for p in range(k):
            answer2.append(''.join(answer))
        tmp = []
        answer = []
    return answer2