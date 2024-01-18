def solution(price):
    if 10 <= price < 100000:
        price = price
    elif price >= 100000 and price < 300000:
        price = price*0.95
    elif price < 500000 and price >= 300000:
        price = price*0.9
    elif price >= 500000:
        price = price*0.8
    return int(price)