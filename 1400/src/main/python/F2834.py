
def minimumPossibleSum(self, n: int, target: int) -> int:
    # 数学题转不过来
    mod = 10**9 + 7
    m = target // 2
    if n <= m:
        return ((1 + n) * n // 2) % mod
    return ((1+ m) * m //2 + (target * 2 + (n - m) - 1) * (n - m) // 2) % mod