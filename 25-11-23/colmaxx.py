n=int(input())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(0,n):
    maxx=mat[i][0]
    for j in range(0,n):
        if mat[j][i]>maxx:
            maxx=mat[i][j]
    print(maxx,end=' ')
