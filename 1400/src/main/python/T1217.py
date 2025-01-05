

from typing import List


def minCostToMoveChips(self, position: List[int]) -> int:
    cnt = 0
    for p in position:
        if p % 2 == 0:
            cnt += 1

    return len(position) - cnt if cnt > len(position) // 2 else cnt