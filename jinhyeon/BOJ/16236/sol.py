from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxl = [-1, 0, 0, 1] #상 좌 우 하
dyl = [0, -1, 1, 0] #같은 거리의 물고기라도 먼저 먹는 우선순위
s_x, s_y = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            s_x, s_y = i, j
            arr[i][j] = 0

s_size = 2
s_energy = 0
def eat_shark(visited, near_dis):
    global s_energy
    global s_size
    global s_x, s_y
    x, y = -1, -1
    flag = False
    for i in range(n):  #제일 위
        for j in range(n):  #제일 왼쪽
            if visited[i][j] == near_dis and arr[i][j] and arr[i][j] < s_size:
                x, y = i, j
                flag = True
                break
        if flag:
            break
    s_energy += 1
    if s_energy == s_size:
        s_energy = 0
        s_size += 1
    arr[x][y] = 0
    s_x, s_y = x, y


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    near_dis = float('inf')
    while q:
        x, y = q.popleft()
        if near_dis < visited[x][y]: #먹을 수 있는 상어의 최단 거리 보다 넘으면
            eat_shark(visited, near_dis)    # 확인시
            return near_dis - 1
        if arr[x][y] and arr[x][y] < s_size:    #먹을 수 있는 상어
            near_dis = visited[x][y]
        for dx, dy in zip(dxl, dyl):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n \
                and not visited[nx][ny] \
                and arr[nx][ny] <= s_size:   #방문 X, 지나가는 상어가 작거나 같을때
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    if near_dis != float('inf'):
        eat_shark(visited, near_dis)
        return near_dis - 1
    return 0
ans = 0
while True:
    cnt = bfs(s_x, s_y)
    if cnt:
        ans += cnt
    else:
        break
print(ans)