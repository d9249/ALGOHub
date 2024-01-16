def solution(my_string, queries):
    for i in range(len(queries)):
        a = my_string[:queries[i][0]]
        b = my_string[queries[i][0]:queries[i][1]+1]
        b = reversed(b)
        b = ''.join(b)
        c = my_string[queries[i][1]+1:]
        my_string = a+b+c
    return my_string