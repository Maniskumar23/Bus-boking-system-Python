from tkinter import*
import sqlite3
con=sqlite3.connect('Bus_project_db.db')
cur=con.cursor()
root=Tk()

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,
columnspan=10,pady=10)
Label(root,text='Add Bus Details',bg='violet').grid(row=3,column=0,columnspan=10,pady=10)

Label(root,text='Bus id').grid(row=4,column=1)
q=Entry(root)
q.grid(row=4,column=2)
Label(root,text='Running Date').grid(row=4,column=3)
w=Entry(root)
w.grid(row=4,column=4)
Label(root,text='Seat Available ').grid(row=4,column=5)
e=Entry(root)
e.grid(row=4,column=6)


Button(root,text='Delete Run',bg='violet red',font='Arial 12').grid(row=4,column=8)
def fun_home():
    root.destroy()
    import page2
Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=9,column=8)
cur.execute('create table New_run_detail(Bus_id int(4),Running_date date,Seat_available int(2))')

def ila():
    qq=q.get()
    ww=w.get()
    ee=e.get()
    cur.execute('insert into New_run_detail values(?,?,?)',((qq),(ww),(ee)))

    con.commit()

    cur.execute('select * from New_run_detail')
    res=cur.fetchall()
    print('result:',res)
    
    con.close()
Button(root,text='Add Run ',bg='violet red',font='Arial 12',command=ila).grid(row=4,column=7)



