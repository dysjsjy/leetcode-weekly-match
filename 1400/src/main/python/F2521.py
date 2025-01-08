

from typing import List


def distinctPrimeFactors(self, nums: List[int]) -> int:
    # 做不出来，看不懂
    s = set()
    for x in nums:
        i = 2
        while i * i <= x:
            if x % i == 0:
                s.add(i)
                x //= i
                while x %i == 0:
                    x //= i
            i += 1
        if x > 1:
            s.add(x)

    return len(s)