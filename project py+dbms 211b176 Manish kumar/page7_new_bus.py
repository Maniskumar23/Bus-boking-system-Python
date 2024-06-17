from tkinter import*
import sqlite3

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))


con=sqlite3.connect('Bus_project_db.db')
cur=con.cursor()
#cur.execute('create table Bus_detail(Bus_id int(4) primary key,Bus_type varchar(5),capacity int(4),Fare_rs int(4),Operator_id int(4),Route_id int(4))')
img=PhotoImage(file='.\\Bus_for_project.png')



Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,
columnspan=10,pady=10)
Label(root,text='Add Bus Details',bg='violet').grid(row=3,column=0,columnspan=10,pady=10)

Label(root,text='Bus id').grid(row=4,column=0)
B=Entry(root)
B.grid(row=4,column=1)

Label(root,text='Bus Type').grid(row=4,column=2)

Label(root,text='Capacity ').grid(row=4,column=4)
c=Entry(root)
c.grid(row=4,column=5)

Label(root,text='Fare Rs ').grid(row=4,column=6)
F=Entry(root)
F.grid(row=4,column=7)

Label(root,text='Operator Id ').grid(row=4,column=8)
O=Entry(root)
O.grid(row=4,column=9)

Label(root,text='Rout Id ').grid(row=4,column=10)
R=Entry(root)
R.grid(row=4,column=11)


def fun_home():
    root.destroy()
    import page2
Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=9,column=8)



b=StringVar()
b.set("select bus type")
d_menu=OptionMenu(root,b,"2x2","3x2","3x3","AC 3x2")
d_menu.grid(row=4,column=3)

def submit():
    BB=B.get()
    bb=b.get()
    cc=c.get()
    ff=F.get()
    Oo=O.get()
    rr=R.get()
    cur.execute('insert into Bus_detail values(?,?,?,?,?,?)',((BB),(bb),(cc),(ff),(Oo),(rr)))
    con.commit()
    cur.execute('select * from Bus_detail')
    res=cur.fetchall()
    print('result:',res)
    con.close()
Button(root,text='Add Bus ',bg='violet red',font='Arial 12',command=submit).grid(row=9,column=6)
Button(root,text='Edit Bus',bg='violet red',font='Arial 12').grid(row=9,column=7)

root.mainloop()
