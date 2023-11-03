n=int(input("Enter range 1: "))
ar1=list(map(int,input("Enter list 1 elements: ").split()))
m=int(input("Enter range 2: "))
ar2=list(map(int,input("Enter list 2 elements: ").split()))
ar1.extend(ar2)
minn=ar1[0]
for i in ar1:
    if i<minn:
        minn=i
print("Minimum element = ",minn)
