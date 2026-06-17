import sys
sys.stdin = open("input.txt","r")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum+= x%10
        x = x//10
    return sum
mx = -2147000000
res = 0
for i in range(n):
    if digit_sum(a[i]) > mx:
        mx = digit_sum(a[i])
        res = a[i]
print(res)


    
