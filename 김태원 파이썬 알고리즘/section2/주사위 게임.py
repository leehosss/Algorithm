import sys
sys.stdin = open("input.txt","r")

n = int(input())
res = 0
for i in range(n):
    money = 0
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    if a[0] == a[1] and a[0] == a[2] and a[1] == a[2]:
        money = 10000+a[0]*1000
        if money > res:
            res = money
    elif a[0] == a[1] or a[0] == a[2]:
        money = 1000+a[0]*100
        if money > res:
            res = money
    elif a[1] == a[2]:
        money = 1000+a[0]*100
        if money > res:
            res = money
    else:
        money = a[0]*100
        if money > res:
            res = money
print(res)