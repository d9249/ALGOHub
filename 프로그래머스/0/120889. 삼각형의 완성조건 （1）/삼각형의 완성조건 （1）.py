def solution(sides):
    c = max(sides)
    i = sides.index(c)
    del sides[i]
    if sides[0] + sides[1] <= c:
        return 2
    else:
        return 1