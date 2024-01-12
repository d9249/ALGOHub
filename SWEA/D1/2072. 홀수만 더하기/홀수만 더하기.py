t = int(input())
for test_case in range(1,t+1):
    i = map(int, input().split())
    answer = 0
    for j in i:
        if j%2 != 0:
            answer += j
    print("#"+str(test_case),str(answer))