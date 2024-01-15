def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '4' not in str(i) and  '6'not in str(i) and '7' not in str(i) and '8' not in str(i) and '9' not in str(i):
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer

# def solution(l, r):
#     answer = []
#     for i in range(1,r):
#         tmp = bin(i)
#         tmp = int(tmp[2:])
#         if l <= tmp*5 <= r and "1" not in str():
#             answer.append(int(tmp)*5)
#         else:
#             answer.append(-1)
#             break
#     return answer