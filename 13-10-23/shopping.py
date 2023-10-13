#offer promo code DUSHERRA-50%,SUNDAY-40%
dn=100
dress=200
perfume=300
shoes=400
print('*****Welcome to PHOENIX mall')
cname=input('Enter customer name: ')
cphno=input('Enter Phno: ')
dno=int(input('Enter no. of doughnuts: '))
drn=int(input('Enter no. of dresses: '))
pfn=int(input('Enter no. of perfume bottles: '))
shn=int(input('Enter no. of shoes: '))
pc=input('Enter promo code: ')
bill=(dn*dno)+(drn*dress)+(pfn*perfume)+(shn*shoes)
if pc=='DUSHERRA' or pc=='dusherra':
    disc=bill*50/100
elif pc=='SUNDAY' or pc=='sunday':
    disc=bill*40/100
elif bill>=2000:
    disc=bill*20/100
elif bill>=1000:
    disc=bill*10/100
elif bill>=500:
    disc=bill*5/100
else:
    disc=bill*3/100
tbill=bill-disc
gst=tbill*12/100
obill=tbill+gst
print('\nCustomer name:',cname)
print('Customer phno:',cphno)
print('Bill:',bill)
print('Discount:',disc)
print('Gst 12%:',gst)
print('Total bill to be paid:',obill)
print('**Thank you! Visit Again***')
