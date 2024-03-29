"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 콜라츠 추측
description : 수학
"""


def solution(num):
    answer = 0

    while num != 1 and answer != 500:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        answer += 1

    if answer == 500:
        return -1

    return answer
