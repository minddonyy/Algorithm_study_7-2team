import sys
sys.stdin = open("input.txt", "r")
#############################################

## 시간복잡도 : 2598ms
## 공간복잡도 : 92032kb

def inspections(choose, val):
    global arr, min_val, width, length, gijun
    new = [i[:] for i in arr]
    for i in range(width):
        if choose[i] == 0:
            new[i] = [0] * length
        elif choose[i] == 1:
            new[i] = [1] * length
    for j in range(length):
        cnt = 0
        before = new[0][j]
        for i in range(width):
            if before == new[i][j]:
                cnt += 1
            else:
                cnt = 1
            before = new[i][j]
            if cnt >= gijun:
                break
        else:
            return
    min_val = val


def dfs(idx, cnt, choose):
    global min_val, gijun, width
    if cnt >= min_val:
        return
    if idx == width:
        inspections(choose, cnt)
        return
    choose.append(2)
    dfs(idx + 1, cnt, choose)
    choose.pop()
    choose.append(0)
    dfs(idx + 1, cnt + 1, choose)
    choose.pop()
    choose.append(1)
    dfs(idx + 1, cnt + 1, choose)
    choose.pop()



T = int(input())
for tc in range(1, T + 1):
    width, length, gijun = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(width)]
    min_val = 99999
    dfs(0, 0, [])
    print(f'#{tc} {min_val}')