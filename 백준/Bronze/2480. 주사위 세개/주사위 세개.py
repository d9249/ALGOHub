a, b, c = list(map(int, input().split(' ')))
if a == b == c:
    print(10000+a*1000)
elif (a == b and a != c) or (a == c and a != b):
    print(1000+a*100)
elif (b == c and b != a):
    print(1000+b*100)
else:
    print(max(a,b,c)*100)