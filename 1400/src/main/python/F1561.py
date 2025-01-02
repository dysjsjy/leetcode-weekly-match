from typing import List


def maxCoins(self, piles: List[int]) -> int:
    piles.sort()
    i = len(piles) - 2
    j = 0
    sum = 0
    while i > j:
        sum += piles[i]
        i -= 2
        j += 1
    return sum


# 灵神
def maxCoins2(self, piles: List[int]) -> int:
    piles.sort()
    return sum(piles[len(piles)//3::2])