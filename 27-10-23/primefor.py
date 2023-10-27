n=int(input("Enter the number: "))
c=0;
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
if n==0:
    print('0 is neither prime nor composite')
elif(c==2):
    print(n,'is prime')
else:
    print(n,'is not prime')
