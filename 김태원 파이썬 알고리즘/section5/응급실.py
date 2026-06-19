import sys
sys.stdin = open("input.txt","r")
from collections import deque

n, m = map(int, input().split())

a = [(idx, col) for idx, col in enumerate(list(map(int, input().split()))) ]
a = deque(a)
cnt= 0
while True:
    cur = a.popleft()

    if any(cur[1] < i[1] for i in a):
        a.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break
            