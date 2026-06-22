import sys
sys.stdin = open("input.txt","r")
from collections import deque


def DFS(l, sum):
    global max
    if sum>c:
        return
    if l == n:
        if sum> max and sum <= c:
            max = sum
        return 
    else:
        DFS(l+1, sum+a[l])
        DFS(l+1, sum)


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = []
    max = 0
    a = [int(input()) for _ in range(n)]
    DFS(0, 0)
    print(max)
    
    