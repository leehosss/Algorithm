import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

s = []
l1 = 0
l2 = 0
while l1 <n and l2 <m:
    if a[l1] <= b[l2]:
        s.append(a[l1])
        l1+=1
    else:
        s.append(b[l2])
        l2+=1
if l1 <n:
    s = s+(a[l1:])
else:
    s = s+(b[l2:])
print(s)