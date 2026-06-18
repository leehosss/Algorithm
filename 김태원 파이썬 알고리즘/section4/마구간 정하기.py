import sys
sys.stdin = open("input.txt","r")



n, m  = map(int, input().split())


def count(x):
    cnt = 1
    ep = line[0]
    for i in range(1,n):
        if line[i] - ep >= x:
            cnt+=1
            ep = line[i]
    return cnt



line = []
for i in range(n):
    a = int(input())
    line.append(a)
line.sort()
lt = 1
rt = line[n-1]
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1 
print(res)


        
    
