from tkinter import*
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="student")

win=Tk()
win.geometry('500x500+250+100')
win.title("DATABASE APPLICATION")


def insert_data():
    reg_no=reg.get()
    nam=name.get()
    mycursor=mydb.cursor()
    sql="insert into stu_details(regno,name) values(%s,%s)"
    val=(reg_no,nam)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Data inserted")

def show_data():
    r=reg.get()
    print(r)
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM stu_details")
    myresult=mycursor.fetchall()

    for x in myresult:
        print(x)

def search_data():
    r=reg.get()
    print(r)
    mycursor=mydb.cursor()
    mycursor.execute("select name from stu_details where regno=%s",(r,))
    myresult=mycursor.fetchone()
    if myresult!=None:
        for x in myresult:
            print(x)
            name.delete(0,'end')
            name.insert(0,x)
    else:
        name.delete(0,'end')
        name.insert(0,"notfound")

def edit_data():
    reg_no=int(reg.get())
    nam=name.get()
    mycursor=mydb.cursor()
    sql="update stu_details set name=%s where regno=%s"
    val=(nam,reg_no)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"record(s) affected...")

def delete_data():
    reg_no=reg.get()
    mycursor=mydb.cursor()
    #sql="delete from stu_details where regno=%s"
    #val=(reg_no)
    mycursor.execute("delete from stu_details where regno=%s",(reg_no,))
    mydb.commit()
    print(mycursor.rowcount,"Record Deleted...")
    reg.delete(0,END)
    name.delete(0,END)
    reg.focus_set()

l1=Label(win,text="Register No",fg="red",bg="orange")
l1.place(x=50,y=50)
l2=Label(win,text="Name",fg="red",bg="orange")
l2.place(x=50,y=100)

reg=Entry(win)
reg.place(x=150,y=50)
name=Entry(win)
name.place(x=150,y=100)

b1=Button(win,text="Save",command=insert_data)
b1.place(x=50,y=200)
b2=Button(win,text="Display",command=show_data)
b2.place(x=150,y=200)
b3=Button(win,text="Search",command=search_data)
b3.place(x=250,y=200)
b4=Button(win,text="Update",command=edit_data)
b4.place(x=350,y=200)
b5=Button(win,text="Delete",command=delete_data)
b5.place(x=450,y=200)

win.mainloop()




















    

    

    
