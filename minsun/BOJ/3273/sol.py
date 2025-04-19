import sys
sys.stdin = open('input.txt')


N = int(input())
arr = list(map(int, input().split()))
sum_value = int(input())
arr.sort()
start = 0
end = N - 1
cnt = 0

while start < end:
    current_sum = arr[start] + arr[end]
    if current_sum == sum_value:
        cnt += 1
        start += 1
        end -= 1
    elif current_sum < sum_value:
        start += 1
    else:
        end -= 1

print(cnt)