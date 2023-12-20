arr = [i for i in range(1, 31)]
for _ in range(28):
    x = int(input())
    arr.remove(x)
print(arr[0], arr[1])