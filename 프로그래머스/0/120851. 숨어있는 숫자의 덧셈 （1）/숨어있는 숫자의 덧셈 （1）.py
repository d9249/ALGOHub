def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        if my_string[i].isdigit() == True:
            answer.append(my_string[i])
    answer = list(map(int, answer))
    return sum(answer)