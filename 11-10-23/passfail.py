sno=int(input("Enter Sno: "))
sname=input("Enter Sname: ")
gr=input("Enter Group: ")
s1=float(input("Enter S1 marks: "))
s2=float(input("Enter S2 marks: "))
s3=float(input("Enter S3 marks: "))
print("\nSNO = ",sno,"\nSNAME = ",sname,"\nGROUP = ",gr)
if((s1>=40)and(s2>=40)and(s3>=40)):
    print("PASS")
else:
    print("FAIL")
