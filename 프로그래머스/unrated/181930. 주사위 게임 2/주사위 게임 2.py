def solution(a, b, c):
    answer = 0
    if a == b == c:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a != b == c:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif a == b != c:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif a == c != b:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif a != b != c:
        answer = (a+b+c)
    return answer