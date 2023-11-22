def arm(n):
    sum=0
    temp=n
    while(n!=0):
        r=n%10
        sum=sum+r*r*r
        n=n//10
    if sum==temp:
        return True
    else:
        return False
a=int(input())
l=[i for i in range(1,a+1) if arm(i)]
for i in l:
    print(i,end=' ')
