n=int(input("Enter range: "))
l=[]
i=1
while i<=n:
    m=int(input("Enter element: "))
    l.append(m)
    i=i+1
print(l)
x=int(input("Enter position: "))
v=int(input("Enter new value: "))
l[x]=v
print(l)
