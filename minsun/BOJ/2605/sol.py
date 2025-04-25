import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
students = list(map(int, input().split()))

result = []

for i in range(N):
    if i == 0:
        result.insert(0, i+1)
    else:
        result.insert(students[i], i+1)

for i in reversed(result):
    print(i, end=" ")