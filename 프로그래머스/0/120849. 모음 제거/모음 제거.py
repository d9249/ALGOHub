def solution(my_string):
    my_string = my_string.replace('a', '', len(my_string))
    my_string = my_string.replace('e', '', len(my_string))
    my_string = my_string.replace('i', '', len(my_string))
    my_string = my_string.replace('o', '', len(my_string))
    my_string = my_string.replace('u', '', len(my_string))
    return my_string