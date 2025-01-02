def entityParser(self, text: str) -> str:
    entity_map = {
        "&quot;": "\"",
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/"
    }
    i, n = 0, len(text)
    ans = ""
    while i < n:
        if text[i] == '&':
            j = i + 1
            while j < n and j - i < 6 and text[j] != ';':
                j += 1
            sub = text[i:min(j + 1, n)]
            if sub in entity_map:
                ans += entity_map[sub]
                i = j + 1
                continue
        ans += text[i]
        i += 1
    return ans

# 错误写法
# def entityParser(self, text: str) -> str:
#     myDict = dict([('&quot;', '\"'), ('&apos;', '\''), ('&amp;', '&'),
#                    ('&gt;', '<'), ('&lt;', '<'), ('&frasl;', '\\')])
#     sList = list()
#     temp = str()
#
#     for i in range(len(text)):
#         if text[i] != ' ':
#             temp += text[i]
#         else:
#             sList.append(temp)
#             temp = str()
#
#         if i == len(text) - 1:
#             sList.append(temp)
#
#     aws = str()
#     for s in sList:
#         if s in myDict:
#             aws += myDict[s]
#         else:
#             aws += s
#         aws += ' '
#     return aws
