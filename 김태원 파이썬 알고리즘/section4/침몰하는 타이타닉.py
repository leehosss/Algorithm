import sys
from collections import deque
sys.stdin = open("input.txt","r")


n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse = True)
a = deque(a) 
cnt = 0
while a:
    if len(a) == 1:
        cnt+=1
        break
    if a[0]+a[-1] > m:
        a.popleft()
        cnt+=1
    else:
        a.popleft()
        a.pop()
        cnt+=1
print(cnt)
