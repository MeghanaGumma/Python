def minlist(l):
    minn=l[0]
    for i in l:
        if i<minn:
            minn=i
    return minn
n=int(input("Enter range: "))
l=list(map(int,input("Enter elements: ").split()))
fmin=minlist(l)
l.remove(fmin)
smin=minlist(l)
print(smin)
