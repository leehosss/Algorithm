import sys
sys.stdin = open("input.txt","r")

n = int(input())

for i in range(1,n+1):
    a = input()
    a = a.upper()
    if a == a[::-1]:
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)