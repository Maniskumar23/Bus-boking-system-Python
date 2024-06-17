from tkinter import*
import sqlite3

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))


con=sqlite3.connect('Bus_project_db.db')
cur=con.cursor()
cur.execute('create table New_route(Route_id number primary key,Station_name varchar(5),Station_Id number)')


img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,
columnspan=10,pady=10)
Label(root,text='Add Bus Details',bg='violet').grid(row=3,column=0,columnspan=10,pady=10)
Label(root,text='Rout id').grid(row=4,column=0)
q=Entry(root)
q.grid(row=4,column=1)
Label(root,text='Station Name').grid(row=4,column=2)
w=Entry(root)
w.grid(row=4,column=3)
Label(root,text='Station Id ').grid(row=4,column=4)
e=Entry(root)
e.grid(row=4,column=5)


Button(root,text='Delete Route',bg='violet red',font='Arial 12').grid(row=4,column=8)
def fun_home():
    root.destroy()
    import page2
Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=9,column=8)

def submit():
    qq=q.get()
    ww=w.get()
    ee=e.get()
    cur.execute('insert into New_route values(?,?,?)',(qq,ww,ee))

    con.commit()
    
    cur.execute('select * from New_route')
    res=cur.fetchall()
    print('result:',res)
    
    con.close()

Button(root,text='Add Route ',bg='violet red',font='Arial 12',command=submit).grid(row=4,column=6)
