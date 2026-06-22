import sys
sys.stdin = open("input.txt","r")
from collections import deque


def DFS(l):
    global cnt
    if l == m:
        for i in range(m):
            print(res[i], end = " ")
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[l] = i
            DFS(l+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)
