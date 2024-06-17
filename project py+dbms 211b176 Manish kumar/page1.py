from tkinter import*
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
#root.geometry('600x600')
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=2,columnspan=10,padx=w/3,pady=h/80)
Label(root,text='Online Bus Booking System',bg='light blue',font='Arial 14',fg='red').grid(row=1,column=3,columnspan=10,padx=w/3,pady=h/80)
Label(root,text=' Manish Kumar',fg='blue violet',font='Arial 12').grid(row=5,column=3,padx=w/3,pady=h/90)
Label(root,text=' 211B176',fg='blue violet',font='Arial 12').grid(row=6,column=3,padx=w/3,pady=h/90)
Label(root,text=' 8932085486',fg='blue violet',font='Arial 12').grid(row=7,column=3,padx=w/3,pady=h/90)
Label(root,text=' Submitted to: Dr.Mahesh Kumar',bg='light blue',fg='blue',font='Arial 14').grid(row=8,column=3,padx=w/3)
Label(root,text=' Project based Learning',fg='Red',font='Arial 12').grid(row=9,column=3,padx=w/3)
def fun(e=0):
    root.destroy()
    import page2
Button(root,text='Next Page',bg='violet red',font='Arial 12',command=fun).grid(row=10,column=5,padx=w//100)

root.mainloop()
