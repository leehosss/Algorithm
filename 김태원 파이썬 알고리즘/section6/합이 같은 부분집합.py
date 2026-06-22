import sys
sys.stdin = open("input.txt","r")
from collections import deque


def DFS(l, sum):
    if sum >total//2:
        return
    if l == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(l+1, sum+a[l])
        DFS(l+1, sum)



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
    
    