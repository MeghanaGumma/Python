def myresult():
    s1=float(sem1marks.get())
    s2=float(sem2marks.get())
    s3=float(sem3marks.get())
    s4=float(sem4marks.get())
    s5=float(sem5marks.get())
    s6=float(sem6marks.get())
    total=s1+s2+s3+s4+s5+s6
    c=round(total/6,2)
    cgpa=total//6
    if cgpa==10:
        gr="O"
    elif cgpa==9:
        gr='A+'
    elif cgpa==8:
        gr='A'
    elif cgpa==7:
        gr='B'
    elif cgpa==6:
        gr='C'
    elif cgpa==5:
        gr='D'
    elif cgpa==4:
        gr='P'
    else:
        gr='F'
    s="CGPA: "+str(c)+"  Grade: "+gr
    res.config(text=s)

from tkinter import *
result=Tk()
result.title("Student Result")
sem1=Label(result,text="Enter Semester 1 Marks:")
sem1marks=Entry(result)
sem2=Label(result,text="Enter Semester 2 Marks:")
sem2marks=Entry(result)
sem3=Label(result,text="Enter Semester 3 Marks:")
sem3marks=Entry(result)
sem4=Label(result,text="Enter Semester 4 Marks:")
sem4marks=Entry(result)
sem5=Label(result,text="Enter Semester 5 Marks:")
sem5marks=Entry(result)
sem6=Label(result,text="Enter Semester 6 Marks:")
sem6marks=Entry(result)
b1=Button(result,text="Submit",command=myresult)
b2=Button(result,text="Cancel",command=exit)
res=Label(result,text="?")

sem1.grid(row=0,column=0)
sem1marks.grid(row=0,column=1)

sem2.grid(row=1,column=0)
sem2marks.grid(row=1,column=1)

sem3.grid(row=2,column=0)
sem3marks.grid(row=2,column=1)

sem4.grid(row=3,column=0)
sem4marks.grid(row=3,column=1)

sem5.grid(row=4,column=0)
sem5marks.grid(row=4,column=1)

sem6.grid(row=5,column=0)
sem6marks.grid(row=5,column=1)

b1.grid(row=6,column=0)
b2.grid(row=6,column=1)
res.grid(row=8,column=0)

result.mainloop()

