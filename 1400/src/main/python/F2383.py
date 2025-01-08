

from typing import List


def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
    ans = 0
    for x, y in zip(energy, experience):
        if initialEnergy <= x:
            ans += x + 1 - initialEnergy
            initialEnergy = x + 1
        initialEnergy -= x
        if initialExperience <= y:
            ans += y + 1 - initialExperience
            initialExperience = y + 1
        initialExperience += y
    return ans