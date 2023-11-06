n=int(input("Enter range: "))
c=0
print('Prime Numbers = ')
for i in range(1,n+1):
    co=0
    for j in range(1,i+1):
        if(i%j==0):
            co=co+1
    if(co==2):
        print(i,end=',')
        c=c+1
print()
print('Count = ',c)
