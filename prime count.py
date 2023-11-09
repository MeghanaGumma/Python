def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
t=int(input("Enter range: "))
count=0
for i in range(1,t):
    if(prime(i)):
        count=count+1
print("Prime number count = ",count)
