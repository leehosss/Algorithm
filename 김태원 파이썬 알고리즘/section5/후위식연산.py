import sys
sys.stdin = open("input.txt","r")
from collections import deque

a = input()
x = []

for i in a:
    if i.isdecimal():
        x.append(int(i))
    else:
        if i =="+":
            a1 = x.pop()
            a2 = x.pop()
            x.append(a1+a2)
        elif i == "-":
            a1 = x.pop()
            a2 = x.pop()
            x.append(a2-a1)
        elif i =="*":
            a1 = x.pop()
            a2 = x.pop()
            x.append(a1*a2)
        elif i == "/":
            a1 = x.pop()
            a2 = x.pop()
            x.append(a2/a1)
print(x[0])