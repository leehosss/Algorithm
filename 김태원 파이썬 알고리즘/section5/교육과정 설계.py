import sys
sys.stdin = open("input.txt","r")
from collections import deque

s =input()
n = int(input())
for i in range(n):
    b = input()
    a = deque(s)
    for x in b:
        if x in a:
            if x != a.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(a) ==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))


