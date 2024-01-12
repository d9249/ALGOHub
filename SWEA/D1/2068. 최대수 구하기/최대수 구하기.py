T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split(' ')))
    print("#"+str(test_case), max(a))