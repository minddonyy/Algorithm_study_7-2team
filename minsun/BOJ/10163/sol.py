import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
length = 1001
white = [[0] * length for _ in range(length)]
for z in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x1+x2):
        for j in range(y1, y1+y2):
            white[i][j] = z


for n in range(1, N+1):
    cnt = 0
    for w in white:
        for y in w:
            if y == n:
                cnt += 1

    print(cnt)
