from tkinter import*
import sqlite3
con=sqlite3.connect('Bus_project_db.db')
cur=con.cursor()
root=Tk()


#cur.execute('create table To_From_detail(Bus_id int(4),To_ varchar(50),From_ varchar(50))')
cur.execute('insert into To_From_detail values(321,"indore","guna")')
cur.execute('insert into To_From_detail values(654,"bhopal","guna")')
cur.execute('insert into To_From_detail values(987,"gwalior","guna")')

con.commit()

cur.execute('select * from To_From_detail')
res=cur.fetchall()
print('result:',res)
