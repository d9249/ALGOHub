def solution(arr, delete_list):
    tmp = []
    for i in range(len(arr)):
        for j in range(len(delete_list)):
            if delete_list[j] == arr[i]:
                tmp.append(delete_list[j])
    for i in range(len(tmp)):
        arr.remove(tmp[i])
    return arr