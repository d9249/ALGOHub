def solution(x1, x2, x3, x4):
    # answer = True
    x5, x6 = True, True
    if (x1 == False and x2 == False):
        x5 = False
    elif (x3 == False and x4 == False):
        x6 = False
    if x5 == True and x6 == True:
        answer = True
    else:
        answer = False
        
    return answer