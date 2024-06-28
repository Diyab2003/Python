from tkinter import*
root= Tk()
root.title("Calculator")
root.geometry('400x300+250x100')
def add():
    txt3.delete(0,END)
    a=int(txt1.get())
    b=int(txt2.get())
    c=a+b
    txt3.insert(0,c)
def sub():
    txt3.delete(0,END)
    a=int(txt1.get())
    b=int(txt2.get())
    c=a-b
    txt3.insert(0,c)
def mul():
    txt3.delete(0,END)
    a=int(txt1.get())
    b=int(txt2.get())
    c=a*b
    txt3.insert(0,c)
def div():
    txt3.delete(0,END)
    a=int(txt1.get())
    b=int(txt2.get())
    c=a/b
    txt3.insert(0,c)
def clear():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt1.focus_set()
l1=Label(win,text="First no:",font="Times New Roman",fg="blue",bg="white").place(x=10,y=10)
l2=Label(win,text="Second no:",font="Times New Roman",fg="blue",bg="white").place(x=10,y=40)
l3=Label(win,text="Third no:",font="Times New Roman",fg="blue",bg="white").place(x=10,y=20) 


txt1 = Entry(root)
txt1.place(x=120, y=10)
txt2 = Entry(root)
txt2.place(x=120, y=40)
txt3 = Entry(root)
txt3.place(x=120, y=70)


btn_add = Button(root, text="Add", width=10, command=add)
btn_add.place(x=10, y=100)
btn_sub = Button(root, text="Subtract", width=10, command=sub)
btn_sub.place(x=100, y=100)
btn_mul = Button(root, text="Multiply", width=10, command=mul)
btn_mul.place(x=190, y=100)
btn_div = Button(root, text="Divide", width=10, command=div)
btn_div.place(x=280, y=100)
btn_clear = Button(root, text="Clear", width=10, command=clear)
btn_clear.place(x=10, y=140)


root.mainloop()
