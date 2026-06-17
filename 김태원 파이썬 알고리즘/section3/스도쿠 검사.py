import sys
sys.stdin = open("input.txt","r")

a = [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        s1 = [0]*10
        s2 = [0]*10

        for j in range(9):
            s1[a[i][j]] = 1
            s2[a[j][i]] = 1

        if sum(s1) != 9 or sum(s2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            s3 = [0]*10

            for k in range(3):
                for l in range(3):
                    s3[a[i*3+k][j*3+l]] = 1

            if sum(s3) != 9:
                return False

    return True

if check(a):
    print("YES")
else:
    print("NO")