n=int(input("Enter the range: "))
l=list(map(int,input("Enter elements: ").split()))
minn=l[0]
for i in l:
    if i<minn:
        minn=i
print("Minimum element = ",minn)
