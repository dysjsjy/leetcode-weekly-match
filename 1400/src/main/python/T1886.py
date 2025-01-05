

from typing import List


def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
    n = len(mat)
    # 最外层表示旋转4次
    for k in range(4):
        #旋转上部份
        for i in range(n // 2):
            # 旋转每次层
            for j in range((n + 1) // 2):
                mat[i][j], mat[n - 1 - j][i], mat[n - 1 - i][n - 1 - j], mat[j][n - 1 - i] = mat[n - 1 - j][i], mat[n - 1 - i][n - 1 - j], mat[j][n - 1 - i], mat[i][j]
        if mat == target:
            return True
    return False