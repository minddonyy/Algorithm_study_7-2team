import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = [0] * 1001

max_idx = 0
max_h = 0
for _ in range(N):
    L, H = map(int, input().split())

    arr[L] = H

    if max_h < H:
        max_idx, max_h = L, H

    result = 0
    max_temp = 0
    for i in range(max_idx + 1):
        max_temp = max(max_temp, arr[i])
        result += max_temp

    max_temp = 0
    for i in range(1000, max_idx, -1):
        max_temp = max(max_temp, arr[i])
        result += max_temp

print(result)

