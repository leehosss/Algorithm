import sys
sys.stdin = open("input.txt","r")



k, n = map(int, input().split())
a = [int(input()) for _ in range(k)]


def count(x):
    ct = 0
    for i in a:
        ct += (i//x)

    return ct

lt =1
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >=n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)



        
    