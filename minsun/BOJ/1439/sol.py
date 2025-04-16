import sys
sys.stdin = open("input.txt", "r")

dasom = input()

cnt = 0
for i in range(len(dasom)-1):
    if dasom[i] != dasom[i+1]:
        cnt+=1

print((cnt+1)//2)
