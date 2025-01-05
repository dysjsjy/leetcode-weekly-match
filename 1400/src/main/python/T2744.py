

from typing import List


def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == reverse(words[j]):
                count += 1
    return count

def maximumNumberOfStringPairs2(self, words: List[str]) -> int:
    words_set = set(words)

    res = 0

    for c in words_set:
        if c == c[::-1]:
            continue
        if c[::-1] in words_set:
            res += 1
    
    return res//2