def solution(num_list):
    num1, num2 = 1, 1
    for i in range(len(num_list)):
        num1 = num1*num_list[i]
        num2 = sum(num_list)**2
        
    if num1 > num2:
        return 0
    else:
        return 1