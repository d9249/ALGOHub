def solution(arr):
    if len(arr) > len(arr[0]):
        a = len(arr) - len(arr[0])
        for i in range(len(arr)):
            for j in range(a):
                arr[i].append(0)
        print(arr)
        return arr
    elif len(arr) < len(arr[0]):
        b = len(arr[0]) - len(arr)
        for i in range(b):
            arr.append([0 for _ in range(len(arr[0]))])
        return arr
    else:
        return arr