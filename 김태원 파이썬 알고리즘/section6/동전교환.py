import sys
sys.stdin = open("input.txt","r")
from collections import deque


def DFS(l, sum):
    global res
    if l > res:
        return
    if sum >m:
        return
    if sum == m:
        if l< res:
            res = l
    else:
        for i in range(n):
            DFS(l+1,sum+a[i])



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res= 2147000000
    DFS(0,0)
    print(res)