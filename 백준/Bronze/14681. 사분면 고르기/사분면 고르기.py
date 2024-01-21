a = int(input())
b = int(input())
if a > 0 and b > 0:
    c = 1
elif a < 0 and b > 0:
    c = 2
elif a > 0 and b < 0:
    c = 4
elif a < 0 and b < 0:
    c = 3
print(c)