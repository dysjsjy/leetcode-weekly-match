

def numberOfSpecialChars(self, word: str) -> int:
    ans = 0
    state = [0] * 27
    for c in map(ord, word):
        x = c & 31
        if c & 32:
            if state[x] == 0:
                state[x] = 1
            elif state[x] == 2:
                state[x] = -1
                ans -= 1
        else:
            if state[x] == 0:
                state[x] = -1
            elif state[x] == 1:
                state[x] = 2
                ans += 1
    return ans