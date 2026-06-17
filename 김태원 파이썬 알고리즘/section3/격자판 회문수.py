import sys
sys.stdin = open("input.txt","r")


a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for k in range(7):
        tmp = a[k][i:i+5]
        if tmp == tmp[::-1]:
            cnt+=1
        for j in range(2):
            if a[i+j][k] != a[i+5-j-1][k]:
                break
        else:
            cnt+=1

print(cnt)