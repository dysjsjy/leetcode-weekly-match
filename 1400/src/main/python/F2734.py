
def smallestString(self, s: str) -> str:
    t = list(s)
    for i, c in enumerate(t):
        if c == 'a':
            continue
        for j in range(i, len(t)):
            if t[j] == 'a':
                break
            t[j] = chr(ord(t[j]) - 1)
        return ''.join(t)
    t[-1] = 'z'
    return ''.join(t)






# 我-错误，找到最长相邻不含a的序列，没有对全是a的情况做出处理
# def smallestString(self, s: str) -> str:
#     left, right = 0, 0
#     while right < len(s):
#         if s[right] == 'a':
#             left = right + 1
#             right = left
#         right += 1
#
#     for i in range(len(s) - 1):
#         if i >= left and i <= right:
#             s[i] = str (s[i] - 1)
#
#     return s