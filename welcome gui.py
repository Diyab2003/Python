from tkinter import*
root= Tk()
root.title("Welcome")
root.geometry('400x300')

def print_text():
    text1 = e1.get()
    text2= e2.get()
    print(text1)
    print(text2)



name=Label(root,text="Name")
name.place(x=50,y=50)
e1=Entry(root)
e1.place(x=100,y=50)
regno=Label(root,text="Regd No:")
regno.place(x=50,y=100)
e2=Entry(root)
e2.place(x=110,y=100)
b=Button(root,text="ENTER",command =print_text)
b.place(x=120,y=150)



root.mainloop()
