from tkinter import*
import sqlite3

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

con=sqlite3.connect('Bus_project_db.db')
cur=con.cursor()

img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label().grid(row=4,column=0,padx=w//50)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,columnspan=10,pady=10)
Label(root,text='check Your Booking',bg='violet').grid(row=3,column=0,columnspan=10,pady=10)
Label(root,text='Enter your mobile No: ').grid(row=4,column=3)
a=Entry(root)
a.grid(row=4,column=4)
Label(root,text='Enter your Bus id: ').grid(row=5,column=3)
b=Entry(root)
b.grid(row=5,column=4)
#cur.execute('create table Mobile_no(Mobile_no varchar(10),Bus_id int(3))')

def print_ticket():
    aa=a.get()
    bb=b.get()

    cur.execute('insert into Mobile_no values(?,?)',((aa),(bb)))
    con.commit()
    cur.execute("""SELECT p.Name,p.Gender,P.No_of,p.age,p.Mobile_no
                FROM Passenger_detail as p,Mobile_no as m,Bus_detail as b,Journey_detail as j
                WHERE p.Mobile_no=m.Mobile_no""")
    
    q=cur.fetchall()
    print("result ",q)
    Label(root,text='Name: ',font='Arial 14').grid(row=7,column=3)
    Label(root,text='Gender: ',font='Arial 14').grid(row=7,column=5)
    Label(root,text='Seates boooked: ',font='Arial 14').grid(row=8,column=3)
    Label(root,text=' Age: ',font='Arial 14').grid(row=8,column=5)
    Label(root,text='Mobile No: ',font='Arial 14').grid(row=9,column=3)
    Label(root,text='Fare Rs: ',font='Arial 14').grid(row=9,column=5)
    Label(root,text='To: ',font='Arial 14').grid(row=10,column=3)
    Label(root,text='From: ',font='Arial 14').grid(row=10,column=5)
    for j in q:
        Label(root,text=j[0],font='Arial 14').grid(row=7,column=4)
        Label(root,text=j[1],font='Arial 14').grid(row=7,column=6)
        Label(root,text=j[2],font='Arial 14').grid(row=8,column=4)
        Label(root,text=j[3],font='Arial 14').grid(row=8,column=6)
        '''
        Label(root,text=j[4],font='Arial 14').grid(row=9,column=4)
        Label(root,text=j[5],font='Arial 14').grid(row=9,column=6)
        Label(root,text=j[6],font='Arial 14').grid(row=10,column=4)
        Label(root,text=j[7],font='Arial 14').grid(row=10,column=6)'''
    

    
Button(root,text='check booking ',bg='violet red',font='Arial 12',command=print_ticket).grid(row=4,column=5)

def fun_home():
    root.destroy()
    import page2
Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=5,column=8)
