def perfect(n):
    temp=n
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if temp==sum:
        print("PERFECT")
    else:
        print("NOT PERFECT")
r=int(input("Enter the range: "))
for i in range(1,r+1):
    no=int(input("Enter number: "))
    perfect(no)

