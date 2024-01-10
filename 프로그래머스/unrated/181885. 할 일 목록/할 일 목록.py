def solution(todo_list, finished):
    arr = []
    for i in range(len(finished)):
        if finished[i] == False:
            arr.append(todo_list[i])
    return arr