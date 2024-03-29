"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : Four Squares
description : 다이나믹 프로그래밍
"""

import math

n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    if i == int(math.sqrt(i)) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

print(dp[n])
