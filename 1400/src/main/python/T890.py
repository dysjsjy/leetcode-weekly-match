

from typing import List

def findAndReplacePattern(self, ws: List[str], pe: str) -> List[str]:
    ans = []
    
    for s in ws:
        map_s_to_p = [-1] * 26  # 字符串 s -> 模式 pe 映射
        map_p_to_s = [0] * 26   # 模式 pe -> 字符串 s 映射
        ok = True  # 标志位，判断是否匹配
        
        for i in range(len(pe)):
            c1 = ord(s[i]) - ord('a')  # s[i] 字符转换为 0-25
            c2 = ord(pe[i]) - ord('a') # pe[i] 字符转换为 0-25
            
            # 如果 c1 尚未映射，且 c2 未被映射过
            if map_s_to_p[c1] == -1 and map_p_to_s[c2] == 0:
                map_s_to_p[c1] = c2  # 建立 s[i] -> pe[i] 的映射
                map_p_to_s[c2] = 1  # 标记 pe[i] 已被映射
            # 若已存在映射且不匹配，标记不符合
            elif map_s_to_p[c1] != c2:
                ok = False
                break
        
        # 如果字符串符合映射规则，加入结果集
        if ok:
            ans.append(s)
    
    return ans
