def solution(angle):
    answer = 0
    if angle > 0 and angle < 90:
        return 1
    if angle > 90 and angle < 180:
        return 3
    if angle == 90:
        return 2
    if angle%180 == 0:
        return 4
    return answer