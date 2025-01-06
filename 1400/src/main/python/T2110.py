

from typing import List


def getDescentPeriods(self, prices: List[int]) -> int:
    pre = None
    cnt = 1
    sum = 0
    for p in prices:
        if pre is not None and (pre - p == 1):
            cnt += 1
        else:
            cnt = 1
        sum += cnt
        pre = p
    return sum