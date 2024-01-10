def solution(num_list):
    list1 = []
    list2 = []
    answer = 0
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            list1.append(num_list[i])
        else:
            list2.append(num_list[i])
    print(list1, list2)
    list1 = ''.join(map(str, list1)) 
    list2 = ''.join(map(str, list2))
    return int(list1)+int(list2)