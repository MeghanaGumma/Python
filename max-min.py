n=int(input("Enter the range: "))
l=[]
i=1
while i<n:
    m=int(input("Enter element: "))
    l.append(m)
    i=i+1
print("Difference = ",max(l)-min(l))
