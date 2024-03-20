import string
import math

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    x, y = divmod(num, base)
    if x == 0 :
        return tmp[y] 
    else :
        return convert(x, base) + tmp[y]

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True
    
def solution(n, k):
    answer = 0
    tmp = convert(n, k)
    tmp2 = tmp.split('0')
    tmp2 = list(filter(None, tmp2))
    for i in range(len(tmp2)):
        if primenumber(int(tmp2[i])) == True and tmp2[i] != '1':
            answer += 1
    return answer