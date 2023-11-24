def mysubtract():
    a=int(num1.get())
    b=int(num2.get())
    s=a-b
    res='Result: '+str(s)
    l3.config(text=res)

from tkinter import *
subtracting=Tk()
subtracting.title("Subtracting two numbers")
l1=Label(subtracting,text="Enter First Number: ")
num1=Entry(subtracting)
l2=Label(subtracting,text="Enter Second Number: ")
num2=Entry(subtracting)
b=Button(subtracting,text="Subtract",command=mysubtract)
l3=Label(subtracting,text="Result: ")

l1.grid(row=0,column=0)
num1.grid(row=0,column=1)


l2.grid(row=1,column=0)
num2.grid(row=1,column=1)

b.grid(row=2,column=0)
l3.grid(row=2,column=1)

subtracting.mainloop()
