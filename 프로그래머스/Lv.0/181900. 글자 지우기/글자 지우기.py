def solution(my_string, indices):
    string = list(my_string)
    for i in sorted(indices, reverse=True):
        del string[i]
    string = ''.join(string)
    return string