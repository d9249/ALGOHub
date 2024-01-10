def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        answer = 1
    else:
        answer = 0
    return answer