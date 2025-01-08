

from functools import cmp_to_key
from typing import List


def kthLargestNumber(self, nums: List[str], k: int) -> str:
    def cmp(str1: str, str2: str) -> int:
        if len(str1) < len(str2):
            return 1
        elif len(str1) > len(str2):
            return -1
        else:
            if str1 < str2:
                return 1
            else:
                return -1
    nums.sort(key=cmp_to_key(cmp))
    return nums[k - 1]