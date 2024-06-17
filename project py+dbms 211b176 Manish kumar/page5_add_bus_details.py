from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
#root.geometry('600x600')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=2,column=0,columnspan=10,pady=10)
Label(root,text='Add new Details to Database',bg='orange',font='Arial 14',fg='white').grid(row=3,column=0,columnspan=10,pady=10)
def fun(e=0):
    root.destroy()
    import page6_new_operator
Button(root,text='New operator',bg='violet red',font='Arial 12',command=fun).grid(row=4,column=2,columnspan=3,pady=10)
def fun1(i=0):
    root.destroy()
    import page7_new_bus 
Button(root,text='New Bus',bg='violet red',font='Arial 12',command=fun1).grid(row=4,column=3,columnspan=3,pady=10)
def fun2(q=0):
    root.destroy()
    import page8_new_route
Button(root,text='New Rout',bg='violet red',font='Arial 12',command=fun2).grid(row=4,column=4,columnspan=3,pady=10)
def fun3(w=0):
    root.destroy()
    import page9_new_run
Button(root,text='New Run',bg='violet red',font='Arial 12',command=fun3).grid(row=4,column=5,columnspan=3,pady=10)

def fun_home():
    root.destroy()
    import page2
Img=PhotoImage(file='.\\home.png')
Button(root,image=Img,command=fun_home).grid(row=4,column=7)
