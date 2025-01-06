
from typing import List


def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    n = len(arr)
    res = 0
    for j in range(1, n + 1, 2):
        for i in range(n - j + 1):
            res += sum(arr[i : i + j])
    return res