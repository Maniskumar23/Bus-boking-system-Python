from tkinter import*
import sqlite3
con=sqlite3.connect('Bus_project_db.db')
cur=con.cursor()
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,columnspan=10,pady=10)
Label(root,text='Add Bus Operator Details',bg='violet').grid(row=3,column=0,columnspan=10,pady=10)
Label(root,text='Operator id').grid(row=4,column=0)
a=Entry(root)
a.grid(row=4,column=1)

Label(root,text='Name').grid(row=4,column=2)
b=Entry(root)
b.grid(row=4,column=3)

Label(root,text='Address ').grid(row=4,column=4)
c=Entry(root)
c.grid(row=4,column=5)

Label(root,text='Phone ').grid(row=4,column=6)
d=Entry(root)
d.grid(row=4,column=7)

Label(root,text='Email ').grid(row=4,column=8)
e=Entry(root)
e.grid(row=4,column=9)


Button(root,text='Edit',bg='violet red',font='Arial 12').grid(row=4,column=11)
def fun_home():
    root.destroy()
    import page2
Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=5,column=9)
#cur.execute('create table Operator_detail(Operator_id int(4),Name varchar(20),Address varchar(50),Phone int(10),Email varchar(20),primary key(Operator_id,Phone))')

def ila():
    aa=a.get()
    bb=b.get()
    cc=c.get()
    dd=d.get()
    ee=e.get()
    Label(root,text=a.get()+' '+b.get()+' '+c.get()+' '+d.get()+' '+e.get()).grid(row=5,column=4)
    cur.execute('insert into Operator_detail values(?,?,?,?,?)',((aa),(bb),(cc),(dd),(ee)))

    con.commit()

    cur.execute('select name,Operator_id from Operator_detail')
    res=cur.fetchall()
    def selection():
        r=v.get()
        selected="You selected the option"+ res[r][0]
        Label(root,text=selected).grid(row=9,column=8)
    v=IntVar(root,1)
    i=3
    for(text,value) in res:
         Radiobutton(root, text = text, variable = v,
                value = value, indicator = 0,
                background = "light blue",command=selection).grid(row=7,column=i, ipady = 5)
         i=i+1
        
    
    con.close()

Button(root,text='Add',bg='violet red',font='Arial 12',command=ila).grid(row=4,column=10)
