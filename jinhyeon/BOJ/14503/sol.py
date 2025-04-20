dxl = [-1, 0, 1, 0] # 북 동 남 서
dyl = [0, 1, 0, -1]

back = [2, 3, 0, 1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# for i in range(n):
#     for j in range(m):
#         if not arr[i][j]:
#             empty += 1
def check_4_dire(r, c, d):
    for _ in range(4):
        d = 3 if d - 1 < 0 else d-1
        x, y = r + dxl[d], c + dyl[d]
        if arr[x][y] == 0:
            r = x
            c = y
            return r, c, d
    r, c = r + dxl[back[d]], c + dyl[back[d]]
    if arr[r][c] == 1:
        return -1, -1, -1
    return r, c, d

while True:
    if not arr[r][c]:   #현재 칸 확인 후 청소
        arr[r][c] = 2
        ans += 1
    r, c, d = check_4_dire(r, c, d)
    if r < 0 and  c < 0 and d < 0:
        break
print(ans)