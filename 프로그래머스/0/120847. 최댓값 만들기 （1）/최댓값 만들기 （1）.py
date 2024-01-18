def solution(numbers):
    a = max(numbers)
    answer = numbers.index(max(numbers))
    del numbers[answer]
    b = max(numbers)
    return a*b