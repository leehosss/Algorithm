import sys
sys.stdin=open("input.txt", "r")
def DFS(l, s,d):
    global res
    if d > m:
        return
    if l == n:
        res = max(res, s)
        return
    else:
        DFS(l+1, s+c[l][0],d+c[l][1])
        DFS(l+1, s,d)


           
if __name__=="__main__":
    n, m = map(int, input().split())
    c = []
    for i in range(n):
        a, b = map(int, input().split())
        c.append((a,b))
    res = 0
    DFS(0,0,0)
    print(res)
