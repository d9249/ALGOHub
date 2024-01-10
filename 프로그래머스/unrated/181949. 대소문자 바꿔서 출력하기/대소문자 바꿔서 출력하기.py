str = input()
str = list(str)
for i in range(len(str)):
    if str[i].isupper() == True:
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()
str = ''.join(str)
print(str)
