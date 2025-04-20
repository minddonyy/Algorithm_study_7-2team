import sys
sys.stdin = open('input.txt', 'r')

K = int(input()) # 1m^2 에 자라는참외의 개수

x = []
y = []
sides = []
# 큰 사각형에서 작은 사각형 뺄거임
# 가장 넓은 가로랑 가장 넓은 세로 찾으세용
for _ in range(6):
    d, l = map(int, input().split()) # 방향,길이
    sides.append((d, l))
    if d == 1 or d == 2:
        x.append(l)
    elif d == 3 or d == 4:
        y.append(l)

max_x = max(x)
max_y = max(y)


for i in range(6):
    if sides[i][1] == max_x and (sides[i][0] == 1 or sides[i][0] == 2):
        max_x_idx = i
    if sides[i][1] == max_y and (sides[i][0] == 3 or sides[i][0] == 4):
        max_y_idx = i

small_x = sides[(max_y_idx + 3) % 6][1]
small_y = sides[(max_x_idx + 3) % 6][1]

area = (max_x * max_y) - (small_x * small_y)
print(area * K)
