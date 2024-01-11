def solution(binomial):
    answer = binomial.split(' ')
    if answer[1] == "+":
        answer = int(answer[0])+int(answer[2])
    elif answer[1] == "-":
        answer = int(answer[0])-int(answer[2])
    elif answer[1] == "*":
        answer = int(answer[0])*int(answer[2])
    return answer