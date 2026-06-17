import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n):
    s1 = s2 = 0
    for j in range(n):
        s1 += a[i][j]
        s2 += a[j][i]
    if s1 > res:
        res = s1
    if s2 > res:
        res = s2
s1 = s2 = 0
for i in range(n):
    s1 += a[i][i]
    s2 += a[i][n-i-1]
if s1 > res:
    res = s1
if s2 > res:
    res = s2
print(res)