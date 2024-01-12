from collections import Counter

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        answer.append(len(strArr[i]))
    count_items = Counter(answer)
    a = count_items.most_common(n=1)
    return a[0][1]