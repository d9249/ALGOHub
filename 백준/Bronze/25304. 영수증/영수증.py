a = int(input())
b = int(input())
answer = 0
for i in range(b):
    c, d = list(map(int, input().split(' ')))
    answer += c*d
if answer ==  a:
    print('Yes')
else:
    print('No')