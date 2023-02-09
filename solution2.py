#!/usr/bin/env python3

def maxA(N):
    """
    For each i, we try every possible value of j (where j < i), and see which value of j gives us the maximum value of dp[j]
    * (i - j - 1)

    :param N: the number of keystrokes we have
    :return: The maximum number of A's that can be printed using N keystrokes.
    """
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(2, i - 2):
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
    return dp[N]
