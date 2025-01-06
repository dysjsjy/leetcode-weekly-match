

def alphabetBoardPath(self, target: str) -> str:
        ans = []
        x = y = 0
        for c in target:
            nx = (ord(c) - ord("a")) // 5
            ny = (ord(c) - ord("a")) % 5
            v = "UD"[nx > x] * abs(nx - x)
            h = "LR"[ny > y] * abs(ny - y)
            ans.append((v + h if c != "z" else h + v) + "!")
            x, y = nx, ny
        return "".join(ans)
