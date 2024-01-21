a = int(input())
arr = list(map(int, input().split()))
c = int(input())
count = 0
for i in range(a):
    if c == arr[i]:
        count+=1
print(count)