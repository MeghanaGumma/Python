n=int(input())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(0,n):
    csum=0
    for j in range(0,n):
        csum=csum+mat[j][i]
    print(csum,end=' ')
