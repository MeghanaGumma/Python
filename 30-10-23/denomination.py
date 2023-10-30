amount=int(input("Enter the amount: "))
tt=0
fh=0
th=0
oh=0
ft=0
ty=0
tn=0
fv=0
tw=0
on=0
while(amount>=2000):
    tt=tt+1
    amount=amount-2000
while(amount>=500):
    fh=fh+1
    amount=amount-500
while(amount>=200):
    th=th+1
    amount=amount-200
while(amount>=100):
    oh=oh+1
    amount=amount-100
while(amount>=50):
    ft=ft+1
    amount=amount-50
while(amount>=20):
    ty=ty+1
    amount=amount-20
while(amount>=10):
    tn=tn+1
    amount=amount-10
while(amount>=5):
    fv=fv+1
    amount=amount-5
while(amount>=2):
    tw=tw+1
    amount=amount-2
while(amount>=1):
    on=on+1
    amount=amount-1
if tt>0:
    print('2000:'+str(tt))
if fh>0:
    print('500:'+str(fh))
if th>0:
    print('200:',th)
if oh>0:
    print('100:',oh)
if ft>0:
    print('50:',ft)
if ty>0:
    print('20:',ty)
if tn>0:
    print('10:',tn)
if fv>0:
    print('5:',fv)
if tw>0:
    print('2:',tw)
if on>0:
    print('1:',on)


