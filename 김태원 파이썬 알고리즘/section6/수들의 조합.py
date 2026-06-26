import sys
sys.stdin=open("input.txt", "rt")
def DFS(l,s):
    global cnt
    if  l == k:
        if sum(res)%m == 0:
            cnt+=1
        
    else:
        for i in range(s,n):
            res[l] = a[i]
            DFS(l+1,i+1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    ch = [0]*n
    res = [0]*k
    DFS(0,0)    
    print(cnt)