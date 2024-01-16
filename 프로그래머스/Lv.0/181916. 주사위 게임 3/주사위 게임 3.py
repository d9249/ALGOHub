def solution(a, b, c, d):
    answer = [a,b,c,d]
    if len(list(set(answer))) == 1:
        return a*1111
    elif len(list(set(answer))) == 2:
        tmp = list(set(answer))
        re = 0
        # if answer.count(tmp[0]) == answer.count(tmp[1]):
        #     return (tmp[1]+tmp[0]) * (tmp[1]-tmp[0])
        # else:
        #     return (10*tmp[1]+1)**2
        for i in range(len(tmp)):
            if answer.count(tmp[i]) == 3:
                re = i
            elif answer.count(tmp[i]) == 2:
                return (tmp[1]+tmp[0]) * (tmp[1]-tmp[0])
        if re == 0:
            return (10*tmp[re]+tmp[1])**2
        else:
            return (10*tmp[re]+tmp[0])**2
    elif len(list(set(answer))) == 3:
        tmp = list(set(answer))
        re = 0
        for i in range(len(tmp)):
            if answer.count(tmp[i]) == 2:
                re = i
        tmp.remove(tmp[re])
        return tmp[0]*tmp[1]
    else:
        return min(answer)