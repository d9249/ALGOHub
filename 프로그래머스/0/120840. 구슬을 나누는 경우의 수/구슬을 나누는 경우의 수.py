import math
from fractions import Fraction
def solution(balls, share):
    answer = (math.factorial(balls))
    answer2 = (math.factorial(balls-share))*math.factorial(share)
    fraction1 = int(Fraction(answer, answer2))
    return fraction1