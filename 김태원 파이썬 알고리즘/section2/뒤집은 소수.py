import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10+t
        x = x//10
    return res

def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
for i in a:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp,end = " ")