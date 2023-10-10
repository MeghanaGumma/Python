p=float(input("Enter principle amount: "))
n=float(input("Enter number of years: "))
r=float(input("Enter rate of interest: "))
si=(p*n*r)/100
emi=(si+p)/(12*n)
print("EMI value = ",emi)
