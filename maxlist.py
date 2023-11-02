n=int(input("Enter range: "))
l=list(map(int,input("Enter elements: ").split()))
maxx=l[0]
for i in l:
    if i>maxx:
        maxx=i
print("Greatest element = ",maxx)
