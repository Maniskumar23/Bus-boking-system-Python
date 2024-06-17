from tkinter import*
from tkinter import messagebox
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
Label(root,text='Enter Journey Details',bg='violet').grid(row=3,column=0,columnspan=10,pady=10)
Label(root,text='To').grid(row=4,column=0)
q=Entry(root)
q.grid(row=4,column=1)
Label(root,text='From').grid(row=4,column=2)
w=Entry(root)
w.grid(row=4,column=3)
Label(root,text='Journey Date').grid(row=4,column=4)
e=Entry(root)
e.grid(row=4,column=5)




'''
def inf():
    Button(root,text='Procees to book',bg='violet red',font='Arial 12').grid(row=8,column=6)
Button(root,text='Show bus',bg='violet red',font='Arial 12',command=inf).grid(row=4,column=7)
'''
def fun_home():
    root.destroy()
    import page2

Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=4,column=8)

def ila(r):
    Label(root,text='Fill Passenger Details to book the bus ticket',bg='light blue',font='Arial 14',fg='red').grid(row=9,column=0,
    columnspan=10,pady=10)
    Label(root,text='Name').grid(row=11,column=0)
    a=Entry(root)
    a.grid(row=11,column=1)
    Label(root,text='Gender').grid(row=11,column=2)
    #Entry(root).grid(row=9,column=3)
    menu=StringVar()
    menu.set("choose")
    de=OptionMenu(root,menu,"male","female","trans")
    de.grid(row=11,column=3)
    Label(root,text='No of seates').grid(row=11,column=4)
    s=Entry(root)
    s.grid(row=11,column=5)
    Label(root,text='Mobile No').grid(row=11,column=6)
    d=Entry(root)
    d.grid(row=11,column=7)
    Label(root,text='Age').grid(row=11,column=8)
    f=Entry(root)
    f.grid(row=11,column=9)

    def fun2():
        aa=a.get()
        mm=menu.get()
        ss=s.get()
        dd=d.get()
        ff=f.get()
        
        cur.execute('insert into Passenger_detail values(?,?,?,?,?,?)',((aa),(mm),(ss),(dd),(ff),(r)))
        con.commit()
        cur.execute('select * from Passenger_detail')
        res=cur.fetchall()
        print('result:',res)
        con.close()
    Button(root,text='Book Seat',bg='violet red',font='Arial 12',command=fun2).grid(row=9,column=10)

#Button(root,text='Procees to book',bg='violet red',font='Arial 12',command=ila).grid(row=8,column=6)


def inf():
    def fun():
        
        qq=q.get()
        ww=w.get()
        ee=e.get()
        cur.execute('insert into Journey_detail values(?,?,?)',((qq),(ww),(ee)))
        con.commit()
        cur.execute("""SELECT b.Bus_id,b.Operator_id
                        FROM Bus_detail as b,Journey_detail as j,New_route as n,New_run_detail as r
                        WHERE j.To_=n.D_name AND j.From_=n.Station_name AND n.Route_id=r.Route_id AND r.Bus_id=b.Bus_id AND j.Journey_Date=r.Running_date""")
        res=cur.fetchall()
        print('result:',res)
        def selection(r):
            
            
            selected=res[r][0]
            Label(root,text=selected).grid(row=5,column=10)
            
        v=IntVar(root,1)
        i=6
        r=v.get()
        for(text,value) in res:
             Radiobutton(root, text = 'BUS AVAILABLE', variable = v,
                    value = value, indicator = 0,
                    background = "orange",command=lambda:selection(r)).grid(row=i,column=2, ipady = 5)
             cur.execute("""SELECT b.Bus_type,b.capacity,b.Fare_rs,B.Operator_id
                        FROM Bus_detail as b,Journey_detail as j,New_route as n,New_run_detail as r
                        WHERE j.To_=n.D_name AND j.From_=n.Station_name AND n.Route_id=r.Route_id AND r.Bus_id=b.Bus_id AND j.Journey_Date=r.Running_date""")
             res1=cur.fetchall()
             for j in res1:
                 Label(root,text=j[0],font='Arial 14').grid(row=6,column=3)
                 Label(root,text=j[1],font='Arial 14').grid(row=6,column=4)
                 Label(root,text=j[2],font='Arial 14').grid(row=6,column=5)
                 Label(root,text=j[3],font='Arial 14').grid(row=6,column=6)
             #Label(root,text=res1,bg='light blue',font='Arial 14').grid(row=i,column=3)
             
             Label(root,text='Bus_type ',bg='light blue',font='Arial 14').grid(row=5,column=3)
             Label(root,text=' capacity ',bg='light blue',font='Arial 14').grid(row=5,column=4)
             Label(root,text=' Fare ',bg='light blue',font='Arial 14').grid(row=5,column=5)
             Label(root,text=' Operator_id',bg='light blue',font='Arial 14').grid(row=5,column=6)
             i=i+1
        Button(root,text='confirm',bg='violet red',font='Arial 12',command=lambda:ila(r)).grid(row=5,column=11)    
        cur.execute('delete from Journey_detail')
    fun()
    
Button(root,text='Show bus',bg='violet red',font='Arial 12',command=inf).grid(row=4,column=7)





#cur.execute('create table Journey_detail(To_ varchar(50),From_ varchar(50),Journey_Date date)')

#cur.execute('create table Passenger_detail(Name varchar(50),Gender varchar(10),No_of seates int(2),Mobile_no int(10),age int(2))')



    

