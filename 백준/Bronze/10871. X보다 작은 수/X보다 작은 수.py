a, b = map(int, input().split(' '))
arr = list(map(int, input().split()))
for i in range(a):
    if b > arr[i]:
        print(arr[i])